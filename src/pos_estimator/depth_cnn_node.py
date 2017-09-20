#!/usr/bin/env python

import rospy

# Import our custom messages

from pos_estimator_msgs.msg import DepthEvalImage, DepthTrainImage, EstimatedPose

def callback_depth_eval_image(msg):
    # Do stuff when a new evaluation image comes in


def callback_depth_train_image(msg):
    # Do stuff when a new training image comes in



def depth_cnn_node():

    rospy.init_node('depth_cnn_world')
    rate = rospy.Rate(10) #10Hz

    rospy.Subscriber('depth_eval_image', DepthEvalImage, callback_depth_eval_image)
    rospy.Subscriber('depth_train_image', DepthTrainImage, callback_depth_train_image)

    depth_eval_pose_publisher = rospy.Publisher('depth_eval_pose', EstimatedPose, queue_size=10)

    while not rospy.is_shutdown():
        rate.sleep()




if __name__ == '__main__':

    try:
       depth_cnn_node()
    except rospy.ROSInterruptException:
        pass
