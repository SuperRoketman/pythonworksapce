import pyautogui
# file_menu = pyautogui.locateOnScreen("file_menu.png")
# print(file_menu)
# pyautogui.click(file_menu)

# upsign = pyautogui.locateOnScreen("upsign.png")
# pyautogui.moveTo(upsign)

# screen = pyautogui.locateOnScreen("screenshot.png")
# print(screen)

# for i in pyautogui.locateAllOnScreen("checkbox.png"):
#     print(i)
#     pyautogui.click(i)

checkbox = pyautogui.locateOnScreen("checkbox.png")
pyautogui.click(checkbox)
# 그냥은 제일 먼저 찾는 1개만 할당