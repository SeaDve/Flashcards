import json


class CardStackModel:
    def __init__(self):
        settings = Gio.Settings.new('io.github.seadve.Flashcards')
        self.cardstack_list = list(settings.get_value("cardstack-list"))

    def save_values(self):
        pass

    def new_cardstack(self, title, color):
        pass

    def del_cardstack(self, cardstack):
        pass


    def new_card(self, cardstack, answer, question):
        pass


    def del_card(self, cardstack, card):
        pass



        
