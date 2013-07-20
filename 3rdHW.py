import os,time,string
c1='cd D:/files/study/python','git init','git add -A','git commit -m \'%s\'' % time.strftime('%Y-%m-%d-%H:%M:%S',time.localtime(time.time())),'git pull origin master','git push master origin'

print(len(c1))
i=0
while i <len(c1):
    if os.system(c1[i])!=0 :  
        print (' ---- [%s]----' % c1[i])
    i+=1