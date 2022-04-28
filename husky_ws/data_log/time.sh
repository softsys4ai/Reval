#!/bin/sh




start_time="$(date +%s)"
sleep 2
current_time="$(date +%s)"
seconds=$(( $current_time-$start_time ))

echo -ne "\rTime: $seconds"
