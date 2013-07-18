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
import pickle,urllib.request
fp=urllib.request.urlopen("http://www.pythonchallenge.com/pc/def/banner.p")
data=pickle.load(fp)
fp.close
# print(data)
for i in data:
    print( "".join([e[1]*e[0] for e in i]))

