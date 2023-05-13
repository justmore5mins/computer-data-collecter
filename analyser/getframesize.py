from PIL import Image

class analysic:
    imagepath:str
    size:tuple
    def __init__(self, path = "/Users/AustinYu/Library/CloudStorage/GoogleDrive-tno062789@gmail.com/我的雲端硬碟/python/computer data collecter/datacollecter/data/shot.png"):
        self.imagepath = path
        
    def getsize(self) -> tuple[int,int]:
        w, h = Image.open(self.imagepath).size
        self.size = (w,h)
        return self.size