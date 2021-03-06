# quiz) 당신은 (주)나도출판의 편집자.
# 유튜버들에게 제안서를 보냄.
# 동일한 내용의 메일에 유튜버 이름 정보만 변경하여
# 파일로 저장하는 프로그램.

# [조건]
# 1. 유튜버 이름은 리스트로 제공 (최소 2명 이상)
# 예) names = ["유튜버1", "유투버2",...]

# 2. 파일 명은 '유튜버 이름.txt'

# [메일 본문]
# 안녕하세요? XXX님.

# (주)나도출판 편집자 나코입니다.
# 현재 저희 출판사는 파이썬에 관한 주제로 책 출간을 기획 중입니다.
# XXX님의 유튜브 영상을 보고 연락을 드리게 되었습니다.
# 자세한 내용은 첨부드리는 제안서를 확인 부탁드리며, 긍정적인 회신 기다리겠습니다.

# 좋은 하루 보내세요 ^^
# 감사합니다.

# - 나코 드림.
names = []
for name in range(1,3):
    Youtuber_name = f"유튜버{name}"
    names.append(Youtuber_name)
for name in names:
    f = open(f"{name}.txt", "w", encoding="utf8") # 이 문장은 with open(f"{name}.txt", "w", encoding="utf8") as f 와 같다
    f.write(f"""
안녕하세요? {name}님.

(주)나도출판 편집자 나코입니다.
현재 저희 출판사는 파이썬에 관한 주제로 책 출간을 기획 중입니다.
{name}님의 유튜브 영상을 보고 연락을 드리게 되었습니다.
자세한 내용은 첨부드리는 제안서를 확인 부탁드리며, 긍정적인 회신 기다리겠습니다.

좋은 하루 보내세요 ^^
감사합니다.

- 나코 드림.
""")
    f.close()