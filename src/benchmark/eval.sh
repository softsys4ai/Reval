#!/bin/sh

# Extract /rosout and other topics
time ros_readbagfile log/all_topics.bag /rosout > log/topics.yaml
time ros_readbagfile log/all_topics.bag /battery/status > log/battery_status.yaml
time ros_readbagfile log/all_topics.bag /collisions > log/collisions.yaml

sleep 3

# How many times DWA planner failed
time rg 'msg: "DWA planner failed to produce path' log/topics.yaml | sort -V > log/DWA_failed.txt

# How many times DWA replanned
time rg 'msg: "Invalid Trajectory' log/topics.yaml | sort -V > log/DWA_invalid_trajectory.txt

# How many time DWA planner invalid trajectory
time rg 'msg: "Got new plan' log/topics.yaml | sort -V > log/DWA_newplan.txt


# How many times executed rotate recovery behavior
time rg 'msg: "Rotate recovery behavior started' log/topics.yaml | sort -V > log/rotate_recovery_executed.txt

# How many times executed ClearCostMaps recovery to unstuck robot
time rg 'msg: "Clearing both costmaps to unstuck robot' log/topics.yaml | sort -V > log/clearCostMaps_ur_recovery_executed.txt

# How many times executed ClearCostMaps recovery to clear a layer (e.g., obstacle layer)
time rg 'msg: "Recovery behavior will clear layer'  log/topics.yaml | sort -V > log/clearCostMaps_layer_recovery_executed.txt


# Once a goal position is reached... rotate to the goal orientation.
# checking if the action is leagal while rotating on goal LatchedStopRotateController::rotateToGoal
# invalid rotation cmd
time rg 'msg: "Rotation cmd in collision' log/topics.yaml | sort -V > log/invalid_rotation_cmd.txt

# Error rotating on goal
time rg 'msg: "Error when rotating' log/topics.yaml | sort -V > log/rotating_goal_error.txt

# Mission failed
# time rg 'msg: "Aborting' log/topics.yaml | sort -V > log/mission_fail.txt

# Mission success
time rg 'msg: "Goal reached' log/topics.yaml | sort -V > log/mission_success.txt

# Battery 
time rg 'percentage: ' log/battery_status.yaml | sort -V > log/battery_percentage.txt

# Collisions 
time rg 'data: ' log/collisions.yaml | sort -V > log/collisions.txt
