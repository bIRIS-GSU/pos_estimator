#!/usr/bin/env python

import rospy

# Import our custom messages

from pos_estimator_msgs.msg import RGBEvalImage, RGBTrainImage, EstimatedPose

def callback_rgb_eval_image(msg):
    # Do stuff when a new evaluation image comes in


def callback_rgb_train_image(msg):
    # Do stuff when a new training image comes in



def rgb_cnn_node():

    rospy.init_node('rgb_cnn_world')
    rate = rospy.Rate(10) #10Hz

    rospy.Subscriber('rgb_eval_image', RGBEvalImage, callback_rgb_eval_image)
    rospy.Subscriber('rgb_train_image', RGBTrainImage, callback_rgb_train_image)

    rgb_eval_pose_publisher = rospy.Publisher('rgb_eval_pose', EstimatedPose, queue_size=10)

    while not rospy.is_shutdown():
        rate.sleep()




if __name__ == '__main__':

    try:
       rgb_cnn_node()
    except rospy.ROSInterruptException:
        pass
