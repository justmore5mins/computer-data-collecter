from pyautogui import screenshot

class screendata:
    screenshot:str = "data"
    def __init__(self) -> None:
        pass
    
    def takescreenshot(self):
        shots = screenshot()
        shots.save(self.screenshot)
        
datas = screendata().takescreenshot()