#!/usr/bin/env python

import rospy

# Import our custom messages

from pos_estimator_msgs.msg import AcquireTrainData, AcquireEvalData, EstimatedPose, OdomEvalData, OdomTrainData
from nav_msgs import Odometry


def callback_acquire_train_data(msg):
    # Do stuff when told to acquire training data


def callback_acquire_eval_data(msg):
    # Do stuff when told to acquire evaluation data


def callback_current_location(msg):
    # Do stuff when informed of a new current location


def callback_odom(msg):
    # Do stuff when new odometry data


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
 
