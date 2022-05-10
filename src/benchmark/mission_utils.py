import subprocess

def GetCurrPose():
    subprocess.check_call("python current_pose.py '%s'", shell=True)

def PoseSamples():
    subprocess.check_call("python pose_samples.py '%s'", shell=True)  

def MissionTime():
    pass