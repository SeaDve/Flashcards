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

    def __init__(self, overlay, title, **kwargs):
        super().__init__(**kwargs)

        self.title = title
        self.overlay = overlay

        self.set_title(self.title)

        cards_list = []
        self.set_subtitle(f"{len(cards_list)} cards")


@Gtk.Template(resource_path='/io/github/seadve/Flashcards/cardstack.ui')
class CardStack(Gtk.Box):
    __gtype_name__ = 'CardStack'

    def __init__(self):
        pass
