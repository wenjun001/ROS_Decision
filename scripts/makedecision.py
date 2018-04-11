#!/usr/bin/env python

import rospy
from std_msgs.msg import String


pub = rospy.Publisher('makedecision', String)

def callback(data):
    rospy.loginfo("Get object detect message : %s",data.data)
    if "NO_"  in data.data: 
        rospy.loginfo("continue going")
        pub.publish("continue going")
    else:
        rospy.loginfo("let stop 5 second")
        pub.publish("stop 5 second")

    
def makedecision():

    rospy.init_node('makedecision', anonymous=True)

    rospy.Subscriber("/darknet_ros/object_detect/result", String, callback)
    rospy.spin()
        
if __name__ == '__main__':
    makedecision()
