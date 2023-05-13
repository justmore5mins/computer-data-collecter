from PIL.ImageGrab import grab

class screendata:
    shotpath:str
    def __init__(self,shotpath:str = "data/shot.png") -> None:
        self.shotpath = shotpath
    
    def takescreenshot(self):
        grab().save(self.shotpath)
        
screendata().takescreenshot()