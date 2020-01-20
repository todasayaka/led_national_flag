#!/usr/bin/env python

import rospy
from std_msgs.msg import Int32

def led_callback(msg):

    if msg == i :
        print ("CIV")
        with open("/dev/myled0", "w") as f:
	    f.write("0\n 1\n 2\n 3\n" )

    if msg == j :
        print ("ITA")
        with open("/dev/myled0", "w") as f:
            f.write("0\n 3\n 4\n 5\n" )

    if msg == k :
        print ("GNI")
        with open("/dev/myled0", "w") as f:
            f.write("0\n 5\n 6\n 7\n" )

if __name__ == "__main__":
        i = Int32(1)
        j = Int32(2)
        k = Int32(3)
	rospy.init_node("led_pub")
	sub = rospy.Subscriber("led", Int32, led_callback)
	rospy.spin()
