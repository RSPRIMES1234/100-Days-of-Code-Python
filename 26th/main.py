import random

names=["Alex","beth",'Caroline',"Dave","Eleanor","Freddie"]
a={key:random.randint(1,100) for key in names}
print(a)
new_a={key:value for (key,value) in a.items() if value>33}
print(new_a)
