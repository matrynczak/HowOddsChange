from drawing_chart import horizontal_chart
from all_functions_to_chart_by_team_name import  *
def get_data_from_xml():
    r = get_xml_data("http://xml.cdn.betclic.com/odds_en.xml")
    parsed_xml = parsing_xml(r)
    return parsed_xml

def get_match_name_from_xml_by_team_name(parsed_xml, team_name):
    num = number_of_match_xpath(parsed_xml)
    list_of_matches_prev = get_list_of_matches(num, parsed_xml)
    list_of_matches = search_match_name_by_team_in_list_of_matches(team_name, list_of_matches_prev)
    match = chose_proper_match_from_list_of_matching_matches(list_of_matches)
    return match

def get_odds_by_match_name(match_name, parsed_xml):
    my_xpath = my_xpath_generator(match_name)
    id_of_match = get_id_of_match_based_on_match_name(parsed_xml, my_xpath)
    id_of_match_result = get_match_result_id_based_on_id_of_match(parsed_xml, id_of_match)
    id_of_home = get_id_of_home_result_based_on_match_result_id(parsed_xml, id_of_match_result)
    odd_of_home = get_odd_of_home_win(parsed_xml, id_of_home)
    id_of_draw = get_id_of_draw_result_based_on_match_result_id(parsed_xml, id_of_match_result)
    odd_of_draw = get_odd_of_draw(parsed_xml, id_of_draw)
    id_of_away = get_id_of_away_result_based_on_match_result_id(parsed_xml, id_of_match_result)
    odd_of_away = get_odd_of_draw(parsed_xml, id_of_away)
    return [odd_of_home, odd_of_draw, odd_of_away]

def drawing_chart(match_name, odds):
    home_name = get_home_name(match_name)
    away_name = get_away_name(match_name)
    home_odd = single_home_odd(odds)
    draw_odd = single_draw_odd(odds)
    away_odd = single_away_odd(odds)
    prob = probability_of_win(home_odd, draw_odd, away_odd)
    home_prob = single_home_probability(prob)
    draw_prob = single_draw_probability(prob)
    away_prob = single_away_probability(prob)
    number_home_goals = home_goals(home_prob)
    number_away_goals = away_goals(away_prob)
    chart = horizontal_chart(home_prob, draw_prob, away_prob, home_name, away_name, number_home_goals, number_away_goals)


