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

from .cardstack import CardStack


@Gtk.Template(resource_path='/io/github/seadve/Flashcards/window.ui')
class FlashcardsWindow(Handy.ApplicationWindow):
    __gtype_name__ = 'FlashcardsWindow'

    top_viewswitcher = Gtk.Template.Child()
    bottom_viewswitcher = Gtk.Template.Child()
    squeezer = Gtk.Template.Child()

    main_listbox = Gtk.Template.Child()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.squeezer.connect("notify::visible-child", self.on_squeezer_notify)

        self.list = ["hidave", "hida", "hidasd", "higsd"]

        for item in self.list:
            stack = CardStack(title=item)
            self.main_listbox.insert(stack, -1)



    def on_squeezer_notify(self, widget, event):
        child = self.squeezer.get_visible_child()
        self.bottom_viewswitcher.set_reveal(child != self.top_viewswitcher)
        
