import os
import xml.etree.ElementTree as ET
file_name = "test_XML.xml"
# The full path to access the xml file
full_file = os.path.abspath(os.path.join("/data", file_name))

xmltree = ET.parse(full_file)
xmlroot = xmltree.getroot()

for element in root.iter():
  if isinstance(element.tag, str):
    print("%s - %s" % (element.tag, element.text))
  else :
    print("SPECIAL: %s - %s" % (element, element.text))


for element in root.iter(tag=etree.Element):
  print("%s - %s" % (element.tag, element.text))
  
for element in root.iter(tag=etree.Entity):
  print(element.text)

