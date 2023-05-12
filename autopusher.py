from os import system
from time import sleep as delay
from datetime import datetime

folder = "/Users/AustinYu/Library/CloudStorage/GoogleDrive-tno062789@gmail.com/我的雲端硬碟/python/computer data collecter"
repository = "https://github.com/justmore5mins/computer-data-collecter.git"

commands = [
    "git add .",
    "git commit -m \"add\"",
    "git push"
    
]

while True:
    print("\n")
    print("start push codes")
    print("nowtime:",datetime.now())
    for command in commands:
        system(command)
    
    delay(600)