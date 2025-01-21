import pyautogui as pg 
import time

pg.PAUSE = 0.5
vezes=int(input("O limite de conexão por semana 1000 e por dia 140.\nQuantas conexões você deseja fazer ? "))

pg.hotkey("Win","2")
pg.sleep
pg.hotkey("ctrl","t")
pg.write(r"https://www.linkedin.com/notifications")
pg.press('enter')
time.sleep(5)
# pg.vscroll(-3000)
pg.click(x=659, y=99)
time.sleep(5)
pg.click(x=1185, y=442)
time.sleep(5)   
for i in range(vezes):          
    pg.press('tab', presses=3 , interval=0.5)
    pg.press('enter')
    time.sleep(1)
