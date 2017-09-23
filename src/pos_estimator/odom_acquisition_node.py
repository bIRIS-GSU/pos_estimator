#!/usr/bin/env python

# Description:
#
# Topics acquire_train_data and acquire_eval_data are calls to action. 
# When these topics are published to by the odom_acquisition_node, this
# node acquires the next data published to the odometry topic, and if 
# acquiring training data, also the next data published to the 
# current_location topic. Then, it publishes its data to odom_train_data
# or odom_eval_data, respectively

import rospy

# Import our custom messages

from pos_estimator_msgs.msg import AcquireTrainData, AcquireEvalData, EstimatedPose, OdomEvalData, OdomTrainData
from nav_msgs import Odometry


# Variables to indicate that we need to store incoming estimated_pose and odometry data
need_current_location = False
need_odom_data = False

# Variable to indicate whether we're acquiring training data or evaluation data
# True - acquiring eval data; False - acquiring train data; None - not acquiring data
need_evaluation_data = None

# Variables to store incoming estimated_pose and odometry data
current_location = EstimatedPose()
odom_location = OdomEvalData()


def publish_train_data(odom_data, cur_loc):
    global need_evaluation_data
    odom_train_data = OdomTrainData()
    odom_train_data.odom_pose = odom_data.odom_pose
    odom_train_data.estimated_pose = cur_loc.estimated_pose
    odom_train_data_publisher.publish(odom_train_data)
    need_evaluation_data = None


def publish_eval_data(odom_data):
    global need_evaluation_data
    odom_eval_data_publisher.publish(odom_data)
    need_evaluation_data = None



def callback_acquire_train_data(msg):
    # Do stuff when told to acquire training data
    global need_evaluation_data = False


def callback_acquire_eval_data(msg):
    # Do stuff when told to acquire evaluation data
    global need_evaluation_data = True


def callback_current_location(msg):
    # Do stuff when informed of a new current location
    global current_location    

    if (need_current_location == True):
        # current_location is of type EstimatedPose
        current_location = msg

        need_current_location = False;
        
        # If we need training data (== False) and we've already gotten odom data
        #  then we can publish
        if (need_evaluation_data == False and need_odom_data == False):
            
            odom_train_data_publisher.publish(odom_location, current_location)
            need_evaluation_data = None



def callback_odom(msg):
    # Do stuff when new odometry data
    global need_odom_data
    global need_current_location
    global odom_location
    global need_evaluation_data

    if (need_odom_data == True):
        # Calculate theta from the odometry quaternion
        euler = tf.transformations.euler_from_quaternion(msg.pose.quaternion)
        odom_location.odom_pose.theta = euler[2]

        # Copy x and y from the odometry pose into our EstimatedPose
        odom_location.odom_pose.x = msg.pose.pose.position.x
        odom_location.odom_pose.y = msg.pose.pose.position.y

        # Indicate we've obtained the odom_data as requested
        need_odom_data = False

        # If we only needed evaluation data, publish OdomEvalData
        if (need_evaluation_data == True):
            publish_eval_data(odom_location)
            return
        # If we need training data and we have current_location,
        #   publish OdomTrainData
        elif (need_evaluation_data == False and need_current_location == False):
            publish_train_data(odom_location, current_location)
            return
            

def odom_acquisition_node():

    rospy.init_node('odom_acquisition_node')
    rate = rospy.Rate(10) # 10Hz

    rospy.Subscriber('acquire_train_data', AcquireTrainData, callback_acquire_train_data)
    rospy.Subscriber('acquire_eval_data', AcquireEvalData, callback_acquire_eval_data)
    rospy.Subscriber('current_location', EstimatedPose, callback_current_location)
    rospy.Subscriber('odom', Odometry, callback_odom)

    odom_eval_data_publisher = rospy.Publisher('odom_eval_data', OdomEvalData, queue_size=10)
    odom_train_data_publisher = rospy.Publisher('odom_train_data', OdomTrainData, queue_size(10)


    while not rospy.is_shutdown():
        rate.sleep()


if __name__ == '__main__':

    try:
        odom_acquisition_node()
    except rospy.ROSInterruptException:
        pass
 
