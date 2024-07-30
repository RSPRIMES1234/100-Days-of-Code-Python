##################### Extra Hard Starting Project ######################
import smtplib
import pandas as pd
import random
import datetime as dt

email="hjkl;adwl;hjkadsl;ahjkds@gmail.com"
password="hjkladhjadhjklasd"

bday=False


# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
def bday_sender(name,email_receiver):
    letter_text=""
    let_num=random.randint(1,3)
    with open(f"./letter_templates/letter_{let_num}.txt") as f:
        for _ in f:
            _=_.replace("[NAME]",name)
            letter_text+=_
# 4. Send the letter generated in step 3 to that person's email address.
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=email,password=password)
        connection.sendmail(from_addr=email,to_addrs=email_receiver,msg=f"Subject:Happy Birthday\n\n{letter_text}")
# 1. Update the birthdays.csv
# def add_bday(name,email,year,month,date):
#     l=locals()
#     print(l)
#     a=""
#     for _ in l:
#         a+=(str(l[_])+",")
#     a+="\n"
#     print(a)
#     with open("birthdays.csv",'a') as f:
#
#         f.write(a)
# add_bday("rohit","rsprimes86@gmail.com","2002","10","1")


# 2. Check if today matches a birthday in the birthdays.csv
now=dt.datetime.now()
df=pd.read_csv("birthdays.csv")

for _ in range(len(df.index)):
    day=int(df.iloc[_]["day"])
    month=int(df.iloc[_]["month"])
    name=df.iloc[_]["name"]
    email_receiver=df.iloc[_]["email"]
    if day==now.day and month==now.month:
        bday_sender(name,email_receiver)





