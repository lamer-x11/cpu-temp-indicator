#!/usr/bin/env python

from pkg_resources import resource_filename
import gobject
import gtk

class Indicator:
    def __init__(self):
        self.icon = None
        self.loadAllIcons()

    # Loads all icons
    def loadAllIcons(self):
        self.iconRegular = self.loadIcon('optimal')
        self.iconWarning = self.loadIcon('high')
        self.iconCritical = self.loadIcon('overheating')

    # Loads a single icon
    def loadIcon(self, name):
        resource = 'icons/{0}.png'.format(name)
        fileName = resource_filename(__name__, resource)

        return gtk.gdk.pixbuf_new_from_file(fileName)

    # Sets a state object
    def setState(self, state):
        self.state = state

    # Creates the indicator icon
    def createIcon(self):
        self.icon = gtk.StatusIcon()
        self.icon.connect('popup-menu', self.rightClick)
        self.icon.set_from_pixbuf(self.iconRegular)

    # Handles right click event
    def rightClick(self, icon, button, timestamp):
        menu = gtk.Menu()

        menuItemQuit = gtk.ImageMenuItem('Quit')

        image = gtk.image_new_from_stock(gtk.STOCK_QUIT, gtk.ICON_SIZE_MENU)
        image.show()

        menuItemQuit.set_image(image)
        menuItemQuit.connect('activate', gtk.main_quit)

        menu.append(menuItemQuit)
        menu.show_all()
        menu.popup(None, None, gtk.status_icon_position_menu, button, timestamp, icon)

    # Creates the icons and starts the update loop
    def start(self):
        self.createIcon()
        gobject.timeout_add(1000, self.update)

    # Updates the indicator 
    def update(self):
        data = self.state.getState()

        self.icon.set_tooltip(data['message'])

        if data['state'] == self.state.STATE_CRITICAL:
            self.icon.set_from_pixbuf(self.iconCritical) 
            return True

        if data['state'] == self.state.STATE_WARNING:
            self.icon.set_from_pixbuf(self.iconWarning) 
            return True

        self.icon.set_from_pixbuf(self.iconRegular) 
        return True
