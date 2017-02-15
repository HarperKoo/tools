#!/usr/bin/python3
import json
from pprint import pprint

jstr = {  
   'house':{  
      'amount':'$0.00',
      'id':1,
      'value':0.0
   },
   'event':'12.199.136.146',
   'location':'',
   'language':{  
      'language_name':'English',
      'language_id':1,
      'language_symbol':None
   },
   'percentage':1.0,
   'identification':'',
   'source':{  
      'name':'john',
      'id':-1
   },
   'paid':{  
      'amount':'$0.00',
      'format':1,
      'value':0.0
   },
   'score':None
}

data_str = json.dumps(jstr)
data = json.loads(data_str)
pprint(data)


def replaceNone(data_dict,v,rv):
	for key in data_dict.keys():
		if data_dict[key] == v:
			data_dict[key] = rv
		elif type(data_dict[key]) is dict:
			replaceNone(data_dict[key],v,rv)


replaceNone(data,None,"")
pprint(data)


