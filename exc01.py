#!/usr/bin/env python
 
import sys, time, commands, logging
from daemon import Daemon





class MyDaemon(Daemon):
		def __init__(self, filePath):
			Daemon.__init__(self, filePath)
			FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
			logging.basicConfig(filename='log.txt', level=logging.INFO, format=FORMAT)
		
		def run(self):
				while True:
					self.execute()
					time.sleep(30)

		def usageInfo(self):
			print "usage: %s start -flag" % sys.argv[0]
			print ("Available flags:\n\t-p - log CPU usage\n\t-r \tlog RAM usage\n\t-pr  log CPU and RAM usage.\n")
			sys.exit(2)


		def getCpu(self):
			cpu = commands.getoutput("top -n 1 | grep Cpu")
			return cpu
	
		def getRam(self):
			memTotal = float(commands.getoutput('cat /proc/meminfo | grep MemTotal').split()[1])
			memFree =  float(commands.getoutput('cat /proc/meminfo | grep MemFree').split()[1])
			memProc = float ((memFree/memTotal) * 100)
			return str(round(memProc, 2)) + "%"

		def getDuo(self):
			info = "\n\tRam usage: " + self.getRam() + "\n\t" + self.getCpu();
			return info

		def execute(self):
			info = ""
			if (len(sys.argv) == 3):
				flag = sys.argv[2]
				if (flag == '-p'):
					info = self.getCpu()
				elif(flag == '-r'):
					info = self.getRam()
				elif(flag == '-pr'):
					info = self.getDuo()
				else:
					print ("Unkown flag. Exit program.")
					sys.exit(2)
			else:
				self.usageInfo()
			logging.info(info)
			  
	 
if __name__ == "__main__":
		daemon = MyDaemon('/tmp/systemLogger.pid')
		if len(sys.argv) >= 2:
				if 'start' == sys.argv[1]:
						daemon.start()
				elif 'stop' == sys.argv[1]:
						daemon.stop()
				elif 'restart' == sys.argv[1]:
						daemon.restart()
				else:
						print "Unknown command. Use start|stop|restart "
						sys.exit(2)
				sys.exit(0)
		else:
				daemon.usageInfo()