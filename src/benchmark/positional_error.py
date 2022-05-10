import numpy as np
import pickle
import math
from goals import *

curr_pose_x = []
curr_pose_y = []

act_pose_x = []
act_pose_y = []

# Getting all the coordinates coming from the mission
def PosError(goal_x, goal_y):
    cx = open("log/cx.txt", "r")
    cy = open("log/cy.txt", "r")
    read_curr_x = cx.read()
    read_curr_y = cy.read()
    curr_pose_x.append(float(read_curr_x))
    curr_pose_y.append(float(read_curr_y))
    act_pose_x.append(goal_x)
    act_pose_y.append(goal_y)

    with open('log/curr_pose_x.ob', 'wb') as fp:
        pickle.dump(curr_pose_x, fp)
        fp.close()  
    with open('log/curr_pose_y.ob', 'wb') as fp:
        pickle.dump(curr_pose_y, fp)
        fp.close()   
    with open('log/act_pose_x.ob', 'wb') as fp:
        pickle.dump(act_pose_x, fp)
        fp.close()  
    with open('log/act_pose_y.ob', 'wb') as fp:
        pickle.dump(act_pose_y, fp)
        fp.close() 

    cx.close()
    cy.close()


# <---------Calculating positional metrics-------->

def successProba():
    with open('log/curr_pose_x.ob', 'rb') as fp:
        curr_x = pickle.load(fp)  
    with open('log/act_pose_x.ob', 'rb') as fp:
        act_x = pickle.load(fp) 
    with open('log/curr_pose_y.ob', 'rb') as fp:
        curr_y = pickle.load(fp) 
    with open('log/act_pose_y.ob', 'rb') as fp:
        act_y = pickle.load(fp) 

    del_x_g = np.subtract(act_x, curr_x)
    del_y_g = np.subtract(act_y, curr_y)
    sigma_x_g = np.std(del_x_g, ddof=1) # sample std
    sigma_y_g = np.std(del_y_g, ddof=1) # sample std
    twoDrms_g = 2 * math.sqrt((sigma_x_g ** 2) + (sigma_y_g ** 2))
    # print("successproba: ",twoDrms_g)


# 2Drms when groud truth is known
"""
We are getting samples when the robot reaches target 1 and
using those samples for our ground truth ground truth.
N.b. we discarded getting the samples when the robot first
spwan in the world because as the robot start moving it
would have more accuracte pose estimation. 
"""
def twoDrmsG():
    with open('log/x_samples.ob', 'rb') as fp:
        curr_x = pickle.load(fp)  
    with open('log/y_samples.ob', 'rb') as fp:
        curr_y = pickle.load(fp) 

    act_x = goal1_x  # This the ground truth of pose_x for the target 1
    act_y = goal1_y  # This the ground truth pose_y for the target 1
    del_x_g = [i - act_x for i in curr_x]
    del_y_g = [i - act_y for i in curr_y]
    sigma_x_g = np.std(del_x_g, ddof=1) # sample std
    sigma_y_g = np.std(del_y_g, ddof=1) # sample std
    twoDrms_g = 2 * math.sqrt((sigma_x_g ** 2) + (sigma_y_g ** 2))
    with open('log/twoDrmsG.txt', 'w') as f:
        f.write(str(twoDrms_g))
        f.close() 

def sigma():
    with open('log/x_samples.ob', 'rb') as fp:
        curr_x = pickle.load(fp)  
    with open('log/y_samples.ob', 'rb') as fp:
        curr_y = pickle.load(fp) 
    mean_curr_pose_x = sum(curr_x)/len(curr_x)
    mean_curr_pose_x = sum(curr_y)/len(curr_y)
    del_x = [i - mean_curr_pose_x for i in curr_x]
    del_y = [i - mean_curr_pose_x for i in curr_y]
    sigma.sigma_x = np.std(del_x, ddof=1) # sample std
    sigma.sigma_y = np.std(del_y, ddof=1) # sample std    

# 2Drms when groud truth is not known
"""
This is the traditional 2Drms 
"""
def twoDrms():
    two_Drms = 2 * math.sqrt((sigma.sigma_x ** 2) + (sigma.sigma_y ** 2))
    with open('log/twoDrms.txt', 'w') as f:
        f.write(str(two_Drms))
        f.close()    

# Drms 
"""
This is the traditional Drms 
"""
def Drms():
    drms = math.sqrt((sigma.sigma_x ** 2) + (sigma.sigma_y ** 2))
    with open('log/drms.txt', 'w') as f:
        f.write(str(drms))
        f.close() 
        
# CPE 
"""
This is the traditional CPE 
"""
def CEP():
    cpe = 0.59 * (sigma.sigma_x + sigma.sigma_y)
    with open('log/cpe.txt', 'w') as f:
        f.write(str(cpe))
        f.close() 

if __name__ == '__main__':
    sigma()
    twoDrmsG()
    twoDrms()
    Drms()
    CEP()
    successProba()