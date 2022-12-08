import os
import pandas as pd
from datetime import datetime
from tabulate import tabulate
from goals import *

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    CGREEN  = '\33[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# Reading configs
df_config = pd.read_csv('log/configs.csv')
cost_scaling_factor_g = df_config['cost_scaling_factor_g']
update_frequency_g = df_config['update_frequency_g']
publish_frequency_g = df_config['publish_frequency_g']
transform_tolerance_g = df_config['transform_tolerance_g']
combination_method_g = df_config['combination_method_g']

cost_scaling_factor_l = df_config['cost_scaling_factor_l']
inflation_radius_l = df_config['inflation_radius_l']
update_frequency_l = df_config['update_frequency_l']
publish_frequency_l = df_config['publish_frequency_l']
combination_method_l = df_config['combination_method_l']
transform_tolerance_l = df_config['transform_tolerance_l']

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
combination_method_g = combination_method_g.to_string(index=False)

inflation_radius_l = inflation_radius_l.to_string(index=False)
update_frequency_l = update_frequency_l.to_string(index=False)
publish_frequency_l = publish_frequency_l.to_string(index=False)
cost_scaling_factor_l = cost_scaling_factor_l.to_string(index=False)
combination_method_l = combination_method_l.to_string(index=False)
transform_tolerance_l = transform_tolerance_l.to_string(index=False)

path_distance_bias = path_distance_bias.to_string(index=False)
goal_distance_bias = goal_distance_bias.to_string(index=False)
occdist_scale = occdist_scale.to_string(index=False)
stop_time_buffer = stop_time_buffer.to_string(index=False)
yaw_goal_tolerance = yaw_goal_tolerance.to_string(index=False)
xy_goal_tolerance = xy_goal_tolerance.to_string(index=False)
min_vel_x = min_vel_x.to_string(index=False)

# Looking for these occurances
DWA_paln_fail = 'msg: "DWA planner failed to produce path."'
DWA_new_plan = 'msg: "Got new plan"'
DWA_invalid_trajectory = 'msg: "Invalid Trajectory'
rotate_recovery = 'msg: "Rotate recovery behavior started."'
ClearCostMaps_ur_recovery = 'msg: "Clearing both costmaps to unstuck robot'
clearCostMaps_layer_recovery = 'msg: "Recovery behavior will clear layer'
rotation_cmd_collision = 'msg: "Rotation cmd in collision'
error_rotating = 'msg: "Error when rotating'
success = 'msg: "Goal reached'

# battery percentage post-processing
skip_word_bp = "battery: "
 
# opening a text file
DWA_failed = open("log/DWA_failed.txt", "r")
DWA_plan = open("log/DWA_newplan.txt", "r")
DWA_trajectory = open("log/DWA_invalid_trajectory.txt", "r")
rotate_recovery_executed = open("log/rotate_recovery_executed.txt", "r")
clearCostMaps_ur_recovery_executed = open("log/clearCostMaps_ur_recovery_executed.txt", "r")
clearCostMaps_layer_recovery_executed = open("log/clearCostMaps_layer_recovery_executed.txt", "r")
invalid_rotation_cmd = open("log/invalid_rotation_cmd.txt", "r")
rotating_goal_error = open("log/rotating_goal_error.txt", "r")
rns = open("log/robustness_narrow_space.txt", "r")
two_Drms = open("log/twoDrms.txt", "r")
Drms = open("log/drms.txt", "r")
Cpe = open("log/cpe.txt", "r")
euclidean_distance = open("log/euclidean_distance.txt", "r")
traveled_distance = open("log/traveled distance.txt", "r")
mission_time = open("log/mission_time.txt", "r")
bat_percentage = open("log/battery_percentage.txt", "r")
mission_success = open("log/mission_success.txt", "r")

# read file content
read_DWA_failed = DWA_failed.read()
read_DWA_plan = DWA_plan.read()
read_DWA_trajectory = DWA_trajectory.read()
read_rotate_recovery_executed = rotate_recovery_executed.read()
read_clearCostMaps_ur_recovery_executed = clearCostMaps_ur_recovery_executed.read()
read_clearCostMaps_layer_recovery = clearCostMaps_layer_recovery_executed.read()
read_invalid_rotation_cmd = invalid_rotation_cmd.read()
read_rotating_goal_error = rotating_goal_error.read()
read_mission_success = mission_success.read()

# Count occurance
total_DWA_failed_occurrences = read_DWA_failed.count(DWA_paln_fail)
total_DWA_newplan_occurances = read_DWA_plan.count(DWA_new_plan)
total_DWA_invalid_trajectory = read_DWA_trajectory.count(DWA_invalid_trajectory)
total_rotate_recovery_executed = read_rotate_recovery_executed.count(rotate_recovery)
total_clearCostMaps_ur_recovery_executed = read_clearCostMaps_ur_recovery_executed.count(ClearCostMaps_ur_recovery)
total_clearCostMaps_layer_recovery = read_clearCostMaps_layer_recovery.count(clearCostMaps_layer_recovery)
total_invalid_rotation_cmd = read_invalid_rotation_cmd.count(rotation_cmd_collision)
total_rotating_goal_error = read_rotating_goal_error.count(error_rotating)
read_rns = rns.read()
read_two_Drms = two_Drms.read()
read_Drms = Drms.read()
read_Cpe = Cpe.read()
read_euclidean_distance = euclidean_distance.read()
read_traveled_distance = traveled_distance.read()
read_mission_time = mission_time.read()

# battery
voltage_min = 11.1
voltage_max = 12.2
first_line = bat_percentage.readline().strip()
volatge = first_line.replace(skip_word_bp, '')
volatge = float(volatge)
print(volatge)
battery_percentage = round(((volatge - voltage_min) / (voltage_max - voltage_min)) * 100, 2)
print(battery_percentage)
# 

# determining mission success
total_mission_success  = read_mission_success.count(success)
read_rns = total_mission_success / target_locations
# If all target reached then mission is a success
if total_mission_success == target_locations:
    ms = 1
else:
    ms = 0    

df = pd.DataFrame({"cost_scaling_factor_g":[cost_scaling_factor_g],"update_frequency_g":[update_frequency_g],
                "publish_frequency_g":[publish_frequency_g],"transform_tolerance_g":[transform_tolerance_g], 
                "combination_method_g":[combination_method_g], "inflation_radius_l":[inflation_radius_l],
                "update_frequency_l":[update_frequency_l],"publish_frequency_l":[publish_frequency_l],
                "cost_scaling_factor_l":[cost_scaling_factor_l],"combination_method_l":[combination_method_l],
                "transform_tolerance_l":[transform_tolerance_l],
                "path_distance_bias":[path_distance_bias],"goal_distance_bias":[goal_distance_bias],
                "occdist_scale":[occdist_scale],"stop_time_buffer":[stop_time_buffer],"xy_goal_tolerance":[xy_goal_tolerance],
                "yaw_goal_tolerance":[yaw_goal_tolerance],"min_vel_x":min_vel_x,
                "DWA failed":[total_DWA_failed_occurrences], "DWA new plan":[total_DWA_newplan_occurances],
                "DWA invalid trajectory":[total_DWA_invalid_trajectory],"Rotate recovery executed":[total_rotate_recovery_executed], 
                "ClearCostMaps unstuck recovery executed":[total_clearCostMaps_ur_recovery_executed],
                "ClearCostMaps layer recovery executed":[total_clearCostMaps_layer_recovery],"Invalid rotation cmd":[total_invalid_rotation_cmd],
                "Error rotating goal":[total_rotating_goal_error],
                "2Drms":[read_two_Drms], "Drms":[read_Drms], "CPE":[read_Cpe],"Euclidean distance":[read_euclidean_distance],
                "RNS":[read_rns],"Traveled distance":[read_traveled_distance],"Mission time":[read_mission_time],"Battery percentage":[battery_percentage],
                "Mission success":[ms]})

if not os.path.isfile('log/eval.csv'):            
    df.to_csv("log/eval.csv", mode='a', index=False, header=True) 
else:
    df.to_csv("log/eval.csv", mode='a', index=False, header=False)


# closing a file
DWA_failed.close() 
DWA_plan.close()
DWA_trajectory.close()
rotate_recovery_executed.close()
clearCostMaps_ur_recovery_executed.close()
clearCostMaps_layer_recovery_executed.close()
invalid_rotation_cmd.close()
rotating_goal_error.close()
rns.close()
# two_DrmsG.close()
two_Drms.close()
Drms.close()
Cpe.close()
euclidean_distance.close()
traveled_distance.close()
mission_time.close()
bat_percentage.close()
mission_success.close()



# --------------- For visualization and saving csv ----------------
# Evaluation metrics
df2 = pd.read_csv('log/eval.csv')
DWA_failed = df2['DWA failed']
DWA_newplan = df2['DWA new plan']
DWA_invalid_trajectory = df2['DWA invalid trajectory']
rotate_recovery_executed = df2['Rotate recovery executed']
clearCostMaps_ur_recovery_executed = df2['ClearCostMaps unstuck recovery executed']
ClearCostMaps_layer_recovery_executed = df2['ClearCostMaps layer recovery executed']
invalid_rotation_cmd = df2['Invalid rotation cmd']
error_rotating_goal = df2['Error rotating goal']
# twoDrmsG = df2['2DrmsG']
two2Drms = df2['2Drms']
Drms = df2['Drms']
CPE = df2['CPE']
euclidean_distance = df2['Euclidean distance']
RNS = df2['RNS']
distance_traveled = df2['Traveled distance']
# collisions = df2['Collisions']
mission_time = df2['Mission time']
battery_percentage = df2['Battery percentage']
mission_success = df2['Mission success']

# Configurations
cost_scaling_factor_g = df2['cost_scaling_factor_g']
update_frequency_g = df2['update_frequency_g']
publish_frequency_g = df2['publish_frequency_g']
transform_tolerance_g = df2['transform_tolerance_g']
# footprint_padding_g = df2['footprint_padding_g']
combination_method_g = df2['combination_method_g']

cost_scaling_factor_l = df2['cost_scaling_factor_l']
inflation_radius_l = df2['inflation_radius_l']
update_frequency_l = df2['update_frequency_l']
publish_frequency_l = df2['publish_frequency_l']
combination_method_l = df2['combination_method_l']
transform_tolerance_l = df2['transform_tolerance_l']
# footprint_padding_l = df2['footprint_padding_l']

path_distance_bias = df2['path_distance_bias']
goal_distance_bias = df2['goal_distance_bias']
occdist_scale = df2['occdist_scale']
stop_time_buffer = df2['stop_time_buffer']
yaw_goal_tolerance = df2['yaw_goal_tolerance']
xy_goal_tolerance = df2['xy_goal_tolerance']
min_vel_x = df2['min_vel_x']

# For terminal
dataT = [RNS, distance_traveled, mission_time,battery_percentage, mission_success]
headersT = ["RNS", "DT", "MT", "BP", "MS"]

# For csv
dataS = [cost_scaling_factor_g, update_frequency_g, publish_frequency_g, transform_tolerance_g,
        combination_method_g, cost_scaling_factor_l, inflation_radius_l, update_frequency_l, publish_frequency_l,
        combination_method_l, transform_tolerance_l, path_distance_bias, goal_distance_bias,
        occdist_scale, stop_time_buffer, yaw_goal_tolerance, xy_goal_tolerance, min_vel_x,
        DWA_failed, DWA_newplan, DWA_invalid_trajectory, rotate_recovery_executed,
        clearCostMaps_ur_recovery_executed, ClearCostMaps_layer_recovery_executed, invalid_rotation_cmd, 
        error_rotating_goal, two2Drms, Drms, CPE, euclidean_distance, RNS, distance_traveled, mission_time, battery_percentage, mission_success]
headerS = ["Cost_scaling_factor_global", "Update_frequency_global", "Publish_frequency_global", "Transform_tolerance_global",
            "Combination_method_global", "Cost_scaling_factor_local", "Inflation_radius_local",
            "Update_frequency_local", "Publish_frequency_local", "Combination_method_local", "Transform_tolerance_local",
            "Path_distance_bias", "Goal_distance_bias", "Occdist_scale", "Stop_time_buffer",
            "yaw_goal_tolerance", "xy_goal_tolerance", "min_vel_x",
            "DWA_failed", "DWA_new_plan", "DWA_invalid_trajectory", "Rotate_recovery_executed", "ClearCostMaps_unstuck_recovery_executed", 
            "ClearCostMaps_layer_recovery_executed", "Invalid_rotation_cmd", "Error_rotating_goal","2DRMS","DRMS","CPE","Euclidean_distance","RNS", "Traveled_distance", 
            "Mission_time","Battery_percentage", "Mission_success"]

# For terminal
df3 = pd.DataFrame(dataT, headersT)
df3 = df3.T

# Organizing the csv
df4 = pd.DataFrame(dataS, headerS)
df4 = df4.T
if not os.path.exists('../../results'):
    os.makedirs('../../results')
timestamp = datetime.now().strftime("%Y_%m_%d-%I_%M_%S_%p")
df4.to_csv(f"../../results/Evaluation_results_{timestamp}.csv", index=False, header=True)

print("")
#print(bcolors.HEADER + "-----------------------------------------Evaluation results-----------------------------------------" + bcolors.ENDC) 
print(bcolors.HEADER + "<----------Evaluation results---------->" + bcolors.ENDC) 
print(tabulate(df3, headers='keys', tablefmt='grid'))
print(bcolors.OKCYAN + "Check Reval/Evaluation_results.csv for the detail result!" + bcolors.ENDC)
print("")