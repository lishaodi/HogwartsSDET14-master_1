from collections import OrderedDict
import json


d=OrderedDict()
d['foo'] = 1
d['bar'] = 2
d['spam'] = 5
d['grok'] = 4   
print(type(d))
print(d)
for key in d:
    print(key, d[key])


c={}
c['foo'] = 1
c['bar'] = 2
c['spam'] = 3
c['grok'] = 4
print(type(c))
print(c)