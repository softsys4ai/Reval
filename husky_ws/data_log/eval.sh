#!/bin/sh

# Extract /rosout
time ros_readbagfile all_topics.bag /rosout > topics.yaml

sleep 3

# How many times DWA planner failed
time rg 'msg: "DWA planner failed to produce path' topics.yaml | sort -V > DWA_failed.txt
sleep 1
# How many times DWA replanned
time rg 'msg: "Got new plan' topics.yaml | sort -V > DWA_newplan.txt
sleep 1
# How many times executed recovery behavior
time rg 'msg: "Rotate recovery behavior started' topics.yaml | sort -V > recovery_executed.txt
sleep 1
# Mission failed
time rg 'msg: "Aborting' topics.yaml | sort -V > mission_fail.txt
sleep 1
# Mission success
time rg 'msg: "Goal reached' topics.yaml | sort -V > mission_success.txt
