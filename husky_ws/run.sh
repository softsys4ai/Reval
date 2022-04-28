#!/bin/sh

# launch husky
# start rosbag
# start measure distance
# provide goal
# start eval.sh
# start evaultion_results.py
# close
# wait for closing

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


