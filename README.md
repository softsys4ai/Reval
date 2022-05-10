![visitor badge](https://visitor-badge.glitch.me/badge?page_id=abirhossen786.486687358-badge)

# Reval
Reval is an open-source framework to evaluate the performance of Robotics platforms. Currently it only supports [Husky platform](https://clearpathrobotics.com/husky-unmanned-ground-vehicle-robot/). The useres can evalute the performance of a mission for a given gazebo envirnoment (or on their own gazebo envirnment) for different configurations in an automated fashion and log the results. Reveal records the [rosbag](http://wiki.ros.org/rosbag) and evalutes all ros topics from the rosbag file. In addition, Reval supports the following metrics to evaluate the quality of a mission:

**Evaluation metrics**
Metrics         |    Description    |
-----------     | ------------------|
DWA F           | # of failed produced path by DWA planner
DWA NP          | # of re-planning by DWA planner
DWA IT          | # of DWA invalid trajectory
RR              | # of rotate recovery excuted
RCU             | # of ClearCostMaps recovery executed for unstuck robot 
RCL             | # of ClearCostMaps layer recovery executed
IRC             | # of invalid rotation cmd
ERG             | # of error rotating on the goal
DRMS            | The square root of the average of the squared horizontal position errors, <img src="https://latex.codecogs.com/png.image?\inline&space;\small&space;\dpi{110}\bg{white}DRMS=\sqrt{\sigma_x^2&plus;\sigma_y^2}" title="https://latex.codecogs.com/png.image?\inline \small \dpi{110}\bg{white}DRMS=\sqrt{\sigma_x^2&plus;\sigma_y^2}" /> ;   where standard deviation of the delta x and y,  <img src="https://latex.codecogs.com/png.image?\inline&space;\small&space;\dpi{120}\bg{white}\sigma&space;=&space;\sqrt{\frac{1}{N}\sum_{i=1}^N(x_i-\mu)^2}" title="https://latex.codecogs.com/png.image?\inline \small \dpi{120}\bg{white}\sigma = \sqrt{\frac{1}{N}\sum_{i=1}^N(x_i-\mu)^2}" />. Probability of 65%
2DRMS           | Twice the Distance Root Mean Squared (DRMS) of the horizontal position error, <img src="https://latex.codecogs.com/png.image?\inline&space;\small&space;\dpi{120}\bg{white}2DRMS=2\sqrt{\sigma_x^2&plus;\sigma_y^2}" title="https://latex.codecogs.com/png.image?\inline \small \dpi{120}\bg{white}2DRMS=2\sqrt{\sigma_x^2&plus;\sigma_y^2}" />. Probability of 95%
CPE             | The radius of circle centered at the true position, containing the position estimate with probability of 50%. <img src="https://latex.codecogs.com/png.image?\inline&space;\small&space;\dpi{120}\bg{white}CEP=0.59(\sigma_x&plus;\sigma_y)" title="https://latex.codecogs.com/png.image?\inline \small \dpi{120}\bg{white}CEP=0.59(\sigma_x+\sigma_y)" />
RNS             | robustness in narrow spaces, <img src="https://latex.codecogs.com/png.image?\inline&space;\small&space;\dpi{120}\bg{white}RNS=\frac{1}{N_{s}}\sum_{i=0}^{N_{s}}&space;(passed_{Ns})" title="https://latex.codecogs.com/png.image?\inline \small \dpi{120}\bg{white}RNS=\frac{1}{N_{s}}\sum_{i=0}^{N_{s}}&space;(passed_{Ns})" /> ; where Ns is the total narrow spaces in the gazebo environment, and passed_Ns is the narrow spaces that the robot successfully crossed.
DT             | total distance traveled during a mission
BP             | battery percentage. For more details: [Gazebo-ROS battery plugin](src/husky_ws/src/gazebo_ros_battery/#gazebo-ros-battery-plugin)
Col            | number of collisions in a mission
MT             | time taken to complete a mission
MS             | mission success. Example: if the robot successfully reached point A to B


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
examaple: `python reval.py -v false -e 10` 

### Demo

<p align="center">
  <img src= "https://user-images.githubusercontent.com/73362969/167279446-c1727093-1c2f-4f3f-92a2-40ecee5de599.png"
</p>

Reval in action:
  
https://user-images.githubusercontent.com/73362969/167276835-6f514a3a-c7ce-45b9-b9fd-ad6223582792.mp4

## Customizations
- To define your custom configuration options: [Set Configuration](/src/benchmark/README.md#cahnging-configuration-options)
- To use your own custom gazebo environment: [Use custom gazebo environment](/src/benchmark/README.md#custom-gazebo-environment)
- To change the goal locations: [Update Goal location](/src/benchmark/README.md#define-mission-specifications)


## Contacts
Please feel free to contact via email if you have any feedbacks. Thank you for using Reval!
|Name|Email|     
|---------------|------------------|      
|Md Abir Hossen|mhossen@email.sc.edu|          
|Pooyan Jamshidi|pjamshid@cse.sc.edu|  
