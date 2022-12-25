import os
import shutil
import signal
import subprocess
import time
from turtle import bgcolor
from tqdm import tqdm
from utils.utils import bcolors, Loader, description, KeyboardInterrupt


if not os.path.exists('src/benchmark/log'):
    os.makedirs('src/benchmark/log')

color = 'white'
ASCII = '.#'

def reval():
    global loading
    loading = False
    set_config = subprocess.check_call("python set_config.py '%s'", cwd="src/benchmark/", shell=True)
    for i in tqdm(range(5),  desc="Set config method=random", colour=color, ascii=ASCII, bar_format='{l_bar}{bar:20}{r_bar}{bar:-20b}', leave=False): 
        time.sleep(1)

    rosbag = subprocess.check_call("gnome-terminal -- ./ros_record.sh '%s'", cwd="src/benchmark/service", shell=True)
    calculate_distance = subprocess.check_call("gnome-terminal -- python calculate_distance_traveled.py '%s'", cwd="src/benchmark", shell=True)
    for i in tqdm(range(5),  desc="Data logger", colour=color, ascii=ASCII, bar_format='{l_bar}{bar:20}{r_bar}{bar:-20b}', leave=False): 
        time.sleep(1)
    print("")
    reval.loader = Loader("Mission in progress...", bcolors.CGREEN + "" + bcolors.ENDC, 0.05).start()
    loading = True
    nav2d_goal = subprocess.check_call("python mission.py '%s'", cwd="src/benchmark/", shell=True)
    reval.loader.stop() 
    loading = False
    print(bcolors.CGREEN + "Mission Done!" + bcolors.ENDC)
    for i in tqdm(range(10),  desc="Finishing simulation", colour=color, ascii=ASCII, bar_format='{l_bar}{bar:20}{r_bar}{bar:-20b}', leave=False):
        time.sleep(1)

    kill_rosnode = subprocess.check_call("./kill_rosnode.sh &>/dev/null", cwd="src/benchmark/service", shell=True)

    for i in tqdm(range(5),  desc="Generating logs", colour=color, ascii=ASCII, bar_format='{l_bar}{bar:20}{r_bar}{bar:-20b}', leave=False):
        time.sleep(1)

    reval.loader = Loader("Evaluating logs...", bcolors.HEADER + "" + bcolors.ENDC, 0.05).start()
    loading = True    
    eval = subprocess.check_call("./eval.sh '%s'", cwd="src/benchmark/service", shell=True)
    reval.loader.stop()
    loading = False  
    positinal_metrics = subprocess.check_call("python positional_error.py '%s'", cwd="src/benchmark/", shell=True)
    evaluation_results = subprocess.check_call("python evaluation_results.py '%s'", cwd="src/benchmark/", shell=True)  

    # path = "src/benchmark/log"
    # if os.path.isdir(path):
    #     shutil.rmtree(path)



if __name__== '__main__':
    try:
        signal.signal(signal.SIGINT, KeyboardInterrupt.signal_handler)
        cursor_off = subprocess.check_call("tput civis", shell=True)

        turtlebot_nav = subprocess.check_call("./turtlebot3_nav.sh '%s'", cwd="src/benchmark/service", shell=True)
        for i in tqdm(range(3),  desc="Launching Turtlebot3 navigation", colour=color, ascii=ASCII, bar_format='{l_bar}{bar:20}{r_bar}{bar:-20b}', leave=False): 
            time.sleep(1)                  
        reval()
        cursor_on = subprocess.check_call("tput cvvis", shell=True)


    except:
        if loading == True:
            reval.loader.stop()    
        print(bcolors.WARNING + "Killing rosnodes and roslaunch" + bcolors.ENDC)
        kill_rosnode = subprocess.check_call("./kill_rosnode.sh '%s'", cwd="src/benchmark/service", shell=True)        
        for i in tqdm(range(5),  desc="Closing everything", colour=color, ascii=ASCII, bar_format='{l_bar}{bar:20}{r_bar}{bar:-20b}'):
            time.sleep(1)
        print(bcolors.FAIL + "Mission Failed!" + bcolors.ENDC)    
        cursor_on = subprocess.check_call("tput cvvis", shell=True)  
