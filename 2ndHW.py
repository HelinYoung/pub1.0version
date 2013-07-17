# import sys
# print("g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj") 
# print('''
# 	amknsrcpq
# 	''')
# a=sys.getrecursionlimit()
# print(a)
import time
import pickle
entry = {}          
entry['title'] = 'Dive into history, 2009 edition'
entry['article_link'] = 'http://diveintomark.org/archives/2009/03/27/dive-into-history-2009-edition'
entry['comments_link'] = None
entry['internal_id'] = b'\xDE\xD5\xB4\xF8'
entry['tags'] = ('diveintopython', 'docbook', 'html')
entry['published'] = True

entry['published_date'] = time.strptime('Fri Mar 27 22:20:42 2009') 


with open('entry.pickle','wb') as f:
	pickle.dump(entry,f)