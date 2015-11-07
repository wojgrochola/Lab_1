import commands
import time
import sys
import logging
class Info:
    def __init__(self):
      self.logger = logging.getLogger(__name__)
      self.logger.setLevel(logging.INFO)
      
      self.handler = logging.FileHandler('log.txt')
      self.handler.setLevel(logging.INFO)
      
      formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
      self.handler.setFormatter(formatter)
      self.logger.addHandler(self.handler)

    def getCpu(self):
      cpu = commands.getoutput("top -n 1 | grep Cpu")
      return cpu
    
    def getRam(self):
      ram = commands.getoutput('top -n 1 | grep "KiB Mem"')
      return ram

    def getDuo(self):
      info = self.getRam() + "\n\t" + self.getCpu();
      return info
    
    def execute(self, flag):
      print("Program is running with flag: %s. Press CTRL-C or CTRL-Z to stop.\n" % flag)
      if (flag == '-p'):
        func = self.getCpu
      elif (flag == '-r'):
        func = self.getRam
      elif (flag == '-pr'):
        func = self.getDuo
        
      while True:
        self.logger.info(("\n\t" + func()))
  
       
      
      
if __name__ == "__main__":
  info = Info()
  if len(sys.argv) == 2:
    if '-p' == sys.argv[1]:
      info.execute('-p')
    elif '-r' == sys.argv[1]:
      info.execute('-r')                     
    elif '-pr' == sys.argv[1]:
      info.execute('-pr')
    else:
      print ("Use -p or -r.")
  else:
    print ("Invalid use.")