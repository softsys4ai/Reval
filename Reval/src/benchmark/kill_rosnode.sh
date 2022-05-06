#!/bin/sh

rosnode kill /my_bag
rosnode kill /calculate_distance_traveled
killall -e roslaunch