user_day = int(input('Enter Day:'))
user_month = int(input('Enter Month:'))
user_year = int(input('Enter Year:'))

current_year = int(input('Enter current Day:'))
current_month = int(input('Enter current Month:'))
current_day = int(input('Enter current Year:'))

year_result = (current_year - user_year) - 1
month_result = 12 - (user_month - current_month)
day_result = current_day - user_day

print('User is', year_result,'years,', month_result,'months, and',day_result,'days old')
