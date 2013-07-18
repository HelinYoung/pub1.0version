#import string#http://www.pythonchallenge.com/pc/def/peak.html
# x=["m","q","g"]
# y="g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.map"
# print(y)
# table=str.maketrans("abcdefghijklmnopqrstuvwxyz", "cdefghijklmnopqrstuvwxyzab")
# print(table)
# print (y.translate(table))
# import re
# pattern = re.compile(r'([^A-Z])([A-Z]{3})([a-z])([A-Z]{3})([^A-Z])')#(r'([A-Za-z])+')
# # 使用Pattern匹配文本，获得匹配结果，无法匹配时将返回None
# match = pattern.findall('''

# ''')
# if match:
#     print (match)
# i=0
# print(len(match),match[0][2])
# while i < len(match):
#     if i==0:#res 不能直接用+=运算
#         res=match[i][2]
#     else :
#         res+=match[i][2]
#     print(i)
#     i+=1
# print(res)
# import urllib.request ,re ,time
# uri="http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%s"
# nothing_rep =re.compile(r'and the next nothing is (\d+)')
# number=16044/2
# nothing =str(number)
# print(nothing_rep.findall('and the next nothing is 44827'))
# while 1:
#     try:
#         fp =urllib.request.urlopen(uri % nothing)
#         bsource=fp.read()
#         print(bsource)#the source is read as HTML bytes
#         strsource=bsource.decode("utf8")   
#         print(strsource) 
#         nothing = nothing_rep.search (strsource).group(1)
#         print (nothing)
#     except :
#          break
# import pickle,urllib.request
# fp=urllib.request.urlopen("http://www.pythonchallenge.com/pc/def/banner.p")
# result=pickle.load(fp)
# fp.close()
# line=''
# for n in result:
#   line=''
#   for m in n:
#       line+= m[0]*m[1]
#   print (line)
# import urllib.request, zipfile, re, collections
# o, n, f = [], "90052", "%s.txt"
# nnr = re.compile(r'Next nothing is (\d+)')

# file = zipfile.ZipFile("channel.zip")
# while True:
#     try:
#         btemp=file.read(f % n)
#         strtemp=btemp.decode("utf8")  
#         n = nnr.search(strtemp).group(1)
#     except:
#         print (file.read(f % n))
#         break
#     print(n)
#     o.append(file.getinfo(f % n).comment.decode('utf8'))
# print (''.join(o))
# import re, image

# i = Image.open("oxygen.png") # http://www.pythonchallenge.com/pc/def/oxygen.png
# row = [i.getpixel((x, 45)) for x in range(0, i.size[0], 7)]
# ords = [r for r, g, b, a in row if r == g == b]

# print ("".join(map(chr, map(int, re.findall("\d+", "".join(map(chr, ords)))))))
# import time
# import pickle
# entry = {}          
# entry['title'] = 'Dive into history, 2009 edition'
# entry['article_link'] = 'http://diveintomark.org/archives/2009/03/27/dive-into-history-2009-edition'
# entry['comments_link'] = None
# entry['internal_id'] = b'\xDE\xD5\xB4\xF8'
# entry['tags'] = ('diveintopython', 'docbook', 'html')
# entry['published'] = True

# entry['published_date'] = time.strptime('Fri Mar 27 22:20:42 2009') 


# with open('entry.pickle','wb') as f:
#     pickle.dump(entry,f)
# import pickle
# with open('entry.pickle', 'rb') as f:  
#     entry = pickle.load(f)              
# entry                                   
# # {'comments_link': None,
# #  'internal_id': b'\xDE\xD5\xB4\xF8',
# #  'title': 'Dive into history, 2009 edition',
# #  'tags': ('diveintopython', 'docbook', 'html'),
# #  'article_link':
# #  'http://diveintomark.org/archives/2009/03/27/dive-into-history-2009-edition',
# #  'published': True}
# print(entry)
import bz2
if __name__ == '__main__':
    un = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'  
    pw = b'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08' 
    print(bz2.decompress(un))
    print(bz2.decompress(pw))#需要这里的pw un 参数是byte型

