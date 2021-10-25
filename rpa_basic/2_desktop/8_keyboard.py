import pyautogui
w = pyautogui.getWindowsWithTitle("제목 없음")[0] # 메모장 1개 띄운 상태에서 가져옴
w.activate()

# pyautogui.write("12345")
# pyautogui.write("MONSTER ENERGY", interval=1)
# pyautogui.write("ㅁㄴㅇㄹ")

# pyautogui.write(["t", "e", "s", "t", "left", "left", "right", "l", "a", "enter"], interval=0.25)
# t e s t 순서대로 적고 왼쪽 방향키 2번, 오른쪽 방향키 1번, l a 순서대로 적고 enter 입력
# left 나 right 같은건 구글에 automate the boring stuff with python 검색하고
# 홈페이지 들어가서 table of contents coqxj 20에 keyboard attribute 검색하면
# 키에 따른 커맨드 나옴.

# 특수문자
# # shift 4 -> $
# pyautogui.keyDown("shift") # 쉬프트 누르고
# pyautogui.press("4") # 4 입력
# pyautogui.keyUp("shift") # 쉬프트 떼고

# 조합키(Hot Key)
# pyautogui.keyDown("ctrl")
# pyautogui.keyDown("a")
# pyautogui.keyUp("a")
# pyautogui.keyUp("ctrl")

# 간편한 조합키
# pyautogui.hotkey("ctrl", "alt", "shift", "a")
# 입력순서로 키다운, 역순으로 키업
# pyautogui.hotkey("ctrl", "a")

import pyperclip
# pyperclip.copy("아머리를몬스따") # 입력된 글자를 클립보드에 저장
# pyautogui.hotkey("ctrl", "v")

def my_write(text):
    pyperclip.copy(text)
    pyautogui.hotkey("ctrl", "v")

my_write("몬스터에너지울트라")

# 자동화 프로그램 종료
# win : ctrl + alt + del
# mac : cmd + sift + option + q