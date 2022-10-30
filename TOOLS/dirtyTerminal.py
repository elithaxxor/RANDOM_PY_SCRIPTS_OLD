#make terminal
import vte 
import os
import gtk
import time
from VirtualTerminal import VirtualTerminal
 
terminal = vte.Terminal()
terminal.connect ("child-exited", lambda term: gtk.main_quit())
terminal.fork_command()

    # put the terminal in a scrollable window
terminal_window = gtk.ScrolledWindow()
terminal_window.set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_AUTOMATIC)
terminal_window.add(terminal)
