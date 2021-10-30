import smtplib
from account import *
from email.message import EmailMessage

msg = EmailMessage()
msg["Subject"] = "테스트 메일입니다." # 제목
msg["From"] = EMAIL_ADDRESS # 송신자
msg["To"] = "cook144k@gmail.com" # 수신자

# 다수의 수신자
# msg["To"] = "cook144k@gmail.com, cook144k@naver.com"

# to_list = ["cook144k@gmail.com", "cook144k@naver.com"]
# msg["To"] = ", ".join(to_list)


# 참조
# msg["Cc"] = "cook144k@gmail.com"

# 비밀참조
# msg["Bcc"] = "cook144k@gmail.com"

msg.set_content("테스트 본문입니다.") # 본문

with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)