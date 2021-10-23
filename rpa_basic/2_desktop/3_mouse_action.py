import pyautogui

pyautogui.sleep(3)
# print(pyautogui.position())

# pyautogui.click(1006, 18, duration=1) # (64,17) 좌표를 클릭
# pyautogui.click()
# pyautogui.mouseDown()
# pyautogui.mouseUp()

# pyautogui.doubleClick()
# pyautogui.click(clicks=500)

# pyautogui.moveTo(200, 200)
# pyautogui.mouseDown()
# pyautogui.moveTo(300, 300)
# pyautogui.mouseUp()
# pyautogui.rightClick()
# pyautogui.middleClick()

# pyautogui.moveTo(592, 417)
# pyautogui.drag(500, 0, duration=0.25) # 너무 빨라서 동작수행 안되면 duration 설정
# pyautogui.dragTo(592, 417, duration=0.3)

pyautogui.scroll(300) # 양수이면 위 방향으로 300만큼 스크롤, 음수이면 아래로