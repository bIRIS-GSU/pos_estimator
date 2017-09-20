#!/usr/bin/env python

import rospy

# Import our custom messages

from pos_estimator_msgs.msg import AcquireTrainData, AcquireEvalData, EstimatedPose, DepthEvalImage, DepthTrainImage
from sensor_msgs.msg import Image



def callback_acquire_train_data(msg):
    # Do stuff when told to acquire training data

def callback_acquire_eval_data(msg):
    # Do stuff when told to acquire evaluation data


def callback_current_location(msg):
    # Do stuff when current location is updated


def callback_depth_image(msg):
    # Do stuff when a new depth image is posted


def depth_acquisition_node():

    rospy.init_node('depth_acquisition_node')
    rate = rospy.Rate(10) #10Hz


    rospy.Subscriber('acquire_train_data', AcquireTrainData, callback_acquire_train_data)
    rospy.Subscriber('acquire_eval_data', AcquireEvalData, callback_acquire_eval_data)
    rospy.Subscriber('current_location', EstimatedPose, callback_current_location)
    rospy.Subscriber('depth/image', Image, callback_depth_image)


    while not rospy.is_shutdown():
        rate.sleep()


if __name__ == '__main__':

    try:
        depth_acquisition_node() 
    except rospy.ROSInterruptException:
        pass
