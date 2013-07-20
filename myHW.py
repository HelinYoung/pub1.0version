from PIL import Image
from PIL import ImageDraw
image = Image.open("cave.jpg")
nsize = tuple([int(x / 2) for x in image.size])
odd = even = Image.new(image.mode, nsize)

for x in range(image.size[0]):
    for y in range(image.size[1]):
        if x % 2 == 0 and y % 2 == 0:
            even.putpixel((int(x / 2), int(y / 2)), image.getpixel((x, y)))
        elif x % 2 == 0 and y % 2 == 1:
            odd.putpixel((int(x / 2),int( (y - 1) / 2)), image.getpixel((x, y)))
        elif x % 2 == 1 and y % 2 == 0:
            even.putpixel((int((x - 1) / 2),int( y / 2) ), image.getpixel((x, y)))
        else:
            odd.putpixel((int((x - 1) / 2),int ((y - 1) / 2)), image.getpixel((x, y)))

even.save("even.jpg")
odd.save("odd.jpg")
even.show()
odd.show()


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
# import bz2
# if __name__ == '__main__':
#     un = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'  
#     pw = b'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08' 
#     print(bz2.decompress(un))
#     print(bz2.decompress(pw))#需要这里的pw un 参数是byte型


# from PIL import Image
# from PIL import ImageDraw

# first = [ 146,399,163,403,170,393,169,391,166,386,170,381,170,371,170,355,169,346,167,335,170,329,170,320,170,
# 310,171,301,173,290,178,289,182,287,188,286,190,286,192,291,194,296,195,305,194,307,191,312,190,316,
# 190,321,192,331,193,338,196,341,197,346,199,352,198,360,197,366,197,373,196,380,197,383,196,387,192,
# 389,191,392,190,396,189,400,194,401,201,402,208,403,213,402,216,401,219,397,219,393,216,390,215,385,
# 215,379,213,373,213,365,212,360,210,353,210,347,212,338,213,329,214,319,215,311,215,306,216,296,218,
# 290,221,283,225,282,233,284,238,287,243,290,250,291,255,294,261,293,265,291,271,291,273,289,278,287,
# 279,285,281,280,284,278,284,276,287,277,289,283,291,286,294,291,296,295,299,300,301,304,304,320,305,
# 327,306,332,307,341,306,349,303,354,301,364,301,371,297,375,292,384,291,386,302,393,324,391,333,387,
# 328,375,329,367,329,353,330,341,331,328,336,319,338,310,341,304,341,285,341,278,343,269,344,262,346,
# 259,346,251,349,259,349,264,349,273,349,280,349,288,349,295,349,298,354,293,356,286,354,279,352,268,
# 352,257,351,249,350,234,351,211,352,197,354,185,353,171,351,154,348,147,342,137,339,132,330,122,327,
# 120,314,116,304,117,293,118,284,118,281,122,275,128,265,129,257,131,244,133,239,134,228,136,221,137,
# 214,138,209,135,201,132,192,130,184,131,175,129,170,131,159,134,157,134,160,130,170,125,176,114,176,
# 102,173,103,172,108,171,111,163,115,156,116,149,117,142,116,136,115,129,115,124,115,120,115,115,117,
# 113,120,109,122,102,122,100,121,95,121,89,115,87,110,82,109,84,118,89,123,93,129,100,130,108,132,110,
# 133,110,136,107,138,105,140,95,138,86,141,79,149,77,155,81,162,90,165,97,167,99,171,109,171,107,161,
# 111,156,113,170,115,185,118,208,117,223,121,239,128,251,133,259,136,266,139,276,143,290,148,310,151,
# 332,155,348,156,353,153,366,149,379,147,394,146,399  ]

# second = [ 156,141,165,135,169,131,176,130,187,134,191,140,191,146,186,150,179,155,175,157,168,157,163,157,159,
# 157,158,164,159,175,159,181,157,191,154,197,153,205,153,210,152,212,147,215,146,218,143,220,132,220,
# 125,217,119,209,116,196,115,185,114,172,114,167,112,161,109,165,107,170,99,171,97,167,89,164,81,162,
# 77,155,81,148,87,140,96,138,105,141,110,136,111,126,113,129,118,117,128,114,137,115,146,114,155,115,
# 158,121,157,128,156,134,157,136,156,136  ]

# img = Image.new('RGB', (640, 480))
# draw = ImageDraw.Draw(img)
# draw.line(first)
# draw.line(second)
# img.show()

# import time
# print(time.time())
# print(time.localtime(time.time()))
# print(time.strftime('%Y-%m-%d-%H:%M:%S',time.localtime(time.time())))

# import bz2
# import binascii

# original_data = 'This is the original text.'
# print （'Original     :', len(original_data), original_data）

# compressed = bz2.compress(original_data)
# print （'Compressed   :', len(compressed), binascii.hexlify(compressed)）

# decompressed = bz2.decompress(compressed)
# print （'Decompressed :', len(decompressed), decompressed）
# import re  
  
# if __name__ == '__main__':  
#     counter = 0  

#     def fun(s):  

#         result = '' 
#         char = s[0]  
#         count = 0    

#         for x in s:  
#             if x == char:  
#                 count += 1  
#             else:  
#                 result += str(count) + char  
#                 count = 1  
#                 char = x  
                  
#         result += str(count) + char  
          
#         print(len(result))  
          
#         global counter  

#         counter += 1  
          
#         if counter < 30:  
#             fun(result)  
                  
#     fun('1')  

#     #solution 2 Start  
#     def describe(s):  
#         sets = re.findall("(1+|2+|3+)", s)  

#         return ''.join(str(len(x)) + x[0] for x in sets)

#     s = '1'  
      
#     for dummy in range(30):  
#         s = describe(s)  
          
#     print(len(s)) 