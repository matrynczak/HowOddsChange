from complex_functions_to_get_odds_by_team import get_data_from_xml, get_match_name_from_xml_by_team_name, get_odds_by_match_name, drawing_chart
from all_functions_to_chart_by_team_name import input_team_by_user


text = 'stop'
value = True


while value:
    team_name = input_team_by_user()
    if team_name != text:
        parsed_xml = get_data_from_xml()
        try:
            match = get_match_name_from_xml_by_team_name(parsed_xml, team_name)
        except(IndexError):
            print "Podana nazwa druzyny nie istnieje w bazie. Podaj nazwe jeszcze raz."
            team_name = input_team_by_user()
            match = get_match_name_from_xml_by_team_name(parsed_xml, team_name)

        odds = get_odds_by_match_name(match, parsed_xml)

        chart = drawing_chart(match, odds)
    else:
        print "Dzieki za skorzystanie z programu!"
        break
