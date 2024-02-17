import datetime

today = datetime.datetime.now()
print(today) #2024-02-17 14:44:29.262071
today = str(today)
woutmicro = today.split(".")
print(woutmicro[0]) #2024-02-17 14:44:29