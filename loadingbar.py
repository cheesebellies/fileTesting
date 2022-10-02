import subprocess
import os

a = os.listdir("/home/runner/Downloads/")[0]

cmd = f'ffprobe -show_data -hide_banner /home/runner/Downloads/{a}'

output = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)

s = str(output.stderr.decode())

vmbps = (int(s.split("Video: ")[-1].split("kb/s")[0].split(", ")[-1][:-1]))/1000
ambps = (int(s.split("Audio: ")[-1].split("kb/s")[0].split(", ")[-1][:-1]))/1000
tmbps = vmbps+ambps
dur = (s.split("Duration: ")[-1].split(",")[0]).split(":")
ts = (int(dur[0])*3600) + (int(dur[1])*60) + (int(dur[0].split(".")[0]))
size = int(1000*((tmbps/8)*ts))

print(size)