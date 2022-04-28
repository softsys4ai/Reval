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
ln -si "${PWD}/ros_readbagfile.py" ~/bin/gs_ros_readbagfile
```
```sh
ln -si "${PWD}/ros_readbagfile.py" ~/bin/ros_readbagfile
```
If this is the first time ever creating the "~/bin" dir, then log out and log back in to your Ubuntu user account to cause Ubuntu to automatically add your ~/bin dir to your executable PATH.

Re-source your `~/.bahsrc` file
```sh
source ~/.bashrc
```

Install python dependencies
```sh
pip install bagpy
```
For python3
```sh
pip3 install bagpy
```
if the above cmd ultimately fails due to permissions errors, use `sudo` to: `sudo pip3 install bagpy`

## Building Reval
Clone the repo 
```sh
git clone https://github.com/softsys4ai/Reval.git
```
Run `catkin build` on the root directory
```sh
cd husky_ws
```
```sh
catkin build
```
## Running Reval
source your new `setup.sh` file. You need source this `setup.sh` file everytime you open a new Terminal
```sh
source devel/setup.bash
```
To evaluate the mission run
```sh
./run.sh
```
If you setup everything correctly, you should see the `Evaluation_results.csv` file on the `data_log` directory 
