import sys
from PyQt4 import QtGui
from probability import count_probability_of_win_selections, single_away_probability, single_draw_probability, single_home_probability
from drawing_chart import horizontal_chart
from get_odds_from_xml import get_xml_data, parsing_xml, input_match_name_by_user, my_xpath_generator, get_id_of_match_based_on_match_name, get_match_result_id_based_on_id_of_match, get_id_of_home_result_based_on_match_result_id, get_odd_of_home_win, get_id_of_draw_result_based_on_match_result_id, get_odd_of_draw, get_id_of_away_result_based_on_match_result_id

class MyWidget(QtGui.QWidget):
    def __init__(self):
        super(MyWidget, self).__init__()
        self.initUI()

    def initUI(self):

        mainLayout = QtGui.QVBoxLayout()

        self.label = QtGui.QLabel("Podaj nazwe meczu, ktory Cie interesuje: ")
        self.edit = QtGui.QLineEdit(self.get_odds_by_match_name())
        button = QtGui.QPushButton("OK")

        mainLayout.addWidget(self.label)
        mainLayout.addWidget(self.edit)
        mainLayout.addWidget(button)

        self.setLayout(mainLayout)
        self.setGeometry(100,100,400,400)

        #podpinamy sygnaly
        button.clicked.connect(self.copy_data)

    #metoda kopiujaca i czyszczace dane - gniazdo !
    def copy_data(self):
        txt = self.edit.text()
        self.label.setText(txt)
        self.edit.setText(list)

    def get_odds_by_match_name(self):
        r = get_xml_data("http://xml.cdn.betclic.com/odds_en.xml")
        parsed_xml = parsing_xml(r)
        match_name = input_match_name_by_user()
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
        return [odd_of_home, odd_of_draw, odd_of_away]

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myWidget = MyWidget()
    myWidget.show()
    sys.exit(app.exec_())