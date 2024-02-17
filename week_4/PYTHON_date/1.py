import datetime

FiveDays = datetime.date.today() - datetime.timedelta(days = 5)
"""
Этот метод создает объект timedelta, который представляет собой продолжительность времени. Здесь мы указываем days=5, что означает пять дней.
"""

print(datetime.timedelta(hours=12)) # 12:00:00
print(datetime.timedelta(days=5)) # 5 days, 0:00:00
print(FiveDays)