import pickle
with open('entry.pickle', 'rb') as f:  
    entry = pickle.load(f)              
entry                                   
# {'comments_link': None,
#  'internal_id': b'\xDE\xD5\xB4\xF8',
#  'title': 'Dive into history, 2009 edition',
#  'tags': ('diveintopython', 'docbook', 'html'),
#  'article_link':
#  'http://diveintomark.org/archives/2009/03/27/dive-into-history-2009-edition',
#  'published': True}
print(entry)