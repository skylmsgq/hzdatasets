#!/bin/bash

echo "Running minigps.py in batch..."
for i in $(seq 1 9); do
	echo "Start $i ..."
	python minigps.py split-$i.txt $i &
done