
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

# def count_probability_of_win_selections():
#     all_odds = get_odds_by_match_name()
#     home_odd = single_home_odd(all_odds)
#     draw_odd = single_draw_odd(all_odds)
#     away_odd = single_away_odd(all_odds)
#     prob = probability_of_win(home_odd, draw_odd, away_odd)
#     return prob








