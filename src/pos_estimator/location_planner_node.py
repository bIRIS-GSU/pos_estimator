#!/usr/bin/env python

import rospy;

# Import our custom messages
from pos_estimator_msgs.msg import DestinationPose, EstimatedPose



def callback_current_location(msg):
    # Structure of argument 'msg' is:
    #    msg.estimated_pose.x
    #    msg.estimated_pose.y
    #    msg.estimated_pose.theta
    #    msg.confidence


def location_planner_node():

    rospy.init_node('pose_estimator_node')

    rospy.Subscriber('current_location', EstimatedPose, callback_current_location)
    destination_publisher = rospy.Publisher('destination_pose', DestinationPose, queue_size=10)

    rate = rospy.Rate(10) # 10Hz

    while not rospy.is_shutdown():
        rate.sleep();

        # Inside some logic within the while loop

	# new_destination = DestinationPose( x, y, theta )
        # destination_publisher.publish(new_destination)


if __name__ == '__main__':
    try:
        location_planner_node()
    except rospy.ROSInterruptException:
        pass
