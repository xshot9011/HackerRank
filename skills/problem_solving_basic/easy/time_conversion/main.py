def timeConversion(s):
  hr = int(s[:2])
  day = s[8:10]
  return '{:02d}:{}'.format(hr+12 if day=='PM' and hr<12 else hr-12 if day=='AM' and hr==12 else hr, s[3:8])
