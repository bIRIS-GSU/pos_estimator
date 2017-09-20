#!/usr/bin/env python

import rospy

# Import our custom messages

from pos_estimator_msgs.msg import DestinationPose, IsTraining, AcquireEvalData, AcquireTrainData, EstimatedPose

def callback_destination_pose(msg):
    # Do stuff when we get a new destination pose

def callback_is_training(msg):
    # Do stuff when our we change from training to evaluation (or vice versa)

def callback_current_location():
    # Do stuff when our current location changes


def location_checker_node():

    rospy.init_node('location_checker_node')

    rospy.Subscriber('destination_pose', DestinationPose, callback_destination_pose)
    rospy.Subscriber('is_training', IsTraining, callback_is_training)
    rospy.Subscriber('current_location', EstimatedPose, callback_current_location)

    acquire_train_data_publisher = rospy.Publisher('acquire_train_data', AcquireTrainData, queue_size=10)
    acquire_eval_data_publisher = rospy.Publisher('acquire_eval_data', AcquireEvalData, queue_size=10)

    rate = rospy.Rate(10) # 10Hz

    while not rospy.is_shutdown():
        rate.sleep()




if __name__ == '__main__':
    try:
       location_checker_node()
    except rospy.ROSInterruptException:
        pass  
