# Kullanıcının Doğum Tarhini Alıp Yaşını Bulan Uygulama

import datetime as dt

birthDay = input("Enter your birthday: (14/02/2003) -> ")
format = "%d/%m/%Y"
birthDay = dt.datetime.strptime(birthDay, format)
today = dt.datetime.now()
result = today - birthDay
print(result)
year = result.days // 365
month = result.days % 365 // 30
day = result.days % 36 % 30
print("Your Age: ", year, "year", month, "month", day, "day")
