kill $(ps aux | grep '[r]fbproxy' | awk '{print $2}')
python3 app.py