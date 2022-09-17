import os
import rospy
import subprocess
from tqdm import tqdm
import time
from utils.utils import bcolors, Loader, description, KeyboardInterrupt
from sensor_msgs.msg import BatteryState

battey_status_sub = '/battery/status'
color = 'white'
ASCII = '.#'

def callback(msg):
    bp = msg.percentage
    print("Battery: ", bp, "%")
    print("")
    print("Mission will stop if battery is less than 10%.")

    if bp < 98 and os.path.isfile('src/benchmark/log/x_samples.ob'):
        kill_rosnode = subprocess.check_call("./kill_rosnode.sh &>/dev/null", cwd="src/benchmark/service", shell=True)
        for i in tqdm(range(5),  desc="Generating logs", colour=color, ascii=ASCII, bar_format='{l_bar}{bar:20}{r_bar}{bar:-20b}', leave=False):
            time.sleep(1)        
        loader = Loader("Evaluating logs...", bcolors.HEADER + "" + bcolors.ENDC, 0.05).start()
        eval = subprocess.check_call("./eval.sh '%s'", cwd="src/benchmark/service", shell=True)
        loader.stop()
        positinal_metrics = subprocess.check_call("python positional_error.py '%s'", cwd="src/benchmark/", shell=True)
        evaluation_results = subprocess.check_call("python evaluation_results.py '%s'", cwd="src/benchmark/", shell=True)  
        kill_check_battery = subprocess.check_call("gnome-terminal -- ./kill_check_battery.sh &>/dev/null", cwd="src/benchmark/service", shell=True)

rospy.init_node('check_battery')
rospy.Subscriber(battey_status_sub, BatteryState, callback)
rospy.spin()