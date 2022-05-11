import os
import subprocess
import time
import argparse
from tqdm import tqdm

log = subprocess.check_call("mkdir -p log", cwd="src/benchmark/", shell=True)
cursor_off = subprocess.check_call("tput civis", shell=True)

color = 'white'
ASCII = '.#'

parser = argparse.ArgumentParser(description='Reval is an open-source framework to evaluate the performace of Robotics platforms. Currently it only supports Husky platform. The useres can evalute the performance of a mission for a given gazebo envirnoment (or on their own gazebo envirnment) for different configurations in an automated fashion and log the results. Reveal records the rosbag and evalutes all ros topics from the rosbag file.',
                                formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('-v', '-viz', help='Turn on/off visualization of gazebo and rviz', default='On', metavar='')
parser.add_argument('-e', '-epoch', help='Number of data-points to be recorded', type=int, default=1, metavar='')
args = parser.parse_args()

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    CGREEN  = '\33[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

print(bcolors.CGREEN + r"""
  _____                 _        
 |  __ \               | |       
 | |__) |_____   ____ _| |       
 |  _  // _ \ \ / / _` | |       
 | | \ \  __/\ V / (_| | |       
 |_|  \_\___| \_/ \__,_|_|       
              _  _____           
        /\   (_)/ ____|          
       /  \   _| (___  _   _ ___ 
      / /\ \ | |\___ \| | | / __|
     / ____ \| |____) | |_| \__ \
    /_/    \_\_|_____/ \__, |___/
                        __/ |    
                       |___/     
--------------v1.1-------------------

""" + bcolors.ENDC)

 
for i in tqdm(range(args.e), colour="green", desc="Epoch", bar_format='{l_bar}{bar:20}{r_bar}{bar:-20b}'):

    if args.v == 'On' or args.v == 'on':
 
        husky_gazebo = subprocess.check_call("./husky_gazebo.sh '%s'", cwd="src/benchmark/", shell=True)
        for i in tqdm(range(8), desc="Launching husky_gazebo", colour=color, ascii=ASCII, bar_format='{l_bar}{bar:20}{r_bar}{bar:-20b}'):
            time.sleep(1)
        
        husky_mb = subprocess.check_call("./husky_movebase.sh '%s'", cwd="src/benchmark/", shell=True)
        for i in tqdm(range(3),  desc="Launching husky_MobeBase", colour=color, ascii=ASCII, bar_format='{l_bar}{bar:20}{r_bar}{bar:-20b}'): 
            time.sleep(1)

        husky_rviz = subprocess.check_call("./husky_rviz.sh '%s'", cwd="src/benchmark/", shell=True)
        for i in tqdm(range(10),  desc="Launching husky_rviz", colour=color, ascii=ASCII, bar_format='{l_bar}{bar:20}{r_bar}{bar:-20b}'): 
            time.sleep(1)

        battery_collision = subprocess.check_call("./husky_battery_bumper.sh '%s'", cwd="src/benchmark/", shell=True)
        set_config = subprocess.check_call("python set_config.py '%s'", cwd="src/benchmark/", shell=True)
        for i in tqdm(range(5),  desc="Set config method=random", colour=color, ascii=ASCII, bar_format='{l_bar}{bar:20}{r_bar}{bar:-20b}'): 
            time.sleep(1)

    
        rosbag = subprocess.check_call("gnome-terminal -- ./ros_record.sh '%s'", cwd="src/benchmark/", shell=True)
        calculate_distance = subprocess.check_call("gnome-terminal -- python calculate_distance_traveled.py '%s'", cwd="src/benchmark/", shell=True)
        for i in tqdm(range(5),  desc="Data logger", colour=color, ascii=ASCII, bar_format='{l_bar}{bar:20}{r_bar}{bar:-20b}'): 
            time.sleep(1)
        print("")

        nav2d_goal = subprocess.check_call("python mission.py '%s'", cwd="src/benchmark/", shell=True)
        for i in tqdm(range(10),  desc="Finishing simulation", colour=color, ascii=ASCII, bar_format='{l_bar}{bar:20}{r_bar}{bar:-20b}'):
            time.sleep(1)

  
        print("Simulation finished!")
        print("--------------------")
        print(bcolors.WARNING + "Killing rosnodes and roslaunch" + bcolors.ENDC)

        kill_rosnode = subprocess.check_call("./kill_rosnode.sh '%s'", cwd="src/benchmark/", shell=True)

        for i in tqdm(range(5),  desc="Generating logs", colour=color, ascii=ASCII, bar_format='{l_bar}{bar:20}{r_bar}{bar:-20b}'):
            time.sleep(1)

        eval = subprocess.check_call("gnome-terminal -- ./eval.sh '%s'", cwd="src/benchmark/", shell=True)
        positinal_metrics = subprocess.check_call("python positional_error.py '%s'", cwd="src/benchmark/", shell=True)
        for i in tqdm(range(20),  desc="Evaluating logs", colour=color, ascii=ASCII, bar_format='{l_bar}{bar:20}{r_bar}{bar:-20b}'):
            time.sleep(1)
        
        print("")
 
        evaluation_results = subprocess.check_call("python evaluation_results.py '%s'", cwd="src/benchmark/", shell=True)
    


    if args.v == 'Off' or args.v == 'off':
        husky_gazebo = subprocess.check_call("./husky_gazebo_nogui.sh '%s'", cwd="src/benchmark/", shell=True)
        for i in tqdm(range(8), desc="Launching husky_gazebo", colour=color, ascii=ASCII, bar_format='{l_bar}{bar:20}{r_bar}{bar:-20b}'):
            time.sleep(1)
    
        husky_mb = subprocess.check_call("./husky_movebase.sh '%s'", cwd="src/benchmark/", shell=True)
        for i in tqdm(range(3),  desc="Launching husky_MoveBase", colour=color, ascii=ASCII, bar_format='{l_bar}{bar:20}{r_bar}{bar:-20b}'): 
            time.sleep(1)

        battery_collision = subprocess.check_call("./husky_battery_bumper.sh '%s'", cwd="src/benchmark/", shell=True)
        set_config = subprocess.check_call("python set_config.py '%s'", cwd="src/benchmark/", shell=True)
        for i in tqdm(range(5),  desc="Set config method=random", colour=color, ascii=ASCII, bar_format='{l_bar}{bar:20}{r_bar}{bar:-20b}'): 
            time.sleep(1)


        rosbag = subprocess.check_call("gnome-terminal -- ./ros_record.sh '%s'", cwd="src/benchmark/", shell=True)
        calculate_distance = subprocess.check_call("gnome-terminal -- python calculate_distance_traveled.py '%s'", cwd="src/benchmark/", shell=True)
        for i in tqdm(range(5),  desc="Data logger", colour=color, ascii=ASCII, bar_format='{l_bar}{bar:20}{r_bar}{bar:-20b}'): 
            time.sleep(1)
        print("")

        
        nav2d_goal = subprocess.check_call("python mission.py '%s'", cwd="src/benchmark/", shell=True)
        for i in tqdm(range(10),  desc="Finishing simulation", colour=color, ascii=ASCII, bar_format='{l_bar}{bar:20}{r_bar}{bar:-20b}'):
            time.sleep(1)

  
        print("Simulation finished!")
        print("--------------------")
        print(bcolors.WARNING + "Killing rosnodes and roslaunch" + bcolors.ENDC)

        kill_rosnode = subprocess.check_call("./kill_rosnode.sh '%s'", cwd="src/benchmark/", shell=True)

        for i in tqdm(range(5),  desc="Generating logs", colour=color, ascii=ASCII, bar_format='{l_bar}{bar:20}{r_bar}{bar:-20b}'):
            time.sleep(1)

        eval = subprocess.check_call("gnome-terminal -- ./eval.sh '%s'", cwd="src/benchmark/", shell=True)
        positinal_metrics = subprocess.check_call("python positional_error.py '%s'", cwd="src/benchmark/", shell=True)
        for i in tqdm(range(20),  desc="Evaluating logs", colour=color, ascii=ASCII, bar_format='{l_bar}{bar:20}{r_bar}{bar:-20b}'):
            time.sleep(1)
        
        print("")
        
        evaluation_results = subprocess.check_call("python evaluation_results.py '%s'", cwd="src/benchmark/", shell=True)

cursor_on = subprocess.check_call("tput cvvis", shell=True)
