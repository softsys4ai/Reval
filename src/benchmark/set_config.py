import dynamic_reconfigure.client
import rospy
import random
import pandas as pd
from param_nodes import move_base_global_costmap_inflation, move_base_global_costmap, move_base_global_costmap_obstacles
from param_nodes import move_base_local_costmap_inflation, move_base_local_costmap, move_base_local_costmap_obstacles
from param_nodes import move_base_DWAPlanner

rospy.init_node('huskyconfig_py', anonymous=True)

#----------------Dynamic reconfigure-----------------

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


## Exp2
# cost_scaling_factor_g = random.randint(21,40) # A scaling factor to apply to cost values during inflation
# update_frequency_g = random.randint(8,15)  # The frequency in Hz for the map to be updated.
# publish_frequency_g = random.randint(5,9) # The frequency in Hz for the map to be publish display information.
# transform_tolerance_g = round(random.uniform(2, 3.2),2) # Specifies the delay in transform (tf) data that is tolerable in seconds.  For example, a transform being 0.2 seconds out-of-date may be tolerable, but a transform being 8 seconds out of date is not.
# footprint_padding_g = round(random.uniform(0.06, 0.1),2) # Amount to pad footprint (m).
# combination_method_g = random.randint(0,1) # # Changes the behaviour how the obstacle_layer handles incoming data from layers beyond it. Possible values are "Overwrite" (0), "Maximum" (1) and "Nothing" (99).

# cost_scaling_factor_l = random.randint(21,40) 
# inflation_radius_l = random.randint(11,20)
# update_frequency_l = random.randint(8, 15)
# publish_frequency_l = random.randint(5, 9)
# transform_tolerance_l = round(random.uniform(2, 3.2),2)
# footprint_padding_l = round(random.uniform(0.06, 0.1),2)
# combination_method_l = random.randint(0,1)

# path_distance_bias = round(random.uniform(1, 2.1),2)
# goal_distance_bias = round(random.uniform(1.6, 2.5),2) # The weighting for how much the controller should attempt to avoid obstacles
# occdist_scale = round(random.uniform(0.06, 1),2) # The weighting for how much the controller should stay close to the path it was given
# stop_time_buffer = round(random.uniform(0.4, 0.7),2) # The amount of time that the robot must stop before a collision in order for a trajectory to be considered valid in seconds
# yaw_goal_tolerance = round(random.uniform(0.4, 0.7),2) # The tolerance in radians for the controller in yaw/rotation when achieving its goal
# xy_goal_tolerance = round(random.uniform(0.5, 0.8),2) # The tolerance in meters for the controller in the x & y distance when achieving a goal
# min_vel_x = round(random.uniform(-0.5, 0),2) # The minimum x velocity for the robot in m/s, negative for backwards motion.


### Default values
# cost_scaling_factor_g = 10.0 # A scaling factor to apply to cost values during inflation
# update_frequency_g = 4.0  # The frequency in Hz for the map to be updated.
# publish_frequency_g = 3.0 # The frequency in Hz for the map to be publish display information.
# transform_tolerance_g = 0.5 # Specifies the delay in transform (tf) data that is tolerable in seconds.  For example, a transform being 0.2 seconds out-of-date may be tolerable, but a transform being 8 seconds out of date is not.
# footprint_padding_g = 0.01 # Amount to pad footprint (m).
# combination_method_g = 1 # # Changes the behaviour how the obstacle_layer handles incoming data from layers beyond it. Possible values are "Overwrite" (0), "Maximum" (1) and "Nothing" (99).

# cost_scaling_factor_l = 10
# inflation_radius_l = 1.0
# update_frequency_l = 4
# publish_frequency_l = 3.0
# transform_tolerance_l = 0.5
# footprint_padding_l = 0.01
# combination_method_l = 1

# path_distance_bias = 0.6
# goal_distance_bias = 0.05 # The weighting for how much the controller should attempt to avoid obstacles
# occdist_scale = 0.125 # The weighting for how much the controller should stay close to the path it was given
# stop_time_buffer = 0.2 # The amount of time that the robot must stop before a collision in order for a trajectory to be considered valid in seconds
# yaw_goal_tolerance = 0.1 # The tolerance in radians for the controller in yaw/rotation when achieving its goal
# xy_goal_tolerance = 0.2 # The tolerance in meters for the controller in the x & y distance when achieving a goal
# min_vel_x = 0 # The minimum x velocity for the robot in m/s, negative for backwards motion.





#----------------DO NOT CHANGE--------------------

df = pd.DataFrame({"cost_scaling_factor_g":[cost_scaling_factor_g],
                "update_frequency_g":[update_frequency_g],"publish_frequency_g":[publish_frequency_g],
                "transform_tolerance_g":[transform_tolerance_g], "footprint_padding_g":[footprint_padding_g],
                "combination_method_g":[combination_method_g], 
                "inflation_radius_l":[inflation_radius_l],"update_frequency_l":[update_frequency_l],
                "publish_frequency_l":[publish_frequency_l],"combination_method_l":[combination_method_l],
                "cost_scaling_factor_l":[cost_scaling_factor_l],"transform_tolerance_l":[transform_tolerance_l],"footprint_padding_l":[footprint_padding_l],
                "path_distance_bias":[path_distance_bias],"goal_distance_bias":[goal_distance_bias],"stop_time_buffer":[stop_time_buffer],
                "occdist_scale":[occdist_scale],"yaw_goal_tolerance":[yaw_goal_tolerance],"xy_goal_tolerance":[xy_goal_tolerance],
                "min_vel_x":min_vel_x})
df.to_csv("log/configs.csv", index=False)     


mb_global_costmap_inf_params = {'cost_scaling_factor':cost_scaling_factor_g}
mb_global_costmap_params = {'update_frequency':update_frequency_g,'publish_frequency':publish_frequency_g,
                        'transform_tolerance':transform_tolerance_g,'footprint_padding':footprint_padding_g}
mb_global_costmap_obs_params = {'combination_method':combination_method_g}


mb_local_costmap_inf_params = {'inflation_radius':inflation_radius_l,'cost_scaling_factor':cost_scaling_factor_l}
mb_local_costmap_params = {'update_frequency':update_frequency_l,'publish_frequency':publish_frequency_l,'transform_tolerance':transform_tolerance_l,
                            'footprint_padding':footprint_padding_l}
mb_local_costmap_obs_params = {'combination_method':combination_method_l}

mb_DWAPlanner_params = {'path_distance_bias':path_distance_bias,'goal_distance_bias':goal_distance_bias,
                        'occdist_scale':occdist_scale,'stop_time_buffer':stop_time_buffer,'yaw_goal_tolerance':yaw_goal_tolerance,
                        'xy_goal_tolerance':xy_goal_tolerance,'min_vel_x':min_vel_x}



# print("move_base_global_inflation: " + str(mb_global_costmap_inf_params))
# print("move_base_global: " + str(mb_global_costmap_params))
# print("move_base_global_obstacles: " + str(mb_global_costmap_obs_params))


# print("move_base_local_inflation: " + str(mb_local_costmap_inf_params))
# print("move_base_local: " + str(mb_local_costmap_params))
# print("move_base_local_obstacles: " + str(mb_local_costmap_obs_params))

# print("move_base DWAPlanner: " + str(mb_DWAPlanner_params))
# print("--------------------")




config = move_base_global_costmap_inflation.update_configuration(mb_global_costmap_inf_params)
config = move_base_global_costmap.update_configuration(mb_global_costmap_params)
config = move_base_global_costmap_obstacles.update_configuration(mb_global_costmap_obs_params)

config = move_base_local_costmap_inflation.update_configuration(mb_local_costmap_inf_params) 
config = move_base_local_costmap.update_configuration(mb_local_costmap_params)
config = move_base_local_costmap_obstacles.update_configuration(mb_local_costmap_obs_params)

config = move_base_DWAPlanner.update_configuration(mb_DWAPlanner_params)

