from get_odds_all_selections import get_odds_by_match_name, single_draw_odd, single_home_odd, single_away_odd, input_match_name_by_user, get_away_name, get_home_name
from probability import single_away_probability, single_draw_probability, single_home_probability, probability_of_win
from drawing_chart import horizontal_chart

text = 'STOP'
value = True

while value:

    match_name = input_match_name_by_user()
    if match_name != text:
        home_name = get_home_name(match_name)
        away_name = get_away_name(match_name)
        all_odds = get_odds_by_match_name(match_name)
        home_odd = single_home_odd(all_odds)
        draw_odd = single_draw_odd(all_odds)
        away_odd = single_away_odd(all_odds)
        prob = probability_of_win(home_odd, draw_odd, away_odd)
        home_prob = single_home_probability(prob)
        draw_prob = single_draw_probability(prob)
        away_prob = single_away_probability(prob)
        chart = horizontal_chart(home_prob, draw_prob, away_prob, home_name, away_name)
    else:
        print "Dzieki za skorzystanie z programu!"
        break


