import re
inp="saad_is,my name;helow:world"
file=open("/home/sadi/Data pre processing FYP/untitled.txt",'r')
sp=str(file.read())
#print(sp)
fin=re.split(sp,inp)
print(fin)