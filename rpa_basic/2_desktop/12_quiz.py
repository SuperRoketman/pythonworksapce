# Quiz) 아래 동작을 자동으로 수행하는 프로그램을 작서하시오

# 1. 그림판 실행 (단축키 : win + r, 입력값 : mspaint) 및 최대화

# 2. 상단의 텍스트 기능을 이용하여 흰 영역 아무 곳에다가 글자 입력
#  - 입력 글자 : "참 잘했어요"

# 3. 5초 대기 후 그림판 종료
#  이 때, 저장하지 않음을 자동으로 선택하여 프로그램이 완전 종료되도록 함.

import pyautogui
import pyperclip

pyautogui.hotkey("win", "r")
pyautogui.sleep(1)
pyautogui.write("mspaint")
pyautogui.press("enter")
pyautogui.sleep(1)

w = pyautogui.getWindowsWithTitle("제목 없음")[0]
if w.isActive == False:
    w.activate() # 활성화 (맨 앞으로 가져오기)

if w.isMaximized == False:
    w.maximize()

pyautogui.sleep(1)


# 나
# text_btn = pyautogui.locateOnScreen("text_btn.png")
# pyautogui.click(text_btn)

# 유튜버
import sys
text_btn = pyautogui.locateOnScreen("text_btn.png")
if text_btn:
    pyautogui.click(text_btn)
else:
    print("찾기 실패")
    sys.exit()


pyautogui.sleep(1)

# 나
# pyautogui.click(933,534)

# 유튜버
brush = pyautogui.locateOnScreen("brush.png")
pyautogui.click(brush.left - 200, brush.top + 200)

pyautogui.sleep(1)

pyperclip.copy('"참 잘했어요"')
pyautogui.hotkey("ctrl", "v")

pyautogui.sleep(5)

w.close()

pyautogui.sleep(1)

# 나
# not_save = pyautogui.locateOnScreen("not_save.png")
# pyautogui.click(not_save)

# 유튜버
pyautogui.press("n")