#!/usr/bin/python3 # shebang

import rospy
from std_msgs.msg import String

def publisher():
    rospy.init_node("nimisha_node1",anonymous=True)
    pub=rospy.Publisher("Greetings",String,queue_size=10)
    rate=rospy.Rate(10)
    rospy.loginfo("publishing text")
    while not rospy.is_shutdown():
        msg=String()
        msg.data="hello, I AM NIMISHA"
        rospy.loginfo(msg)
        pub.publish(msg)
        rate.sleep()
    
if __name__=="__main__":
    try:
        publisher()
    except rospy.ROSInterruptException:
      pass
