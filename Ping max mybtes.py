import subprocess
import random

def ping(host, size):
     result = subprocess.run(['ping', '-c', '1', '-s', str(size), host], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
     return result.returncode == 0

ip_address = ["X.X.X.X"]
max_size = 1472

for ip in ip_address:
    print(f"Testing IP addresss ")
    while True:
        for size in range(64, max_size+1, 8):
            if ping(ip, size):
                print(f"Successful")
                break
            else:
                print(f"Failed")

