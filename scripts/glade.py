import gi
from gi.repository import Gtk

class Handler:
  def onDestroy(self, *args):
    Gtk.main_quit()

builder.Gtk.Builder()
builder.add_from_file('../ui/design_1.glade')
builder.connect_signals(Handler())

window = builder.get_object('window1')
window.show_all()

Gtk.main()