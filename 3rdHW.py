import os,time,string
c1='cd Desktop/Git','git init','git add -A','git commit -m \'%s\'' % time.strftime('%Y-%m-%d-%H:%M:%S',time.localtime(time.time())),
'git pull origin master','git push origin'

print(len(c1))
i=0
while i <len(c1):
    print(c1[i])
    if os.system(c1[i])!=0 :  
        pass
    #     print (' ---- 执行命令失败 [%s]----' % c1[i] )
    i+=1