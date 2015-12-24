#!/bin/bash

cd output
python -m pelican.server &

echo -e "\n  Preview blog at  http://localhost:8000/ \n" 
