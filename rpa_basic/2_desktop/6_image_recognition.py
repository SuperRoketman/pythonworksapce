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

# checkbox = pyautogui.locateOnScreen("checkbox.png")
# pyautogui.click(checkbox)
# 그냥은 제일 먼저 찾는 1개만 할당

# upsign = pyautogui.locateOnScreen("upsign.png")
# pyautogui.moveTo(upsign)

# 속도 개선
# 1. GrayScale / 정확도가 조금 떨어질 수 있음
# upsign = pyautogui.locateOnScreen("upsign.png", grayscale=True)
# pyautogui.moveTo(upsign)

# 2. 범위 지정
# upsign = pyautogui.locateOnScreen("upsign.png", region=(1776, 760, 141, 100))
# pyautogui.moveTo(upsign)

# 3. 정확도 조정
# run_btn = pyautogui.locateOnScreen("run_btn.png", confidence=0.9) # 90%
# pyautogui.moveTo(run_btn)

# 자동화 대상이 바로 보여지지 않는 경우
# 1. 계속 대기
# file_menu_notepad = pyautogui.locateOnScreen("file_menu_notepad.png")
# # if file_menu_notepad:
# #     pyautogui.click(file_menu_notepad)
# # else:
# #     print("발견 실패")
# while file_menu_notepad is None:
#     file_menu_notepad = pyautogui.locateOnScreen("file_menu_notepad.png")
#     print("발견 실패")
# pyautogui.click(file_menu_notepad)

# 2. 일정 시간동안 기다리기(TimeOut)
import time
import sys

# timeout = 10 # 10초 대기
# start = time.time() # 시작시간 설정
# file_menu_notepad = None
# while file_menu_notepad is None:
#     file_menu_notepad = pyautogui.locateOnScreen("file_menu_notepad.png")
#     end = time.time() # 종료 시간 설정
#     if end - start > timeout: # 지정시간 초과
#         print("시간 초과")
#         sys.exit()

# pyautogui.click(file_menu_notepad)

def find_target(img_file, timeout=30):
    start = time.time()
    target = None
    while target is None:
        target = pyautogui.locateOnScreen(img_file)
        end = time.time()
        if end - start > timeout:
            break
    return target

def my_click(img_file, timeout=30):
    target = find_target(img_file, timeout)
    if target:
        pyautogui.click(target)
    else:
        print(f"[Timeout {timeout}s] Target not found ({img_file}). Terminate program.")
        sys.exit()

my_click("file_menu_notepad.png", 10)