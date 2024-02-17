from datetime import *

yesterday = date.today() - timedelta(days = 1)
today = date.today()
tommorow = date.today() + timedelta(days = 1)

print(yesterday,",", today,",", tommorow) #2024-02-16 2024-02-17 2024-02-18