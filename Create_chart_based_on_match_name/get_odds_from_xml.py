from lxml import etree
import  requests

def get_xml_data(xml):
    r = requests.get(xml)
    return  r

def parsing_xml(data):
    xml_parsed = etree.XML(data.content)
    return xml_parsed

def number_of_match_xpath(xml,xpath):
    number_of_matches = xml.count(xpath)
    return number_of_matches

def my_xpath_generator(match_name):     #function creates xpath with id's which user should declare
    my_xpath = "//sport[@id='1']//match[@name=" + "'" + str(match_name) + "'" + "]"
    return my_xpath

# try:
def get_id_of_match_based_on_match_name(xml_parsed, my_xpath):
    id_of_match = xml_parsed.xpath(my_xpath)[0].attrib['id']
    return id_of_match
# except:
#     print "Prosze podac prawidlowa nazwe druzyny"

def get_match_result_id_based_on_id_of_match(xml_parsed, id_of_match):
    match_result_id = xml_parsed.xpath("//sport[@id='1']//match[@id=" + str(id_of_match) + "]//bet[@name='Match Result']")[0].attrib['id']
    return match_result_id

def get_id_of_home_result_based_on_match_result_id(xml_parsed, match_result_id):
    id_of_home = xml_parsed.xpath("//sport[@id='1']//bet[@id=" + str(match_result_id) + "]/choice[@name='%1%']")[0].attrib['id']
    return  id_of_home

def get_id_of_draw_result_based_on_match_result_id(xml_parsed, match_result_id):
    id_of_draw = xml_parsed.xpath("//sport[@id='1']//bet[@id=" + str(match_result_id) + "]/choice[@name='Draw']")[0].attrib['id']
    return  id_of_draw

def get_id_of_away_result_based_on_match_result_id(xml_parsed, match_result_id):
    id_of_away = xml_parsed.xpath("//sport[@id='1']//bet[@id=" + str(match_result_id) + "]/choice[@name='%2%']")[0].attrib['id']
    return  id_of_away

def get_odd_of_home_win(xml_parsed, id_of_home):
    odd_of_home_win = xml_parsed.xpath("//sport[@id='1']//choice[@id=" + str(id_of_home) + "]")[0].attrib['odd']
    return odd_of_home_win

def get_odd_of_draw(xml_parsed, id_of_draw):
    odd_of_draw = xml_parsed.xpath("//sport[@id='1']//choice[@id=" + str(id_of_draw) + "]")[0].attrib['odd']
    return odd_of_draw

def get_odd_of_away_win(xml_parsed, id_of_away):
    odd_of_away_win = xml_parsed.xpath("//sport[@id='1']//choice[@id=" + str(id_of_away) + "]")[0].attrib['odd']
    return odd_of_away_win

def number_of_match_xpath(xml):
    number_of_matches = xml.xpath('count(//sport[@id=\'1\']//bet[@code=\'Ftb_Mr3\'])')
    return number_of_matches
