#!/usr/bin/env python


import rospy

# Import our custom messages

from pos_estimator_msgs.msg import OdomEvalData, OdomTrainData, EstimatedPose


def callback_odom_eval_data(msg):


def callback_odom_train_data(msg):



def odom_analyzer_node():

    rospy.init_node('odom_analyzer_node')
    rate = rospy.Rate(10) # 10Hz

    rospy.Subscriber('odom_eval_data', OdomEvalData, callback_odom_eval_data)
    rospy.Subscriber('odom_train_data', OdomTrainData, callback_odom_train_data)

    odom_eval_pose_publisher = rospy.Publisher('odom_eval_pose', EstimatedPose, queue_size=10)

    while not rospy.is_shutdown():
        rate.sleep()



if __name__ == '__main__':
    try:
        odom_analyzer_node()
    except rospy.ROSInterruptException:
        pass
