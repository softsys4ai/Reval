## Install the husky simulator
`sudo apt install ros-melodic-husky-simulator` \
`sudo apt install ros-melodic-husky-navigation` \
`sudo apt-get install ros-melodic-husky-desktop`
* For Noetic run \
`sudo apt-get install ros-noetic-husky-desktop` \
`sudo apt-get install ros-noetic-husky-simulator` \
`sudo apt install ros-noetic-husky-navigation`

# Step 1:
* Create a folder `mkdir ~/husky_ws`
* `cd /husky_ws` Clone the repo `git clone https://github.com/softsys4ai/AdaptConfig_robotics.git`
* Run `catkin build` on the root directory
* Change the values for following configurations randomly on the `costmap_common.yaml` file located at `cd /husky_ws/src/husky/husky_navigation/config`. 
```yaml
update_frequency:
publish_frequency:
transform_tolerance:
resolution:
obstacle_range:
raytrace_range:
inflation_radius:
```
*  Change the values for following configurations randomly on the `planner.yaml` file located at `cd /husky_ws/src/husky/husky_navigation/config`. 
```yaml
# Goal Tolerance Parameters
yaw_goal_tolerance: 
xy_goal_tolerance:
sim_time: 
sim_granularity:
heading_lookahead:   
pdist_scale:
gdist_scale:
heading_scoring_timestep:
```

# Step 2:
## Running the simulator

Make sure to source the each terminal before running the commands using `source /devel/setup.bashrc` on the root directory (husky_ws).

* Terminal 1: 
> `roslaunch husky_gazebo husky_playpen.launch`
* Terminal 2:
> `roslaunch husky_viz view_robot.launch`
* Ternimal 3:
> `roslaunch husky_navigation move_base_mapless_demo.launch`

## Logging the results
* Install [ros_readbagfile](http://wiki.ros.org/ROS/Tutorials/reading%20msgs%20from%20a%20bag%20file)
```
# Download the file
wget https://raw.githubusercontent.com/ElectricRCAircraftGuy/eRCaGuy_dotfiles/master/useful_scripts/ros_readbagfile.py
# Make it executable
chmod +x ros_readbagfile.py
# Ensure you have the ~/bin directory for personal binaries
mkdir -p ~/bin
# Move this executable script into that directory as `ros_readbagfile`, so that it will
# be available as that command
mv ros_readbagfile.py ~/bin/ros_readbagfile
# Re-source your ~/.bashrc file to ensure ~/bin is in your PATH, so you can use this
# new `ros_readbagfile` command you just installed
. ~/.bashrc
#
# Install python dependencies (see the comments at the top of the ros_readbagfile.py 
# file for the latest dependencies and instructions)
pip install bagpy
pip3 install bagpy
```
* Navigate to `cd husky_ws/data_log`
* Terminal 4: Starting the rosbag
> `./ros_record.sh`
* Teminal 5: measuring the traveled distance
> `python calculate_distance_traveled.py`


# Step 3:
* Once everything is up and running, give a 2D navigation goal on the rviz. Make sure to start a timer to recorde the mission time. At this point the husky should start moving and you should see traveled distance values on Terminal 5. 
* If the robot reach the goal terminate all the terminals using `ctrl+c`. You should have a rosbag file on the data_log folder. 
* If the robot does not reach the goal or get stuck wait for `Aborting because a valid control could not be found. Even after executing all recovery behaviors` this messege on Terminal 3 then stop the timer and ternimate all the terminal using `ctrl+c`
* Checking the number of collision per mission is by observation, if the husky hits any obstcle you can visualize it on the gazebo screen.

# Step 4:
* `cd /husky_ws/data_log` run `./eval.sh` on terminal. It will generate the topics.yaml and all the messge text files on the data_log folder.
* `cd /husky_ws/data_log` run `python evaluation_resultsl.py` on terminal. It will print all the evaluation metrics.
* Log the data [here](https://docs.google.com/spreadsheets/d/1z7JyRzxkC3PpUkAlv72hyn8fvZ6lhPCaiiUfCrJXOZU/edit?usp=sharing)
