from gi.repository import Gio, GLib

class CardStackModel:
    def __init__(self):
        self.settings = Gio.Settings.new('io.github.seadve.Flashcards')
        self.cardstack_list = list(self.settings.get_value("cardstack-list"))

    def save_values(self):
        self.settings.set_value("cardstack-list", GLib.Variant('aa{sv}', self.cardstack_list))

    def new_cardstack(self, title, color):
        self.cardstack_list.append(
            {
                "title": title,
                "color": color,
                "cards": []
            }
        )

    def del_cardstack(self, cardstack):
        del self.cardstack_list[cardstack]


    def new_card(self, cardstack, answer, question):
        self.cardstack_list[cardstack]["cards"].append(
            {
                "answer": answer,
                "question": question
            }
        )


    def del_card(self, cardstack, card):
        del self.cardstack_list[cardstack][card]



        
