# Reval
Reval is an open-source framework to evaluate the performace of Robotics platforms. Currently it only supports [Husky platform](https://clearpathrobotics.com/husky-unmanned-ground-vehicle-robot/). The useres can evalute the performance of a mission for a given gazebo envirnoment (or on their own gazebo envirnment) for different configurations in an automated fashion and log the results. Reveal records the [rosbag](http://wiki.ros.org/rosbag) and evalutes all ros topics from the rosbag file. In addition, Reval supports the following metrics to evaluate the quality of mission:

**Evaluation metrics**
* number of failed produced path by DWA planner
* number of re-planning by DWA planner
* number of recovery behaviour executed 
* distance traveled
* mission time
* mission success: checks if the robot chead the goal

To define your custom configuration values: [Set Configuration](https://github.com/softsys4ai/Reval/tree/master/husky_ws/data_log)

To use can custom gazebo environment: [Use custom gazebo environment](https://github.com/softsys4ai/Reval/tree/master/husky_ws/data_log)

To change the gola location: [Update Goal location](https://github.com/softsys4ai/Reval/tree/master/husky_ws/data_log)

Reval supports both the [Husky simulator](https://www.clearpathrobotics.com/assets/guides/melodic/husky/SimulatingHusky.html) and Hysky physical robot. The instructions provided below are for Husky simulator. To run Reval on the physical Husky, first setup your husky using [Husky UGV Tutorial](https://www.clearpathrobotics.com/assets/guides/melodic/husky/BackUpHusky.html) then follow the below instructions.

## Requirements
* Ubuntu 18 or Ubuntu 20
* [ROS Melodic](http://wiki.ros.org/melodic/Installation/Ubuntu) or [ROS Noetic](http://wiki.ros.org/noetic/Installation/Ubuntu) 
* Python 2.7 (for ROS Melodic), Python 3.6+ (for ROS Noetic)
* [Pandas 1.4+](https://pypi.org/project/pandas/)

## Installations
### Installing the [husky simulator](https://www.clearpathrobotics.com/assets/guides/melodic/husky/SimulatingHusky.html)
For ROS Melodic
```sh
sudo apt-get install ros-melodic-husky-simulator
```

```sh
sudo apt-get install ros-melodic-husky-navigation
```

```sh
sudo apt-get install ros-melodic-husky-desktop
```


For ROS Noetic
```sh
sudo apt-get install ros-noetic-husky-simulator
```

```sh
sudo apt install ros-noetic-husky-navigation
```

```sh
sudo apt-get install ros-noetic-husky-desktop
```


### Installing [rosbag](http://wiki.ros.org/rosbag) for Python
#### Download and install [ros_readbag.py](http://wiki.ros.org/ROS/Tutorials/reading%20msgs%20from%20a%20bag%20file) using these commands:
Download the file
```sh
wget https://raw.githubusercontent.com/ElectricRCAircraftGuy/eRCaGuy_dotfiles/master/useful_scripts/ros_readbagfile.py
```
Make it executable
```sh
chmod +x ros_readbagfile.py
```
Ensure you have the ~/bin directory for personal binaries
```sh
mkdir -p ~/bin
```
Move this executable script into that directory as `ros_readbagfile`, so that it will be available as that command
```sh
mv ros_readbagfile.py ~/bin/ros_readbagfile
```
Create a symlink in `~/bin` to this script so you can run it from anywhere:
```sh
ln -si "${PWD}/ros_readbagfile.py" ~/bin/ros_readbagfile
```
If this is the first time ever creating the "~/bin" dir, then log out and log back in to your Ubuntu user account to cause Ubuntu to automatically add your ~/bin dir to your executable PATH.

Re-source your `~/.bahsrc` file
```sh
source ~/.bashrc
```

## Building Reval
Source your ROS setup.sh file
```sh
source /opt/ros/<ros distro>/setup.bash
```

Clone the repo 
```sh
git clone https://github.com/softsys4ai/Reval.git
```

Run `catkin build` on the `husky_ws` directory
```sh
cd Reval/husky_ws
```
```sh
catkin build
```
If everything is correct, you should see something similar to the following output

![catkin_build](https://user-images.githubusercontent.com/73362969/165857662-dd52c4d0-8a00-45f3-bdfc-1ceb9c9bde62.jpg)


## Running Reval
```sh
cd Reval/husky_ws
```
source your new `setup.sh` file. You need source this `setup.sh` file everytime you open a new Terminal
```sh
source devel/setup.bash
```
To evaluate the mission run
```sh
./run.sh
```
If you setup everything correctly, you should see the `Evaluation_results.csv` file on the `data_log` directory 

### Demo
<!--- https://user-images.githubusercontent.com/73362969/165874997-e870c4e2-95df-4af5-a5cd-c2d3f6d4935e.mp4 --->
![Reval_demo](https://user-images.githubusercontent.com/73362969/165876695-b7e5689d-415a-4e58-8208-3ba4116a1229.gif)






