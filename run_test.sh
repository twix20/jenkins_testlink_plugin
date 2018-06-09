#!/usr/bin/env bash

pip install --user -r requirements.txt

find . -name "*_tests.py" -print | while read f; do
        echo "$f"
        ###
        python -m coverage run "$f"
        python -m coverage xml -o coverage.xml
        ###
done
