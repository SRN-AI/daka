#!/bin/bash
read -p "Please input token and session:" token session
python3 ~/daka/update.py ~/daka/app.json ${token} ${session}
