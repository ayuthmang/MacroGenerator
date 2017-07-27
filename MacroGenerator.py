"""

This script used for generating macro file (.mcr) for Macro Recorder
you can download at https://www.jitbit.com/macro-recorder/

"""

__author__ = "Ayuth Mangmesap (blackSource)"

import re

class MacroGenerator:

	def __init__(self, target_name):
		# super(MacroGenerator, self).__init__()
		self.target_name = target_name;
		self.__fopen = open(target_name,"w");

	def write_file(self, command):
		self.__fopen.write(command + '\n');

	def paste_clipboard(self):
		self.write_file('Keyboard : ControlLeft : KeyDown')
		self.write_file('Keyboard : V : KeyDown')
		self.write_file('Keyboard : V : KeyUp')
		self.write_file('Keyboard : ControlLeft : KeyUp')

	def set_clipboard(self, text):
		self.write_file('SET CLIPBOARD : {0} : 0 : Please enter the text to store in clipboard:'.format(text))

	def set_delay(self, delay):
		self.write_file('DELAY : {0}'.format(delay));

	def sendkey(self, key):
		self.write_file('Keyboard : {0} : KeyPress'.format(key));

	def init():
		self.set_delay(macro_file,1000);

	def close(self):
		self.__fopen.close();