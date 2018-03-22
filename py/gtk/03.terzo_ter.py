import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class MyWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="media dei voti")
        
        # demo per un campo di testo 
        self.voti = Gtk.Entry()
        self.add(self.voti)
        
        #bottone 
        self.button = Gtk.Button(label="Calcola Media")
        self.button.connect("clicked", self.on_button_clicked)
        self.add(self.button)
        #NON FUNZIONA PERCHE' NON E' POSSIBILE INSERIRE PIU' 
        #WIDGET IN UNA FINESTRA
        #BISOGNA INSERIRLE IN UN CONTENITORE.....
        
		# demo per una label di testo
        self.voti = Gtk.Label("media = ")
        self.add(self.voti) 
        
        
    def on_button_clicked(self, widget):
        # calcola la media ......
        print("Hello World")


win = MyWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
