import os,time,string
<<<<<<< HEAD
c1='cd "D:/Users/H.Young/Desktop/Git"','git init','git add -A','git commit -m \'%s\'' % time.strftime('%Y-%m-%d-%H:%M:%S',time.localtime(time.time())),'git pull origin master'
=======
c1='cd "C:/Users/Administrator/Desktop/Git"','git init','git add -A','git commit -m \'%s\'' % time.strftime('%Y-%m-%d-%H:%M:%S',time.localtime(time.time())),'git pull origin master'
>>>>>>> a08d8f99709d80d37634cd4a009ab27975319f9d

print(len(c1))
cm=' && '.join(c1)
print(cm)
if os.system(cm)!=0 :
    print (' ---- 执行命令失败 [%s]----' % cm )
