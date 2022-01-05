#!/usr/bin/python
print ("""
Show a counter down to fireworks from 10 to 0
""")
from time import sleep

for i in range(10,-1,-1):
    if i != 0:
        print(i,"...")
    else:
        print(i," !!!!")
    sleep(1)
print("BUM ")
sleep(1)
print("POW ")
sleep(1)
print("PAH ")