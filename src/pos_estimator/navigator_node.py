#!/usr/bin/env python

import rospy
from geometry_msgs import Twist

# Import our custom messages
from pos_estimator_msgs.msg import DestinationPose, EstimatedPose

def callback_destination_pose(msg):
    # Do stuff when a new destination is posted

def callback_estimated_pose(msg):
    # Do stuff when our current estimated position is updated




def navigator_node(): 

    rospy.init_node('navigator_node')

    rospy.Subscriber('destination_pose', DestinationPose, callback_destination_pose)
    rospy.Subscriber('current_location', EstimatedPose, callback_estimated_pose)

    velocity_publisher = rospy.Publisher('cmd_vel', Twist)

    rate = rospy.Rate(10) # 10Hz

    while not rospy.is_shutdown():
        rate.sleep();

        # Inside some logic within the while loop

	# new_velocity = Twist()
	# new_velocity.linear = [x,0,0]
        # new_velocity.angular = [0,0,z]
        # velocity_publisher.publish(new_velocity)


if __name__ == '__main__':
    try:
        navigator_node()
    except rospy.ROSInterruptException:
        pass


