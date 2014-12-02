# Copyright (C) 2014, One Laptop Per Child
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the
# Free Software Foundation, Inc., 59 Temple Place - Suite 330,
# Boston, MA 02111-1307, USA.

from gi.repository import Gtk
from gi.repository import GLib

from sugar3.graphics import style


class MessageBox(Gtk.EventBox):
    """Widget to display informative messages.

    Required: title
    Optional: An Icon, description text, and multiple buttons

    """
    def __init__(self, title, icon=None, description=None):
        Gtk.EventBox.__init__(self)

        self.icon = icon

        self.modify_bg(Gtk.StateType.NORMAL,
                       style.COLOR_WHITE.get_gdk_color())

        alignment = Gtk.Alignment.new(0.5, 0.5, 0.1, 0.1)
        self.add(alignment)
        alignment.show()

        box = Gtk.VBox()
        alignment.add(box)
        box.show()

        if icon is not None:
            box.pack_start(icon, expand=True, fill=False, padding=0)
            icon.show()

        title_label = Gtk.Label()
        title_color = style.COLOR_BUTTON_GREY.get_html()
        title_label.set_markup('<span weight="bold" color="%s">%s</span>' % (
            title_color, GLib.markup_escape_text(title)))
        box.pack_start(title_label, expand=True, fill=False, padding=0)
        title_label.show()

        self.button_box = Gtk.HButtonBox()
        self.button_box.set_layout(Gtk.ButtonBoxStyle.CENTER)
        box.pack_start(self.button_box, False, True, 0)
        self.button_box.show()

    def add_button(self, button):
        self.button_box.pack_start(button, expand=True, fill=False, padding=0)
