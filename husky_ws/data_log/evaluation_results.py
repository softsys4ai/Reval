import pandas as pd
import datetime
import os


# Reading configs
df_config = pd.read_csv('configs.csv')
cost_scaling_factor_g = df_config['cost_scaling_factor_g']
update_frequency_g = df_config['update_frequency_g']
publish_frequency_g = df_config['publish_frequency_g']
transform_tolerance_g = df_config['transform_tolerance_g']
footprint_padding_g = df_config['footprint_padding_g']
combination_method_g = df_config['combination_method_g']

cost_scaling_factor_l = df_config['cost_scaling_factor_l']
inflation_radius_l = df_config['inflation_radius_l']
update_frequency_l = df_config['update_frequency_l']
publish_frequency_l = df_config['publish_frequency_l']
combination_method_l = df_config['combination_method_l']
transform_tolerance_l = df_config['transform_tolerance_l']
footprint_padding_l = df_config['footprint_padding_l']

path_distance_bias = df_config['path_distance_bias']
goal_distance_bias = df_config['goal_distance_bias']
occdist_scale = df_config['occdist_scale']
stop_time_buffer = df_config['stop_time_buffer']
yaw_goal_tolerance = df_config['yaw_goal_tolerance']
xy_goal_tolerance = df_config['xy_goal_tolerance']
min_vel_x = df_config['min_vel_x']


cost_scaling_factor_g = cost_scaling_factor_g.to_string(index=False)
update_frequency_g = update_frequency_g.to_string(index=False)
publish_frequency_g = publish_frequency_g.to_string(index=False)
transform_tolerance_g = transform_tolerance_g.to_string(index=False)
footprint_padding_g = footprint_padding_g.to_string(index=False)
combination_method_g = combination_method_g.to_string(index=False)

inflation_radius_l = inflation_radius_l.to_string(index=False)
update_frequency_l = update_frequency_l.to_string(index=False)
publish_frequency_l = publish_frequency_l.to_string(index=False)
cost_scaling_factor_l = cost_scaling_factor_l.to_string(index=False)
combination_method_l = combination_method_l.to_string(index=False)
transform_tolerance_l = transform_tolerance_l.to_string(index=False)
footprint_padding_l = footprint_padding_l.to_string(index=False)

path_distance_bias = path_distance_bias.to_string(index=False)
goal_distance_bias = goal_distance_bias.to_string(index=False)
occdist_scale = occdist_scale.to_string(index=False)
stop_time_buffer = stop_time_buffer.to_string(index=False)
yaw_goal_tolerance = yaw_goal_tolerance.to_string(index=False)
xy_goal_tolerance = xy_goal_tolerance.to_string(index=False)
min_vel_x = min_vel_x.to_string(index=False)


# Looking these occurances
DWA_paln_fail = 'msg: "DWA planner failed to produce path."'
DWA_new_plan = 'msg: "Got new plan"'
recovery = 'msg: "Rotate recovery behavior started."'
success = 'Goal reached'

 

# opening a text file
DWA_failed = open("DWA_failed.txt", "r")
DWA_plan = open("DWA_newplan.txt", "r")
recover_executed = open("recovery_executed.txt", "r")
mission_success = open("mission_success.txt", "r")
traveled_distance = open("traveled distance.txt", "r")
mission_time = open("mission_time.txt", "r")
  
# read file content
read_DWA_failed = DWA_failed.read()
read_DWA_plan = DWA_plan.read()
read_recover_executed = recover_executed.read()
read_mission_success = mission_success.read()


# Count occurance
total_DWA_failed_occurrences = read_DWA_failed.count(DWA_paln_fail)
total_DWA_newpan_occurances = read_DWA_plan.count(DWA_new_plan)
total_recover_executed = read_recover_executed.count(recovery)
read_traveled_distance = traveled_distance.read()
read_mission_time = mission_time.read()
total_mission_success = read_mission_success.count(success)


df = pd.DataFrame({"cost_scaling_factor_g":[cost_scaling_factor_g],"update_frequency_g":[update_frequency_g],
                "publish_frequency_g":[publish_frequency_g],"transform_tolerance_g":[transform_tolerance_g], 
                "combination_method_g":[combination_method_g], "inflation_radius_l":[inflation_radius_l],
                "update_frequency_l":[update_frequency_l],"publish_frequency_l":[publish_frequency_l],
                "cost_scaling_factor_l":[cost_scaling_factor_l],"combination_method_l":[combination_method_l],"transform_tolerance_l":[transform_tolerance_l],
                "footprint_padding_l":[footprint_padding_l],
                "path_distance_bias":[path_distance_bias],"goal_distance_bias":[goal_distance_bias],"occdist_scale":[occdist_scale],
                "stop_time_buffer":[stop_time_buffer],"xy_goal_tolerance":[xy_goal_tolerance],"yaw_goal_tolerance":[yaw_goal_tolerance],
                "min_vel_x":min_vel_x,
                "DWA failed":[total_DWA_failed_occurrences], "DWA new plan":[total_DWA_newpan_occurances],
                "Recovery behavior":[total_recover_executed], "Traveled distance":[read_traveled_distance],
                "Mission success":[total_mission_success],
                "Mission time":[read_mission_time]})

if not os.path.isfile('Evaluation_results.csv'):            
    df.to_csv("Evaluation_results.csv", mode='a', index=False, header=True) 
else:
    df.to_csv("Evaluation_results.csv", mode='a', index=False, header=False)


print("DWA planner failed: " + str(total_DWA_failed_occurrences)) 
print("DWA new plan: " + str(total_DWA_newpan_occurances))
print("Recovery executed: " + str(total_recover_executed))
print("Mission success: " + str(total_mission_success))
print("Distance traveled: " + str(read_traveled_distance) + " meters")
print("Mission time: " + str(read_mission_time) + " seconds")

# closing a file
DWA_failed.close() 
DWA_plan.close()
recover_executed.close()
mission_success.close()
mission_time.close()
