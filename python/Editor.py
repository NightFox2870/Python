#!/usr/bin/env python

import pygtk
pygtk.require('2.0')
import gobject
import random
import os
import gtk
#EndImports

class iscApp1:
 iscVtextfile = "/home/yarrith/textfile.txt"
 iscVStr = "Type text here"
 iscWindow6Window1 = gtk.Window(gtk.WINDOW_TOPLEVEL)
 iscWindow6Window1Fixed = gtk.Fixed()
 iscWindow6Button0 = gtk.Button("Done and Save")
 iscWindow6TextField0 = gtk.TextView(buffer=None)
 iscWindow6Button10 = gtk.Button("Open File")

 #EndOfGlobalVariables

 def main(self):
  gtk.main()

 def destroy(self, widget, data=None):
  gtk.main_quit()

#EndOfClass

def iscGetTextField1():
 thisiscApp1.iscVStr = thisiscApp1.iscWindow6TextField0.get_buffer().get_text(thisiscApp1.iscWindow6TextField0.get_buffer().get_start_iter(), thisiscApp1.iscWindow6TextField0.get_buffer().get_end_iter())
 iscSaveAllTextToFile7()
 #iscGetTextField1Done


def iscSaveTextFileDialog2():
 dialog = gtk.FileChooserDialog("Save..", None, gtk.FILE_CHOOSER_ACTION_SAVE,  (gtk.STOCK_CANCEL, gtk.RESPONSE_CANCEL,gtk.STOCK_SAVE, gtk.RESPONSE_OK))
 dialog.set_default_response(gtk.RESPONSE_OK)
 dialog.set_current_name("untitled.txt")
 filter = gtk.FileFilter()
 filter.set_name("Text Files")
 filter.add_mime_type("text/plain")
 filter.add_pattern("*.txt")
 dialog.add_filter(filter)
 filter2 = gtk.FileFilter()
 filter2.set_name("All Files")
 filter2.add_mime_type("All Files")
 filter2.add_pattern("*.*")
 dialog.add_filter(filter2)
 response = dialog.run()
 if response == gtk.RESPONSE_OK:
  thisiscApp1.iscVtextfile = dialog.get_filename()
  iscGetTextField1()
  #iscSaveTextFileDialog2Done
  pass
 elif response == gtk.RESPONSE_CANCEL:
  #iscSaveTextFileDialog2Cancelled
  pass

 dialog.destroy()

def iscOpenTextFileDialog3():
 dialog = gtk.FileChooserDialog("Open..", None, gtk.FILE_CHOOSER_ACTION_OPEN,  (gtk.STOCK_CANCEL, gtk.RESPONSE_CANCEL,gtk.STOCK_OPEN, gtk.RESPONSE_OK))
 dialog.set_default_response(gtk.RESPONSE_OK)
 filter = gtk.FileFilter()
 filter.set_name("Text Files")
 filter.add_mime_type("text/txt")
 filter.add_mime_type("image/jpeg")
 filter.add_pattern("*.txt")
 filter.add_pattern("*.text")
 dialog.add_filter(filter)
 response = dialog.run()
 if response == gtk.RESPONSE_OK:
  thisiscApp1.iscVtextfile = dialog.get_filename()
  iscReadAllTextFromFile5()
  #iscOpenTextFileDialog3Done
  pass
 elif response == gtk.RESPONSE_CANCEL:
  #iscOpenTextFileDialog3Cancelled
  pass

 dialog.destroy()

def iscSetTextField4():
 thisiscApp1.iscWindow6TextField0.get_buffer().set_text(thisiscApp1.iscVStr)
 #iscSetTextField4Done


def iscReadAllTextFromFile5():
 f = open(thisiscApp1.iscVtextfile, 'r+')
 thisiscApp1.iscVStr = f.read()
 f.close()
 iscSetTextField4()
 #iscReadAllTextFromFile5Done


def iscWindow6():
 thisiscApp1.iscWindow6Button0 = gtk.Button("Done and Save")
 thisiscApp1.iscWindow6TextField0 = gtk.TextView(buffer=None)
 thisiscApp1.iscWindow6Button10 = gtk.Button("Open File")
 thisiscApp1.iscWindow6Window1 = gtk.Window(gtk.WINDOW_TOPLEVEL)
 thisiscApp1.iscWindow6Window1Fixed = gtk.Fixed()
 thisiscApp1.iscWindow6Window1.set_title("Window")
 thisiscApp1.iscWindow6Window1.set_default_size(300, 300)
 thisiscApp1.iscWindow6Window1.add(thisiscApp1.iscWindow6Window1Fixed)
 thisiscApp1.iscWindow6Window1Fixed.width = 300
 thisiscApp1.iscWindow6Window1Fixed.height = 300
 thisiscApp1.iscWindow6Window1.connect("delete_event", iscWindow6Closed)
 thisiscApp1.iscWindow6Window1Fixed.show()
 thisiscApp1.iscWindow6Window1Fixed.put(thisiscApp1.iscWindow6Button0, 191, 6)
 thisiscApp1.iscWindow6Button0.set_size_request(91, 24)
 thisiscApp1.iscWindow6Button0.connect("clicked", iscWindow6ButtonClicked)
 thisiscApp1.iscWindow6Button0.show()
 thisiscApp1.iscWindow6Window1Fixed.put(thisiscApp1.iscWindow6TextField0, 6, 35)
 thisiscApp1.iscWindow6TextField0.set_size_request(287, 259)
 thisiscApp1.iscWindow6TextField0.show()
 thisiscApp1.iscWindow6Window1Fixed.put(thisiscApp1.iscWindow6Button10, 7, 5)
 thisiscApp1.iscWindow6Button10.set_size_request(80, 26)
 thisiscApp1.iscWindow6Button10.connect("clicked", iscWindow6Button1Clicked)
 thisiscApp1.iscWindow6Button10.show()
 thisiscApp1.iscWindow6Window1.show()
 #iscWindow6Opened
 #iscWindow6Done


def iscWindow6Closed(self, other):
 pass
 iscAppQuit8()
 #iscWindow6Closed


def iscWindow6ButtonClicked(self):
 pass
 iscSaveTextFileDialog2()
 #iscWindow6ButtonClicked


def iscWindow6Button1Clicked(self):
 pass
 iscOpenTextFileDialog3()
 #iscWindow6Button1Clicked


def iscSaveAllTextToFile7():
 f = open(thisiscApp1.iscVtextfile, 'w')
 f.write(thisiscApp1.iscVStr)
 f.close()
 iscAppQuit8()
 #iscSaveAllTextToFile7Done


def iscAppQuit8():
 thisiscApp1.destroy(None,None)
 #iscAppQuit8Done


#EndOfFunctions

thisiscApp1 = iscApp1()

iscWindow6()
#iscApp1Launched
#EndOfStatements

thisiscApp1.main()