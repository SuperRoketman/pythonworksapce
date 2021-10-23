import pyautogui
# 스크린샷 찍기
# img = pyautogui.screenshot()
# img.save("screenshot.png") # 파일로 저장

# pyautogui.mouseInfo()
# 979,18 18,131,208 #1283D0

pixel = pyautogui.pixel(979, 18)
print(pixel)

print(pyautogui.pixelMatchesColor(979, 18, (18, 131, 207)))