#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import tostring
import json
import sys

workflowConfig = {
      'user.name' : 'novaya',
      'oozie.use.system.libpath' : 'True',
      'nameNode' : 'hdfs://nameservice1',
      'jobTracker' : 'yarnRM',
      'oozie.wf.application.path' : 'hdfs://nameservice1/user/novaya/oozie/workspaces/hue-oozie-1491563708.01',
      'security_enabled' : 'False',
      'target_date' : 'targetDate',
      'oos_date' : 'oosDate',
      'DB_KEY' : 'pda-full-analytics',
      'TargetPath' : '/user/novaya/shuyuCDM_camp31/camp_zone_pc',
      'RUN_DATE': sys.argv[1]+'-'+sys.argv[2]+'-'+sys.argv[3]
  }
root = ET.Element("configuration")
# property = ET.SubElement(root, "property")
# ET.SubElement(property, "field1", name="blah").text = "some value1"
# ET.SubElement(property, "field2", name="asdfasd").text = "some vlaue2"
for key, value in workflowConfig.items():
    property = ET.SubElement(root, "property")
    ET.SubElement(property, 'name').text = key
    ET.SubElement(property, 'value').text = value

tree = ET.ElementTree(root)
tree.write("filename.xml")


urlStartJob = 'http://10.10.129.141:11000/oozie/v1/jobs?action=start'
headers = {'Content-Type': 'application/xml'}

r = requests.post(urlStartJob, data=ET.tostring(tree.getroot()), headers=headers)
r.status_code

jobId = json.loads(r.text)['id']
urlGetStatusJob = f"http://10.10.129.141:11000/oozie/v1/job/{jobId}"
r2 = requests.get(urlGetStatusJob)
print(json.loads(r2.text)['status'])


# <configuration><doc><field1 name="blah">some value1</field1><field2 name="asdfasd">some vlaue2</field2></doc></configuration>


