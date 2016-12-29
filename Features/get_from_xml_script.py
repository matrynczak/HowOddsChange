import requests
import libxml2
import urllib2
import lxml
#
# feed = requests.get("http://xml.cdn.betclic.com/odds_en.xml")
# content = feed.content
# print content
# if 'id="26796969"'  in  content:
#     print True
# else:
# #     print False
#
#
# from xml.dom    import  minidom
# from xml.dom.minidom import parse
# # xmldoc = minidom.parse('/home/mateusz/odds_en.xml')
# # childs = xmldoc.childNodes
# xml_doc = minidom.parse("/home/mateusz/odds_en.xml")
# print xml_doc.toxml()
# nodes = xml_doc.childNodes
# bet = nodes[0].getElementsByTagName('bet')[1]
# print nodes[0].getElementsByTagName('bet')[1]
# # match = xmldoc.('id="194882934"')
# # print match
#
# import re





# parsed_content = json.loads(content)
# print parsed_content

feed = urllib2.urlopen("http://xml.cdn.betclic.com/odds_en.xml").read()
print feed
print len(feed)


# feed_xml = feed.etree.ElementTree.parse("http://xml.cdn.betclic.com/odds_en.xml")
# root = feed_xml.getroot()

# soup = BeatifulSoup.BeatifulSoup(feed)
#
# aaa = soup.find_all('match')
# for matches in aaa:
#     print matches

#print content
# print feed_parsed








