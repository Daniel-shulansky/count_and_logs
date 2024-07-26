#!/bin/bash

service='app'
max_scale=5
min_scale=3

curr=$(docker compose ps -q $service | wc -l)

if [ $curr -lt $max_scale ]; then
	docker compose up -d --scale $service=$max_scale
        echo --- upscaling $service to $max_scale ---
else
	docker compose up -d --scale $service=$min_scale
	echo --- downscaling $service to $min_scale ---
fi
