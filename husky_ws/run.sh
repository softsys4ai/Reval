#!/bin/sh

# launch husky
# start rosbag
# start measure distance
# provide goal
# start eval.sh
# start evaultion_results.py
# close
# wait for closing

#various color codes
color_lblue='\033[1;34m'
color_red='\033[1;31m'
color_lgreen='\033[1;32m'
color_custom='\033[1;33;44m'
color_no='\033[0m'
printf "${color_lgreen}"
cat << "EOF"
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
--------------v1.0-------------------
EOF
printf "${color_no}"

echo "Launching husky"
echo "--------------------"

cd data_log/

python launch_husky.py

echo "Randomly setting configuration values"
echo "--------------------"
sleep 10

python set_config.py

echo "Starting rosbag and calculate distance"
echo "--------------------"
sleep 5
 
gnome-terminal -- ./ros_record.sh
gnome-terminal -- python calculate_distance_traveled.py

echo "2D Nav goal given"
echo "--------------------"
sleep 5

python goal.py

echo "Finishing simulation..."
sleep 10
echo "Simulation finished!"
echo "--------------------"
echo "Killing rosnodes and roslaunch"
echo "--------------------"

rosnode kill /my_bag
rosnode kill /calculate_distance_traveled
killall -e roslaunch

echo "Generating logs from rosbag file"
echo "--------------------"
sleep 5

./eval.sh

echo "Evaluating the rosbag logs"
echo "--------------------"
sleep 3


python evaluation_results.py
echo "********************"

echo "Everything done!"


