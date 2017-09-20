#!/usr/bin/env python

import rospy

# Import our custom messages

from pos_estimator_msgs.msg import OdomTrainData


def callback_odom_train_data():
    # Do stuff when we receive new training data



def odom_organizer_node()

    rospy.init_node('odom_organizer_node')
    rate = rospy.Rate(10) # 10Hz


    rospy.Subscriber('odom_train_data', OdomTrainData, callback_odom_train_data)

    while not rospy.is_shutdown():
        rate.sleep()



if __name__ == '__main__':

    try:
        odom_organizer_node()
    except rospy.ROSInterruptException:
        pass
