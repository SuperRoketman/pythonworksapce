from imap_tools import MailBox
from account import*

# mailbox = MailBox("imap.gmail.com", 993)
# mailbox.login(EMAIL_ADDRESS, EMAIL_PASSWORD, initial_folder="INBOX")

with MailBox("imap.gmail.com", 993).login(EMAIL_ADDRESS, EMAIL_PASSWORD, initial_folder="INBOX") as mailbox:
    # for msg in mailbox.fetch(): # 전체 메일 다 가져오기
        # print("[{}] {}".format(msg.from_, msg.subject))

    # for msg in mailbox.fetch('(UNSEEN'): # 읽지 않은 메일 다 가져오기
    #     print("[{}] {}".format(msg.from_, msg.subject))

    # for msg in mailbox.fetch('FROM cook144k@gmail.com', limit=3, reverse=True): # 특정인이 보낸 메일 가져오기
    #     print("[{}] {}".format(msg.from_, msg.subject)) 

    # 작은 따옴표로 먼저 감싸고, 실제 TEXT 부분은 큰 따옴표로 감싸주세요
    # for msg in mailbox.fetch('(TEXT "test mail")'): # 어떤 글자를 포함하는 메일 가져오기
    #     print("[{}] {}".format(msg.from_, msg.subject))

    # for msg in mailbox.fetch('(SUBJECT "test mail")'): # 제목을 포함한 메일 가져오기
    #     print("[{}] {}".format(msg.from_, msg.subject))

    # 한글을 못쓰기 때문에 우회방법을 써야함
    # for msg in mailbox.fetch(limit=5, reverse=True): # 어떤 글자(한글)를 포함하는 메일 필터링
    #     if "테스트" in msg.subject:
    #         print("[{}] {}".format(msg.from_, msg.subject))

    # for msg in mailbox.fetch('(SENTSINCE 01-Oct-2021)', reverse=True, limit=5): # 특정 날짜 이후의 메일
    #     print("[{}] {}".format(msg.from_, msg.subject))

    # for msg in mailbox.fetch('(ON 01-Oct-2021)', limit=5, reverse=True): # 특정 날짜에 온 메일
    #     print("[{}] {}".format(msg.from_, msg.subject))

    # imaps tool 사이트에서 메일 검색 조건 찾아볼 수 있ㅇ므

    # 2가지 이상의 조건을 모두 만족하는 메일
    # for msg in mailbox.fetch('(ON 01-Oct-2021 SUBJECT "test mail")', reverse=True):
    #     print("[{}] {}".format(msg.from_, msg.subject))

    # 2가지 이상의 조건 중 하나라도 만족하는 메일
    for msg in mailbox.fetch('(OR ON 01-Oct-2021 SUBJECT "test mail")', reverse=True):
        print("[{}] {}".format(msg.from_, msg.subject))