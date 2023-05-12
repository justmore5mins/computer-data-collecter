from PIL.ImageGrab import grab

class screendata:
    def __init__(self) -> None:
        pass
    
    def takescreenshot(self):
        grab().save("data/shot.jpg")
        
datas = screendata().takescreenshot()