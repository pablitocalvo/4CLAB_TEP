import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class MyWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="terzo")
		# demo per una label di testo
        self.testo = Gtk.Label("Questa e' una label di testo ")
        self.add(self.testo)
       

win = MyWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
