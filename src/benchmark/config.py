import os
import random
import pandas as pd

for i in range(100):
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
    

    
    # if not os.path.isfile('config.csv'):            
    #     df.to_csv("config.csv", mode='a', index=False, header=True) 
    # else:
    #     df.to_csv("config.csv", mode='a', index=False, header=False)   
df2 = pd.read_csv("config.csv")
bool_series = df2.duplicated()
with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
    print(bool_series)   