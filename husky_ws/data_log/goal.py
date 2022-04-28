import actionlib
import rospy
import time
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal, MoveBaseFeedback, MoveBaseResult

# def done_cb(status, result):
#     if status == 3:
#         rospy.loginfo("Goal reached")
#     if status == 2 or status == 8:
#         rospy.loginfo("Goal cancelled")        
#     if status == 4:
#         rospy.loginfo("Goal aborted")

rospy.init_node('send_client_goal')

client = actionlib.SimpleActionClient('/move_base', MoveBaseAction)
rospy.loginfo("Waiting for move base server")
client.wait_for_server()

goal = MoveBaseGoal()
goal.target_pose.header.frame_id = 'odom' 
goal.target_pose.pose.position.x = 14.5426712036
goal.target_pose.pose.position.y = -0.691165924072
goal.target_pose.pose.orientation.z = -0.0198330671035
goal.target_pose.pose.orientation.w = 0.99980330538

start_time = time.time()
client.send_goal(goal)
client.wait_for_result()
end_time = round((time.time() - start_time), 2)
with open('mission_time.txt', 'w') as f:
    f.write(str(end_time))
    f.close()
#print("Mission time: " + str(end_time))
