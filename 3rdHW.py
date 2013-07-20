import os,time,string
c1='cd "C:/Users/Administrator/Desktop/Git"','git init','git add -A','git commit -m \'%s\'' % time.strftime('%Y-%m-%d-%H:%M:%S',time.localtime(time.time())),'git pull origin master'

print(len(c1))
cm=' && '.join(c1)
print(cm)
if os.system(cm)!=0 :  
    print (' ---- 执行命令失败 [%s]----' % cm )
