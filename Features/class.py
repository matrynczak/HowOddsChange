from lxml import etree
import requests


def input_match_name_by_user():
    name_of_match = raw_input('Podaj mecz, ktory Cie interesuje (w formacie "X - X"):')
    return name_of_match

def get_xml_data():
    feed = requests.get('http://xml.cdn.betclic.com/odds_en.xml')
    return feed

class get_odd_of_selection(object):

    def __init__(self, name_of_match, feed_xml):
        self.name_of_match = name_of_match
        self.feed_xml = feed_xml

    def parsing_xml(self):
        xml_parsed = etree.XML(self.feed_xml.content)
        return xml_parsed

    def my_xpath_generator(self):  # function creates xpath with id's which user should declare
        my_xpath = "//sport[@id='1']//match[@name=" + str(self.name_of_match) + "]"
        return my_xpath

    # try:
    def get_id_of_match_based_on_match_name(xml_parsed, my_xpath):
        id_of_match = xml_parsed.xpath(my_xpath)[0].attrib['id']
        return id_of_match

    # except:
    #     print "Prosze podac prawidlowa nazwe druzyny"


    def get_match_result_id_based_on_id_of_match(xml_parsed, id_of_match):
        match_result_id = \
        xml_parsed.xpath("//sport[@id='1']//match[@id=" + str(id_of_match) + "]//bet[@name='Match Result']")[0].attrib[
            'id']
        return match_result_id

    def get_id_of_home_result_based_on_match_result_id(xml_parsed, match_result_id):
        id_of_home = \
        xml_parsed.xpath("//sport[@id='1']//bet[@id=" + str(match_result_id) + "]/choice[@name='%1%']")[0].attrib['id']
        return id_of_home

    def get_id_of_draw_result_based_on_match_result_id(xml_parsed, match_result_id):
        id_of_draw = \
        xml_parsed.xpath("//sport[@id='1']//bet[@id=" + str(match_result_id) + "]/choice[@name='Draw']")[0].attrib['id']
        return id_of_draw

    def get_id_of_away_result_based_on_match_result_id(xml_parsed, match_result_id):
        id_of_away = \
        xml_parsed.xpath("//sport[@id='1']//bet[@id=" + str(match_result_id) + "]/choice[@name='%2%']")[0].attrib['id']
        return id_of_away

    def get_odd_of_home_win(xml_parsed, id_of_home):
        odd_of_home_win = xml_parsed.xpath("//sport[@id='1']//choice[@id=" + str(id_of_home) + "]")[0].attrib['odd']
        return odd_of_home_win

    def get_odd_of_draw(xml_parsed, id_of_draw):
        odd_of_draw = xml_parsed.xpath("//sport[@id='1']//choice[@id=" + str(id_of_draw) + "]")[0].attrib['odd']
        return odd_of_draw

    def get_odd_of_away_win(xml_parsed, id_of_away):
        odd_of_away_win = xml_parsed.xpath("//sport[@id='1']//choice[@id=" + str(id_of_away) + "]")[0].attrib['odd']
        return odd_of_away_win



# def get_odds_by_match_name():       #uses methods of get_odd_of_selection class
#     r = get_odd_of_selection.get_xml_data("http://xml.cdn.betclic.com/odds_en.xml")
#     parsed_xml = get_odd_of_selection.parsing_xml(r)
#     match_name = get_odd_of_selection.input_match_name_by_user()
#     my_xpath = get_odd_of_selection.my_xpath_generator(match_name)
#     id_of_match = get_odd_of_selection.get_id_of_match_based_on_match_name(parsed_xml, my_xpath)
#     id_of_match_result = get_odd_of_selection.get_match_result_id_based_on_id_of_match(parsed_xml, id_of_match)
#     id_of_home = get_odd_of_selection.get_id_of_home_result_based_on_match_result_id(parsed_xml, id_of_match_result)
#     odd_of_home = get_odd_of_selection.get_odd_of_home_win(parsed_xml, id_of_home)
#     id_of_draw = get_odd_of_selection.get_id_of_draw_result_based_on_match_result_id(parsed_xml, id_of_match_result)
#     odd_of_draw = get_odd_of_selection.get_odd_of_draw(parsed_xml, id_of_draw)
#     id_of_away = get_odd_of_selection.get_id_of_away_result_based_on_match_result_id(parsed_xml, id_of_match_result)
#     odd_of_away = get_odd_of_selection.get_odd_of_draw(parsed_xml, id_of_away)
#     return  "Home:" + odd_of_home + " Draw:" + odd_of_draw + " Away:" + odd_of_away

match_name = input_match_name_by_user()
feed =  get_xml_data()
match1 = get_odd_of_selection(match_name, feed)
parsed_xml = match1.parsing_xml()
my_xpath = get_odd_of_selection.my_xpath_generator(match_name)
id_of_match = get_odd_of_selection.get_id_of_match_based_on_match_name(parsed_xml, my_xpath)
id_of_match_result = get_odd_of_selection.get_match_result_id_based_on_id_of_match(parsed_xml, id_of_match)
id_of_home = get_odd_of_selection.get_id_of_home_result_based_on_match_result_id(parsed_xml, id_of_match_result)
odd_of_home = get_odd_of_selection.get_odd_of_home_win(parsed_xml, id_of_home)
id_of_draw = get_odd_of_selection.get_id_of_draw_result_based_on_match_result_id(parsed_xml, id_of_match_result)
odd_of_draw = get_odd_of_selection.get_odd_of_draw(parsed_xml, id_of_draw)
id_of_away = get_odd_of_selection.get_id_of_away_result_based_on_match_result_id(parsed_xml, id_of_match_result)
odd_of_away = get_odd_of_selection.get_odd_of_draw(parsed_xml, id_of_away)
# return  "Home:" + odd_of_home + " Draw:" + odd_of_draw + " Away:" + odd_of_away
