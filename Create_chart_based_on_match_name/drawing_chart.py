from pylab import *

def horizontal_chart(home_odd, draw_odd, away_odd, home_name, away_name):
    value = home_odd, draw_odd, away_odd   # the bar lengths
    pos = arange(3)+1.5    # the bar centers on the y axis

#    fig = plt.figure()
    ax = plt.subplot()
 #   ax = fig.add_subplot(-180)
    ax.barh(pos,value, align='center')
    yticks(pos, (home_name, 'Remis', away_name))
    xlabel('Prawdopodobienstwo [%]')
    # ylabel()
    title('Procentowe szanse na wygrana?')
    #grid(True)

    for i, value in enumerate(value):
        ax.text(value - 5.0 , i + 1.45, value, color='white', fontweight='bold', size=14)

    chart = show()
    return chart

#example = horizontal_chart(32.0, 12.0, 45.0)
