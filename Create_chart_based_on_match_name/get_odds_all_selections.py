from get_odds_from_xml import get_xml_data, parsing_xml, my_xpath_generator, get_id_of_match_based_on_match_name, get_match_result_id_based_on_id_of_match, get_id_of_home_result_based_on_match_result_id, get_odd_of_home_win, get_id_of_draw_result_based_on_match_result_id, get_odd_of_draw, get_id_of_away_result_based_on_match_result_id


def input_match_name_by_user():
    name_of_match = raw_input('Podaj mecz, ktory Cie interesuje (w formacie X - X) lub wpisz STOP, by zakonczyc dzialanie programu:')
    return name_of_match

def get_odds_by_match_name(match_name):
    r = get_xml_data("http://xml.cdn.betclic.com/odds_en.xml")
    parsed_xml = parsing_xml(r)
    # match_name = input_match_name_by_user()
    my_xpath = my_xpath_generator(match_name)
    id_of_match = get_id_of_match_based_on_match_name(parsed_xml, my_xpath)
    id_of_match_result = get_match_result_id_based_on_id_of_match(parsed_xml, id_of_match)
    id_of_home = get_id_of_home_result_based_on_match_result_id(parsed_xml, id_of_match_result)
    odd_of_home = get_odd_of_home_win(parsed_xml, id_of_home)
    id_of_draw = get_id_of_draw_result_based_on_match_result_id(parsed_xml, id_of_match_result)
    odd_of_draw = get_odd_of_draw(parsed_xml, id_of_draw)
    id_of_away = get_id_of_away_result_based_on_match_result_id(parsed_xml, id_of_match_result)
    odd_of_away = get_odd_of_draw(parsed_xml, id_of_away)
   # return  "Home:" + odd_of_home + " Draw:" + odd_of_draw + " Away:" + odd_of_away
    return  [odd_of_home, odd_of_draw, odd_of_away]

def single_home_odd(all_odds):
    home_odd = all_odds[0]
    return home_odd

def single_draw_odd(all_odds):
    draw_odd = all_odds[1]
    return draw_odd

def single_away_odd(all_odds):
    away_odd = all_odds[2]
    return away_odd

def get_home_name(match_name):
    home_name_list = match_name.split('-')[0]
    home_name = home_name_list.replace('"',"")
    return home_name

def get_away_name(match_name):
    home_name_list = match_name.split('-')[1]
    away_name = home_name_list.replace('"',"")
    return away_name



