#!/bin/sh

robag=$( rosnode kill /my_bag &>/dev/null )
caldis=$( rosnode kill /calculate_distance_traveled &>/dev/null)
all=$( killall -e roslaunch &>/dev/null)