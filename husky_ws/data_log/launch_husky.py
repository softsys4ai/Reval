import subprocess
import time 

husky_gazebo = subprocess.check_call("./husky_gazebo.sh '%s'", shell=True)
time.sleep(8)
husky_mb = subprocess.check_call("./husky_movebase.sh '%s'", shell=True)
time.sleep(3)
husky_rviz = subprocess.check_call("./husky_rviz.sh '%s'", shell=True)