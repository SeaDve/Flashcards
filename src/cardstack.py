# cardstack.py
#
# Copyright 2021 SeaDve
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from gi.repository import Gtk, Handy, GLib


@Gtk.Template(resource_path='/io/github/seadve/Flashcards/cardstackrow.ui')
class CardStackRow(Handy.ActionRow):
    __gtype_name__ = 'CardStackRow'

    play_button = Gtk.Template.Child()

    def __init__(self, window, cards_list, title, **kwargs):
        super().__init__(**kwargs)

        self.title = title
        self.set_title(self.title)
        self.window = window
        self.listbox = self.window.main_listbox
        self.overlay = self.window.main_overlay
        self.cards_list = cards_list

        self.window.data["cardstack"]
        self.set_subtitle(f"{len(cards_list)} cards")

        self.edit_box = CardStackEdit(self.cards_list)

        self.play_box = CardStack()
        self.play_box.set_question(self.title)

        self.play_button.connect("clicked", self.on_play_button_clicked)
        self.connect("activated", self.on_edit_mode)
        self.window.back_button.connect("clicked", self.on_back_button_clicked)

    def on_play_button_clicked(self, widget):
        self.window.set_play_mode()
        self.window.cardstack_title.set_text(self.title)
        self.overlay.add_overlay(self.play_box)

    def on_edit_mode(self, widget):
        self.window.set_play_mode()
        self.window.cardstack_title.set_text(self.title)
        self.overlay.add_overlay(self.edit_box)

    def on_back_button_clicked(self, widget):
        self.window.unset_play_mode()

        try:
            self.play_box.get_parent().remove(self.play_box)
        except:
            pass

        try:
            self.edit_box.get_parent().remove(self.edit_box)
        except:
            pass



@Gtk.Template(resource_path='/io/github/seadve/Flashcards/cardstack.ui')
class CardStack(Gtk.Box):
    __gtype_name__ = 'CardStack'

    question_label = Gtk.Template.Child()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def set_question(self, question):
        self.question_label.set_label(question)


@Gtk.Template(resource_path='/io/github/seadve/Flashcards/cardstackedit.ui')
class CardStackEdit(Gtk.Box):
    __gtype_name__ = 'CardStackEdit'

    edit_mode_listbox = Gtk.Template.Child()

    def __init__(self, cards_list, **kwargs):
        super().__init__(**kwargs)

        for item in cards_list:
            question_row = Card()
            question_row.set_question(item["question"])
            question_row.set_answer(item["answer"])
            self.edit_mode_listbox.insert(question_row, -1)

        new_card_row = Gtk.ListBoxRow()
        image = Gtk.Image()
        image.set_from_icon_name("list-add-symbolic", 2)
        new_card_row.add(image)
        image.show()
        new_card_row.show()
        self.edit_mode_listbox.insert(new_card_row, -1)


@Gtk.Template(resource_path='/io/github/seadve/Flashcards/card.ui')
class Card(Handy.ExpanderRow):
    __gtype_name__ = 'Card'

    question_entry = Gtk.Template.Child()
    answer_entry = Gtk.Template.Child()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        GLib.timeout_add(500, self.update, priority=GLib.PRIORITY_LOW)

    def set_question(self, question):
        self.question_entry.set_text(question)

    def set_answer(self, answer):
        self.answer_entry.set_text(answer)

    def update(self):
        self.set_subtitle(self.question_entry.get_text())
        self.set_title(self.answer_entry.get_text())
        return True
