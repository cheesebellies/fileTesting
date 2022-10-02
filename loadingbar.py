import subprocess
import os

subprocessout = subprocess.Popen(f"ffprobe -show_data -hide_banner {os.listdir('~/Downloads/')[0]}", shell=True, stdout=subprocess.PIPE)
resultout = subprocessout.stdout.read().decode().strip()
s = str(resultout)

vmbps = (int(s.split("Video: ")[-1].split("kb/s")[0].split(", ")[-1][:-1]))/1000
ambps = (int(s.split("Audio: ")[-1].split("kb/s")[0].split(", ")[-1][:-1]))/1000
tmbps = vmbps+ambps
dur = (s.split("Duration: ")[-1].split(",")[0]).split(":")
ts = (int(dur[0])*3600) + (int(dur[1])*60) + (int(dur[0].split(".")[0]))
size = int(1000*((tmbps/8)*ts))

print(size)