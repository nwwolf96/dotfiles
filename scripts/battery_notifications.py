import subprocess
import time
while(True):
    time.sleep(60) # Sleep for 30 seconds
    p = subprocess.Popen("upower -i $(upower -e | grep 'BAT') | grep percentage ", shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    percentage = 0
    for line in p.stdout.readlines():
        percentage = int(str(line).split(":          ")[1].split("%")[0])
    retval = p.wait()
    if (percentage < 30):
        command = "notify-send --icon=gtk-info Battery \"Battery at " + str(percentage) + " percent\""   
        p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        