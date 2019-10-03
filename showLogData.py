import datetime
import time

def printLogData(temp):
	print("#",datetime.datetime.now(),"# :" ,temp)
	time.sleep(0.500)

# app = printLogData()