#!/bin/bash

for i in {1..5}
do
  echo "Running iteration $i..."
  python3 publisher.py
done