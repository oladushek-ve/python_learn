import locale
from datetime import datetime
from datetime import date
from datetime import time
from datetime import timedelta

print('date')
d1 = date(2019, 11, 25)
print(f'{d1}\n'
      f'{d1.year}\n'
      f'{d1.month}\n'
      f'{d1.day}\n')

print('time')
t1 = time(3, 1, 20, 2321)
print(f'{t1}\n'
      f'{t1.hour}\n'
      f'{t1.minute}\n'
      f'{t1.second}\n'
      f'{t1.microsecond}')

print('today')
print(str(date.today()) + '\n')

print('max and min')
print(f'{date.max}\n'
      f'{date.min}\n'

      f'{time.max}\n'
      f'{time.min}\n'

      f'{datetime.max}\n'
      f'{datetime.min}\n')

print('datetime')
dt = datetime(2001, 6, 30, 6, 30, 22)
print(f'{dt}\n'
      f'{dt.year}\n'
      f'{dt.month}\n'
      f'{dt.day}\n'
      f'{dt.hour}\n'
      f'{dt.minute}\n'
      f'{dt.second}\n')

print('now')
now = datetime.now()
print(f'{now}\n')

print('new datetime')
new_dt = now.replace(hour=now.hour + 4)
print(f'{new_dt}\n')

print('parsing')
dt = datetime.strptime('10/6/2017', '%d/%m/%Y')
print(dt)
dt = datetime.strptime('19/12/2013, 12:30', '%d/%m/%Y, %H:%M')
print(dt)
dt = datetime.strptime('11-11-2019, 19-34', '%d-%m-%Y, %H-%M')
print(dt)

print('\nlocal')
locale.setlocale(locale.LC_ALL, '')
dtrus = datetime.now()
dtr = dtrus.strftime('%d-%b-%Y (%a)')
print(dtr)
dtr1 = dtrus.strftime('%d-%B-%Y (%A)')
print(dtr1)

print('\ndelta')
delta1 = timedelta(days=3, hours=10, minutes=12)
print(delta1)
delta2 = timedelta(days=2, hours=7, minutes=6)
print(delta1 - delta2)
print(delta2 - delta1)

print('\nmy birthday\n')
my_birth = date(2001, 6, 30)
delta = date.today() - my_birth
print(delta)
my_age = int(delta.days / 365)
print(f'My age is {my_age}')

print('\ndasha birthday\n')
dasha_birth = date(2002, 8, 24)
delta_d = date.today() - dasha_birth
print(delta_d)
dasha_age = int(delta.days / 365)
print(f'Dasha age is {dasha_age}')
