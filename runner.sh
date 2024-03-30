#!/bin/sh
# python3 /trippyfinal/sentiment_analysis_backend/sentiment_api/nltkimports.py
# P4=$!
# python /sentiment_analysis/sentiment_analysis_backend/manage.py crontab add &
# P1=$!
python /trippyfinal/Backend/manage.py runserver 0.0.0.0:8000 &
P2=$!
cd /trippyfinal/Frontend && npm start &
P3=$!
# wait $P4 $P1 $P2 $P3
wait $P2 $P3