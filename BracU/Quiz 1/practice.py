import math
sec= int(input())
min= sec/60
h = min/60

print(math.floor(h),math.floor(min%60),math.floor(sec%60))