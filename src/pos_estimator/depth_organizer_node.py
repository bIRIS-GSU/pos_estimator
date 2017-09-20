#!/usr/bin/env python

import rospy

from pos_estimator_msgs.msg import DepthTrainImage



def callback_depth_train_image(msg):
    # Do stuff when we get a new training image


def depth_organizer_node():

    rospy.init_node('depth_organizer_node')
    rate = rospy.Rate(10) # Hz

    rospy.Subscriber('depth_train_image', DepthTrainImage, callback_depth_train_image)


    while not rospy.is_shutdown():
        rate.sleep()




if __name__ == '__main__':

    try:
        depth_organizer_node()
    except rospy.ROSInterruptException:
        pass
