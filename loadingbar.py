import subprocess
import os
from tqdm import tqdm
import time
from replit import db

class Bar:

  def __init__(self):
    pass

  def get_prog(self,cmd2):
    output = subprocess.run(cmd2, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    
    prog = (str(output.stdout.decode())).split("runner ")[-1].split(" ")[0]
    # if prog == prevprog:
    #   return "Done"
    # else:
      # print(int(prog))
    return int((int(prog))/1000000)

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
    size = int((int(((tmbps/8)*ts))))
    
    cmd2 = f'ls -l /home/runner/Downloads/{a}'
    count = 0
    remt=[]
    while True:
      size2 = self.get_prog(cmd2)
      print(f"DOWNLOADING FILE: {size2}/{size}mb  [{'#'*(int(10*(size2/size)))}{' '*(10-int(10*(size2/size)))}]",end="\r")
      if size == size2:
        print("DOWNLOAD COMPLETE.")
        time.sleep(60)
        db["isdone"] = True
        os.system("./runapp.sh")
        break
      time.sleep(.25)
      count += .25
    # print(size)
    
    # with tqdm(total=size) as pbar:
    #   previprog = 0
    #   aba = True
    #   while True:
    #     previprog = self.get_prog(previprog,cmd2)
    #     if type(previprog) == str:
    #       pbar.update(size)
    #       break
    #     elif type(previprog) == int and previprog >= size:
    #       pbar.update(size)
    #       break
    #     else:
    #       if aba:
    #         aba = False
    #         pbar.update(previprog)
    #       else:
    #         pbar.update(previprog)
    #     time.sleep(.25)