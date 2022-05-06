import actionlib
import rospy
import time
import subprocess
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from positional_error import *
from rns import *
from goals import *

goal = MoveBaseGoal()
goal.target_pose.header.frame_id = 'odom' 

def target(x, y, z, w):
    goal.target_pose.pose.position.x = x
    goal.target_pose.pose.position.y = y
    goal.target_pose.pose.orientation.z = z
    goal.target_pose.pose.orientation.w = w

def GetCurrPose():
    subprocess.check_call("python current_pose.py '%s'", shell=True)

def PoseSamples():
    subprocess.check_call("python pose_samples.py '%s'", shell=True)    


if __name__ == "__main__":
    rospy.init_node('send_client_goal')
    client = actionlib.SimpleActionClient('/move_base', MoveBaseAction)
    rospy.loginfo("Mission in progress...")
    client.wait_for_server()    

    start_time = time.time()
    
    # This is where we define mission specifications
    # ----------------Target 1----------------
    target(goal1_x, goal1_y, goal1_z, goal1_w)
    client.send_goal(goal)
    client.wait_for_result()  
    GetCurrPose()
    PoseSamples()
    cx = open("log/cx.txt", "r")
    curr_x = cx.read()
    curr_x = float(curr_x)
    rns(curr_x, goal1_x)
    PosError(goal1_x, goal1_y)  
    cx.close()

   # ----------------Target 2----------------
    target(goal2_x, goal2_y, goal2_z, goal2_w)
    client.send_goal(goal)
    client.wait_for_result()   
    GetCurrPose()
    cx = open("log/cx.txt", "r")
    curr_x = cx.read() 
    curr_x = float(curr_x)     
    rns(curr_x, goal2_x)
    time.sleep(0.5)
    PosError(goal2_x, goal2_y)
    cx.close()

    # ----------------Target 3----------------
    target(goal3_x, goal3_y, goal3_z, goal3_w)
    client.send_goal(goal)
    client.wait_for_result()   
    GetCurrPose()
    cx = open("log/cx.txt", "r")
    curr_x = cx.read() 
    curr_x = float(curr_x)    
    rns(curr_x, goal3_x) 
    PosError(goal3_x, goal3_y)  
    cx.close()

    # ----------------Target 4----------------
    target(goal4_x, goal4_y, goal4_z, goal4_w)
    client.send_goal(goal)
    client.wait_for_result()      
    GetCurrPose()
    cx = open("log/cx.txt", "r")
    curr_x = cx.read() 
    curr_x = float(curr_x)     
    rns(curr_x, goal4_x)   
    PosError(goal4_x, goal4_y) 
    cx.close() 

    # ----------------Target 5----------------
    target(goal5_x, goal5_y, goal5_z, goal5_w)
    client.send_goal(goal)
    client.wait_for_result()       
    GetCurrPose()
    cx = open("log/cx.txt", "r")
    curr_x = cx.read() 
    curr_x = float(curr_x)     
    rns(curr_x, goal5_x)
    PosError(goal5_x, goal5_y)
    cx.close()

    time.sleep(0.5)
    CalcRns() 
    ResetRNS()


    end_time = round((time.time() - start_time), 2)
    with open('log/mission_time.txt', 'w') as f:
        f.write(str(end_time))
        f.close()