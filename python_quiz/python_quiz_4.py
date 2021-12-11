# quiz) 신조어 퀴즈 클래스
# - Word 클래스 작성
# __init__(...) : 신조어, 보기1, 보기2, 정답을 받아서 멤버 변수 설정
# show_question(...) : 질문 내용 표시
# check_answer(...) : 입력값이 정답인지 확인하여 "정답입니다" " 틀렸습니다" 출력

# - 예제
# word = Word("얼죽아", "얼어 죽어도 아메리카노", "얼굴만은 죽어도 아기피부", 1)
# word.show_question()
# word.check_answer(int(input("=> ")))

# - 출력 결과
# "얼죽아" 의 뜻은?
# 1. 얼어 죽어도 아메리카노
# 2. 얼굴만은 죽어도 아기피부
# => 1
# 정답입니다.

class Word:
    def __init__(self, new_word, selection1, selection2, answer):
        self.new_word = new_word
        self.selection1 = selection1
        self.selection2 = selection2
        self.answer = answer

    def show_question(self):
        print(f"""
"{self.new_word}" 의 뜻은?
1. {self.selection1}
2. {self.selection2}""")
    
    def check_answer(self, inputs):
        if self.answer == inputs:
            print("정답입니다.")
        else:
            print("오답입니다.")


word = Word("얼죽아", "얼어 죽어도 아메리카노", "얼굴만은 죽어도 아기피부", 1)

word.show_question()
word.check_answer(int(input("=> ")))