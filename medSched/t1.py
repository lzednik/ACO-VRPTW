import datetime

svc_dt=datetime.date(2017,3,24)

wd=svc_dt.weekday()

if wd<=4:
    print('weekday')
else:
    print('weekend')
