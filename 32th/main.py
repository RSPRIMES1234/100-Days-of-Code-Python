import smtplib
import datetime as dt
import random



if dt.datetime.now().weekday()==1:
    with open("quotes.txt") as f:
        x=[q for q in f]
        a=random.choice(x)


    email="aghjkdlahjkdasl;dh@gmail.com"
    password="lhjkadkl;ahjdasdhjl;asdhjk;"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=email,password=password)
        connection.sendmail(from_addr=email,to_addrs="hujiadghjklasd@gmail.com",msg=f"Subject:Monday motivation\n\n{a}")
