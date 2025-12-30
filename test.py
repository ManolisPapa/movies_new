from pandas import Timestamp, to_datetime

a = Timestamp(year=2022, month=12, day=1)
b = Timestamp(year=2023, month=12, day=1)

avg = (a.timestamp() + b.timestamp()) / 2

print(to_datetime(avg, unit='s'))