import subprocess
import os
from tqdm import tqdm
import time

class Bar:

  def __init__(self):
    pass

  def get_prog(prevprog,cmd2):
    output = subprocess.run(cmd2, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    
    prog = (str(output.stdout.decode())).split("runner ")[-1].split(" ")[0]
    if prog == prevprog:
      return "Done"
    else:
      return int((int(prog))/1000)

  def Start(self):
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
    
    cmd2 = f'ls -l /home/runner/Downloads/{a}'
    
    with tqdm(total=size) as pbar:
      previprog = 0
      previprog2 = 0
      while True:
        previprog = self.get_prog(previprog,cmd2)
        if type(previprog) == str:
          pbar.update(size)
          break
        elif type(previprog) == int and previprog >= size:
          pbar.update(size)
          break
        else:
          pbar.update(previprog-previprog2)
        previprog = previprog2
        time.sleep(.25)