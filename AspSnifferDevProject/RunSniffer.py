from SnifferBase import*
import os.path
import time as t

mod_time = os.path.getctime("test7.txt")
print(t.strftime("%d.%m.%Y %H:%M:%S",t.localtime(mod_time)))




obj = SnifferBase()
#obj.openLogFile()




#obj.printActivity("Moving file...")
#try:
#	os.rename("test3.txt", "test7.txt")
#except BaseException as e:
#	obj.printActivity("Failed to move " + str(e))
#else:
#	obj.printActivity("OK")
'''
obj.printActivity('------bacho viko from here-----')

obj.buffRawHex.seek(0)
for line in obj.buffRawHex:
	obj.printActivity(line)'''
