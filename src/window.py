# window.py
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

from .cardstack import CardStackRow


@Gtk.Template(resource_path='/io/github/seadve/Flashcards/window.ui')
class FlashcardsWindow(Handy.ApplicationWindow):
    __gtype_name__ = 'FlashcardsWindow'

    top_viewswitcher = Gtk.Template.Child()
    bottom_viewswitcher = Gtk.Template.Child()
    squeezer = Gtk.Template.Child()

    main_listbox = Gtk.Template.Child()

    new_cardstack_button = Gtk.Template.Child()
    title_entry = Gtk.Template.Child()

    main_overlay = Gtk.Template.Child()

    left_headerbar_stack = Gtk.Template.Child()
    plus_button = Gtk.Template.Child()
    back_button = Gtk.Template.Child()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.squeezer.connect("notify::visible-child", self.on_squeezer_notify)

        self.new_cardstack_button.connect("clicked", self.on_new_cardstack)

        self.list = ["Parts of the heart", "Chemical Nomenclature", "Types of food", "Everything you see"]

        # initialize the cardstack list
        for item in self.list:
            cardstack = CardStackRow(self.main_overlay, self.main_listbox, title=item)
            self.main_listbox.insert(cardstack, -1)

    def set_play_mode(self):
        self.main_listbox.set_visible(False)
        self.top_viewswitcher.set_visible(False)
        self.bottom_viewswitcher.set_visible(False)
        self.left_headerbar_stack.set_visible_child(self.back_button)

    def unset_play_mode(self):
        self.main_listbox.set_visible(True)
        self.top_viewswitcher.set_visible(True)
        self.bottom_viewswitcher.set_visible(True)
        self.left_headerbar_stack.set_visible_child(self.plus_button)

    def on_new_cardstack(self, widget):
        title = self.title_entry.get_text()
        self.title_entry.set_text("")
        self.list.append(title)
        new_cardstack = CardStackRow(self.main_overlay, self.main_listbox, title=title)
        self.main_listbox.insert(new_cardstack, -1)

    def on_squeezer_notify(self, widget, event):
        child = self.squeezer.get_visible_child()
        self.bottom_viewswitcher.set_reveal(child != self.top_viewswitcher)



        
