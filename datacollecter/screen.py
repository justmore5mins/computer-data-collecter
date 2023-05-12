from PIL.ImageGrab import grab

class screendata:
    shotpath:str
    def __init__(self,shotpath:str) -> None:
        self.shotpath = shotpath
    
    def takescreenshot(self):
        grab().save(self.shotpath)

screendata("data/shot.png").takescreenshot()