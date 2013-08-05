#!/usr/bin/python



import xml.etree.ElementTree as et



def _parseXML(root, deep = 0, max_deep = 30):
	if deep >= max_deep :
		return None

	data = {
		".tag"	: root.tag	,
		".attr"	: root.attrib	,
		".text"	: root.text	,
		".tags"	: set()
	}

	for child in root:
		tag = child.tag
		if tag not in data[".tags"]:
			data[".tags"].add(tag)
			data[tag] = []

		data[tag].append( _parseXML(child, deep + 1) )

	return data



def simpleXML(source, source_is_file = True):
	if source_is_file :
		root = et.parse(source).getroot()
	else:
		root = et.fromstring(source)
		
	return _parseXML(root)



if __name__ == "__main__" :
	xml = """\
	<countries>
		<country code='AT' eu="yes">Austria</country>
		<country code='BG' eu="yes">Bulgaria</country>
		<country code='DE' eu="yes">Germany</country>
		<country>USSR</country>
		<country code='US' />

		<version>1.2.4</version>
	</countries>
	"""

	data = simpleXML(xml, False)

	print data
	print

	print data["version"][0]
	print data["country"][0]
	print

	for item in data["country"]:
		print "%-8s %-20s %-3s" % ( item[".attr"].get("code"), item[".text"], item[".attr"].get("eu", "no") )

