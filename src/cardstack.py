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

from gi.repository import Gtk, Handy


@Gtk.Template(resource_path='/io/github/seadve/Flashcards/cardstackrow.ui')
class CardStackRow(Handy.ActionRow):
    __gtype_name__ = 'CardStackRow'

    play_button = Gtk.Template.Child()

    def __init__(self, window, title, **kwargs):
        super().__init__(**kwargs)

        self.title = title
        self.set_title(self.title)
        self.window = window
        self.listbox = self.window.main_listbox
        self.overlay = self.window.main_overlay


        self.play_box = CardStack()

        self.play_button.connect("clicked", self.on_play_button_clicked)
        self.window.back_button.connect("clicked", self.on_back_button_clicked)

        cards_list = []
        self.set_subtitle(f"{len(cards_list)} cards")

        self.play_box.set_question(self.title)

    def on_play_button_clicked(self, widget):
        self.window.set_play_mode()
        self.overlay.add_overlay(self.play_box)

    def on_back_button_clicked(self, widget):
        try:
            self.window.unset_play_mode()
            self.play_box.get_parent().remove(self.play_box)
        except:
            pass



@Gtk.Template(resource_path='/io/github/seadve/Flashcards/cardstack.ui')
class CardStack(Gtk.Box):
    __gtype_name__ = 'CardStack'

    question_label = Gtk.Template.Child()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        pass

    def set_question(self, question):
        self.question_label.set_label(question)
