from lxml import etree
import  requests


def get_xml_data(xml):
    r = requests.get(xml)
    return  r


def parsing_xml(data):
    xml_parsed = etree.XML(data.content)
    return xml_parsed


def number_of_match_xpath(xml):
    number_of_matches = xml.xpath('count(//sport[@id=\'1\']//bet[@code=\'Ftb_Mr3\'])')
    return number_of_matches


def get_list_of_matches(number_of_matches, xml_parsed):
    list_of_matches_name = []
    for x in range(1, int(number_of_matches)):
        list_of_matches_name.append(xml_parsed.xpath("//sport[@id='1']//match")[int(x)].attrib['name'])
    return list_of_matches_name


def search_match_name_by_team_in_list_of_matches(team_name, list_of_matches_name):
    found_matches = []
    for match_name in list_of_matches_name:
        if match_name.find(team_name)  !=  -1:
            found_matches.append(match_name)
    return found_matches


def chose_proper_match_from_list_of_matching_matches(list_of_matches):
    max_of_list_of_matches = len(list_of_matches)+1
    if len(list_of_matches)>1:
        for i, match in zip(range(1, max_of_list_of_matches), list_of_matches):
                print ('{0}. {1}'.format(i, match))
        number_of_match = raw_input('Wpisz numer meczu, ktory miales na mysli: ')
        int_number_of_match = int(number_of_match)
        selected_match = list_of_matches[int_number_of_match-1]
    else:
        selected_match = list_of_matches[0]
    return selected_match


def my_xpath_generator(match_name):
    my_xpath = "//sport[@id='1']//match[@name=" + "'" + str(match_name) + "'" +  "]"
    return my_xpath


def get_id_of_match_based_on_match_name(xml_parsed, my_xpath):
    id_of_match = xml_parsed.xpath(my_xpath)[0].attrib['id']
    return id_of_match


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


def input_team_by_user():
    team_name = raw_input('Podaj nazwe druzyny lub wpisz \'stop\' by zakonczyc dzialanie programu:')
    return team_name


def probability_of_win(home_odd, draw_odd, away_odd):
    prob_home = round(1/float(home_odd) * 100, 1)
    prob_draw = round(1/float(draw_odd) * 100, 1)
    prob_away = round(1/float(away_odd) * 100, 1)
    return  [prob_home, prob_draw, prob_away]


def single_home_probability(prob):
    home_prob = prob[0]
    return home_prob


def single_draw_probability(prob):
    draw_prob = prob[1]
    return draw_prob


def single_away_probability(prob):
    away_prob = prob[2]
    return away_prob


def get_home_name(match_name):
    home_name_list = match_name.split('-')[0]
    home_name = home_name_list.replace('"',"")
    return home_name


def get_away_name(match_name):
    home_name_list = match_name.split('-')[1]
    away_name = home_name_list.replace('"',"")
    return away_name


def single_home_odd(all_odds):
    home_odd = all_odds[0]
    return home_odd


def single_draw_odd(all_odds):
    draw_odd = all_odds[1]
    return draw_odd


def single_away_odd(all_odds):
    away_odd = all_odds[2]
    return away_odd


def home_goals(home_prob):
    if home_prob > 90:
        home_goal = 3
    elif 75 < home_prob <= 90:
        home_goal = 2
    # elif 50 < home_prob <= 75:
    #     home_goal = 2
    elif 30 < home_prob <= 75:
        home_goal = 1
    else:
        home_goal = 0
    return home_goal


def away_goals(away_prob):
    if away_prob > 90:
        away_goal = 3
    elif 75 < away_prob <= 90:
        away_goal = 2
    # elif 50 < away_prob <= 75:
    #     away_goal = 2
    elif 30 < away_prob <= 75:
        away_goal = 1
    else:
        away_goal = 0
    return away_goal

