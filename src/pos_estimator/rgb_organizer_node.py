#!/usr/bin/env python

import rospy

from pos_estimator_msgs.msg import RGBTrainImage



def callback_rgb_train_image(msg):
    # Do stuff when we get a new training image


def rgb_organizer_node():

    rospy.init_node('rgb_organizer_node')
    rate = rospy.Rate(10) # Hz

    rospy.Subscriber('rgb_train_image', RGBTrainImage, callback_rgb_train_image)


    while not rospy.is_shutdown():
        rate.sleep()




if __name__ == '__main__':

    try:
        rgb_organizer_node()
    except rospy.ROSInterruptException:
        pass
