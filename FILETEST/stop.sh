kill $(ps aux | grep '[r]fbproxy' | awk '{print $2}')
rm -r ~/Downloads/