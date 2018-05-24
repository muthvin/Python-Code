import re
from collections import Counter

#input = r"C:\Muthu\Working\DeviceLogs\Logs\ndm_V1.log"
input = r"C:\Users\vinod.muthu\Desktop\a3.txt"

#important = []
#keep_phrase = [".py"]

with open(input) as f:
    f = f.readlines()

for line in f:
    #m = re.match(r'^\s\s\s(."Hash Value")', line)
    m = re.match(r'.*(Add to expect_queue:)(.*)', line)
    if m:
        print (m.group(2))
        
      
    #m = re.match(r'.*\s(.*.py.*?).*',line)
    #if m:
        #important.append(m.group(1))

#print (Counter(important))
#important = set(important)

        
        

    
    
