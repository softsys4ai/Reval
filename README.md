![visitor badge](https://visitor-badge.glitch.me/badge?page_id=abirhossen786.486687358-badge)

# Reval
Reval is an open-source framework to evaluate the performace of Robotics platforms. Currently it only supports [Husky platform](https://clearpathrobotics.com/husky-unmanned-ground-vehicle-robot/). The useres can evalute the performance of a mission for a given gazebo envirnoment (or on their own gazebo envirnment) for different configurations in an automated fashion and log the results. Reveal records the [rosbag](http://wiki.ros.org/rosbag) and evalutes all ros topics from the rosbag file. In addition, Reval supports the following metrics to evaluate the quality of mission:

**Evaluation metrics**
* number of failed produced path by DWA planner
* number of re-planning by DWA planner
* number of recovery behaviour executed 
* distance traveled
* mission time
* mission success: checks if the robot chead the goal

To define your custom configuration values: [Set Configuration](/husky_ws/data_log/README.md#cahnging-configuration-values)

To use can custom gazebo environment: [Use custom gazebo environment](/husky_ws/data_log/README.md#to-use-your-custom-map)

To change the gola location: [Update Goal location](/husky_ws/data_log/README.md#to-change-the-goal-location)

Reval supports both the [Husky simulator](https://www.clearpathrobotics.com/assets/guides/melodic/husky/SimulatingHusky.html) and Hysky physical robot. The instructions provided below are for Husky simulator. To run Reval on the physical Husky, first setup your husky using [Husky UGV Tutorial](https://www.clearpathrobotics.com/assets/guides/melodic/husky/BackUpHusky.html) then follow the below instructions.

## Build status
Build Type      |    Status     |
-----------     | --------------|
ROS melodic     | [![ROS melodic](https://img.shields.io/badge/ROS_meoldic-failing-FF0000)](http://wiki.ros.org/melodic/Installation/Ubuntu)
ROS noetic      | [![ROS noetic](https://img.shields.io/badge/ROS_noetic-passing-success)](http://wiki.ros.org/noetic/Installation/Ubuntu)

Platform        |    Status     |
-----------     | --------------|
Husky UGV     | [![Husky UGV](https://img.shields.io/badge/Husky_UGV-passing-success)](https://www.clearpathrobotics.com/assets/guides/noetic/husky/SimulatingHusky.html)
TurtleBot3      | [![TurtleBot3](https://img.shields.io/badge/TurtleBot3-coming_soon-ff69b4)](https://emanual.robotis.com/docs/en/platform/turtlebot3/quick-start/)
OceanWATERS     | [![OW](https://img.shields.io/badge/OceanWATERS-coming_soon-ff69b4)](https://github.com/nasa/ow_simulator)



## Requirements
* Ubuntu 18 or Ubuntu 20
* [ROS Melodic](http://wiki.ros.org/melodic/Installation/Ubuntu) or [ROS Noetic](http://wiki.ros.org/noetic/Installation/Ubuntu) 
* Python 2.7 (for ROS Melodic), Python 3.6+ (for ROS Noetic)

## Installations
### Installing the [husky simulator](https://www.clearpathrobotics.com/assets/guides/melodic/husky/SimulatingHusky.html)
For ROS Melodic
```sh
sudo apt-get install ros-melodic-husky-simulator
sudo apt-get install ros-melodic-husky-navigation
sudo apt-get install ros-melodic-husky-desktop
```

For ROS Noetic
```sh
sudo apt-get install ros-noetic-husky-simulator
sudo apt-get install ros-noetic-husky-navigation
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
## Install dependencies
Clone the repo
```sh
git clone https://github.com/softsys4ai/Reval.git
```
Installing the dependencies
```sh
sudo apt install ripgrep
pip install pandas
pip install tqdm
pip install tabulate 
```
Or `cd Reval/` run `./requirements.sh`. If you face permission denied, first run `chmod +x requirements.sh` 

## Building Reval
Source your ROS setup.sh file
```sh
source /opt/ros/<ros distro>/setup.bash
```

Run `catkin build` on the `Reval root` directory
```sh
cd Reval/
```
```sh
catkin build
```
N.b. If you face `Catkin command not found`, install `sudo apt-get install python3-catkin-tools` OR you can use `catkin_make`

If everything is correct, you should see something similar to the following output

![catkin_build](https://user-images.githubusercontent.com/73362969/165857662-dd52c4d0-8a00-45f3-bdfc-1ceb9c9bde62.jpg)


## Running Reval
```sh
cd Reval/
```
source your new `setup.sh` file. You need source this `setup.sh` file everytime you open a new Terminal
```sh
source devel/setup.bash
```
To evaluate the mission run
```sh
python reval.py
```

```
optional arguments:
  -h, --help    show this help message and exit
  -v , -viz     turn on/off visualization of gazebo and rviz (default: True)
  -e , -epoch   number of data-points to be recorded (default: 1)
```
examaple: `python reval.py -v false -d 10` 

### Demo
https://user-images.githubusercontent.com/73362969/165874997-e870c4e2-95df-4af5-a5cd-c2d3f6d4935e.mp4

## Contacts
Please feel free to contact via email if you have any feedbacks. Thank you for using Reval!
|Name|Email|     
|---------------|------------------|      
|Md Abir Hossen|mhossen@email.sc.edu|          
|Pooyan Jamshidi|pjamshid@cse.sc.edu|  





