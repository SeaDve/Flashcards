# main.py
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

import sys
import gi

gi.require_version('Gtk', '3.0')
gi.require_version('Handy', '1')

from gi.repository import Gtk, GLib, Gio, Handy

from .window import FlashcardsWindow


class Application(Gtk.Application):
    def __init__(self, version):
        super().__init__(application_id='io.github.seadve.Flashcards',
                         flags=Gio.ApplicationFlags.FLAGS_NONE)

        self.version = version

        GLib.set_application_name("Flashcards")
        GLib.set_prgname('io.github.seadve.Flashcards')

    def do_startup(self):
        Gtk.Application.do_startup(self)

        Handy.init()

        self.setup_actions()

    def do_activate(self):
        self.window = self.props.active_window
        if not self.window:
            self.window = FlashcardsWindow(application=self)
        self.window.present()

    def setup_actions(self):
        action = Gio.SimpleAction.new("show-about", None)
        action.connect("activate", self.show_about_dialog)
        self.add_action(action)

    def show_about_dialog(self, action, widget):
        about = Gtk.AboutDialog()
        about.set_transient_for(self.window)
        about.set_modal(True)
        about.set_version(self.version)
        about.set_program_name("Flashcards")
        about.set_logo_icon_name("io.github.seadve.Flashcards")
        about.set_authors(["Dave Patrick"])
        about.set_comments(_("Simple memorizing aid"))
        about.set_wrap_license(True)
        about.set_license_type(Gtk.License.GPL_3_0)
        about.set_copyright(_("Copyright 2021 Dave Patrick"))
        # Translators: Replace "translator-credits" with your names, one name per line
        about.set_translator_credits(_("translator-credits"))
        about.set_website_label(_("GitHub"))
        about.set_website("https://github.com/SeaDve/Flashcards")
        about.show()


def main(version):
    app = Application(version)
    return app.run(sys.argv)
