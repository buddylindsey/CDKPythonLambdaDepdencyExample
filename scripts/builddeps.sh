#! /bin/bash

source deps/bin/activate
pip install -r requirements/lambda.txt -t ./python
find ./python | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs rm -rf
zip -r python.zip ./python/
cp python.zip ./output