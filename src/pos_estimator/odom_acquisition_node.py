#!/usr/bin/env python

# Description:
#
# Topics acquire_train_data and acquire_eval_data are calls to action. 
# When these topics are published to by the location_checker_node, this
# node acquires the next data published to the odometry topic, and if 
# acquiring training data, also the next data published to the 
# current_location topic. Then, it publishes its data to odom_train_data
# or odom_eval_data, respectively

import rospy
import tf

# Import our custom messages

from pos_estimator_msgs.msg import AcquireTrainData, AcquireEvalData, EstimatedPose, OdomEvalData, OdomTrainData
from nav_msgs import Odometry

# Variables to store incoming estimated_pose and odometry data
current_location = EstimatedPose()
odom_location = OdomEvalData()

# I think these need to be in the global namespace
odom_eval_data_publisher = rospy.Publisher('odom_eval_data', OdomEvalData, queue_size=10)
odom_train_data_publisher = rospy.Publisher('odom_train_data', OdomTrainData, queue_size=10)


def callback_acquire_train_data(msg):
    # Do stuff when told to acquire training data
	odom_train_data = OdomTrainData()
	odom_train_data.odom_pose = odom_location.odom_pose
	odom_train_data.estimated_pose = current_location.pose
    global odom_train_data_publisher
	odom_train_data_publisher.publish(odom_train_data)


def callback_acquire_eval_data(msg):
    # Do stuff when told to acquire evaluation data
    global odom_eval_data_publisher
	odom_eval_data_publisher.publish(odom_location)


def callback_current_location(msg):
    global current_location = msg


def callback_odom(msg):
    # Do stuff when new odometry data
    global odom_location

	# Calculate theta from the odometry quaternion
	euler = tf.transformations.euler_from_quaternion(msg.pose.quaternion)
	odom_location.odom_pose.theta = euler[2]

	# Copy x and y from the odometry pose into our EstimatedPose
	odom_location.odom_pose.x = msg.pose.pose.position.x
	odom_location.odom_pose.y = msg.pose.pose.position.y

            

def odom_acquisition_node():

    rospy.init_node('odom_acquisition_node')
    rate = rospy.Rate(10) # 10Hz

    rospy.Subscriber('acquire_train_data', AcquireTrainData, callback_acquire_train_data)
    rospy.Subscriber('acquire_eval_data', AcquireEvalData, callback_acquire_eval_data)
    rospy.Subscriber('current_location', EstimatedPose, callback_current_location)
    rospy.Subscriber('odom', Odometry, callback_odom)

    


    while not rospy.is_shutdown():
        rate.sleep()


if __name__ == '__main__':

    try:
        odom_acquisition_node()
    except rospy.ROSInterruptException:
        pass
 
