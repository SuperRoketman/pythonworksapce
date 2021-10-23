import pyautogui
# pyautogui.FAILSAFE = False
pyautogui.PAUSE = 1 # 모든 동작에 sleep 1 적용
# pyautogui.mouseInfo() # F1 입력시 3초 후 그 당시 마우스 정보 저장 (1014,13 179,179,179 #B3B3B3)

for i in range(5):
    pyautogui.move(100, 100)
    # pyautogui.sleep(1)