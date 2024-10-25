#!/usr/bin/python3
import rospy
from std_msgs.msg import String

def publisher():
    rospy.init_node("nimisha")
    pub=rospy.Publisher("hello_class",String,queue_size=20)
    rospy.Subscriber("welcome",String)
    rate=rospy.Rate(10)
    #rospy.loginfo("")
    msg=String()
    msg.data="HELLO RAA24_26 !"
    while not rospy.is_shutdown():
         
         pub.publish(msg)
         rospy.loginfo(msg.data)
         rate.sleep()
if __name__=='__main__':
    try:
        publisher()
    except rospy.ROSInterruptException:
        pass
