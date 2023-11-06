'''day in year'''
month=int(input('month: '))
day=int(input('day: '))
if month<7:
    days_month=month*31
elif month>=7 and month<10:
    days_month=(month-6)*30 + (6*31)
else:
    days_month=(month-9)*29+ (6*31) +(3*30)
all_days=days_month+day
print(all_days)