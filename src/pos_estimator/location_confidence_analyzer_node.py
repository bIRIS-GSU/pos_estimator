#!/usr/bin/env python

import rospy

from pos_estimator_msgs.msg import EstimatedPose

def callback_odom_eval_pose(msg):


def callback_depth_eval_pose(msg):


def callback_rgb_eval_pose(msg):



def location_confidence_analyzer_node():

    rospy.init_node('location_confidence_analyzer_node')
    rate = rospy.Rate(10) # 10Hz

    rospy.Subscriber('odom_eval_pose', EstimatedPose, callback_odom_eval_pose)
    rospy.Subscriber('depth_eval_pose', EstimatedPose, callback_depth_eval_pose)
    rospy.Subscriber('rgb_eval_pose', EstimatedPose, callback_rgb_eval_pose)

    current_location_publisher = rospy.Publisher('current_location', EstimatedPose, queue_size=10)



    while not rospy.is_shutdown():
        rate.sleep()





if __name__ == '__main__':

    try:
        location_confidence_analyzer_node()
    except rospy.ROSInterruptException:
        pass
