### Cahnging configuration values
Currently Reval supports the following configurations
```python
cost_scaling_factor_g = random.randint(1,20) # A scaling factor to apply to cost values during inflation
update_frequency_g = random.randint(4,7)  # The frequency in Hz for the map to be updated.
publish_frequency_g = random.randint(1,4) # The frequency in Hz for the map to be publish display information.
transform_tolerance_g = round(random.uniform(0.2, 2),2) # Specifies the delay in transform (tf) data that is tolerable in seconds.  For example, a transform being 0.2 seconds out-of-date may be tolerable, but a transform being 8 seconds out of date is not.
footprint_padding_g = round(random.uniform(0.01, 0.05),2) # Amount to pad footprint (m).
combination_method_g = random.randint(0,1) # # Changes the behaviour how the obstacle_layer handles incoming data from layers beyond it. Possible values are "Overwrite" (0), "Maximum" (1) and "Nothing" (99).

cost_scaling_factor_l = random.randint(1,20) 
inflation_radius_l = random.randint(1,10)
update_frequency_l = random.randint(4,7)
publish_frequency_l = random.randint(1,4)
transform_tolerance_l = round(random.uniform(0.2, 2),2)
footprint_padding_l = round(random.uniform(0.01, 0.05),2)
combination_method_l = random.randint(0,1)

path_distance_bias = round(random.uniform(0.1, 1),2)
goal_distance_bias = round(random.uniform(0.5, 1.5),2) # The weighting for how much the controller should attempt to avoid obstacles
occdist_scale = round(random.uniform(0.01, 0.05),2) # The weighting for how much the controller should stay close to the path it was given
stop_time_buffer = round(random.uniform(0.1, 0.3),2) # The amount of time that the robot must stop before a collision in order for a trajectory to be considered valid in seconds
yaw_goal_tolerance = round(random.uniform(0.1, 0.3),2) # The tolerance in radians for the controller in yaw/rotation when achieving its goal
xy_goal_tolerance = round(random.uniform(0.1, 0.4),2) # The tolerance in meters for the controller in the x & y distance when achieving a goal
min_vel_x = round(random.uniform(-0.3, 0),2) # The minimum x velocity for the robot in m/s, negative for backwards motion.
```
To chnage to configuration values, simply chnage the upper and lowerd bounds on the `set_config.py` file located at `husky_ws//data_log`. For example, to change the `cost_scaling_factor_g` value,
```python
cost_scaling_factor_g = random.randint(5,10)
```
To set a static value,
```python
cost_scaling_factor_g = 10
```

### To use your custom map
* Copy your gazebo world file (e.g., `my_map.world`) into `husky_ws/src/husky/hysky_gazebo/worlds`  
* Update the world file name on `playpen.launch` loacted at `husky_ws/src/husky/hysky_gazebo/launch` as follows:
```launch
<launch>
  <include file="$(find gazebo_ros)/launch/empty_world.launch">
  
    # update with your world file <your_file_name>.world
    <arg name="world_name" value="$(find husky_gazebo)/worlds/Scenario1.world"/> 
    
    # keep this as it is
    <arg name="paused" value="false"/>
    <arg name="use_sim_time" value="true"/>
    <arg name="gui" value="true"/>
    <arg name="headless" value="false"/>
    <arg name="debug" value="false"/>
  </include>
</launch>
```

### To change the Goal location
Update the coordinates with your goal location on the `goal.py` file located at `husky_ws/data_log`
```python
goal = MoveBaseGoal()
goal.target_pose.header.frame_id = 'odom' 

# Update the coordinates with your goal location
goal.target_pose.pose.position.x = 14.5426712036
goal.target_pose.pose.position.y = -0.691165924072
goal.target_pose.pose.orientation.z = -0.0198330671035
goal.target_pose.pose.orientation.w = 0.99980330538
```

