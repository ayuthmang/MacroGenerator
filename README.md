# What is __MacroGenerater__

MacroGenerator is a python script - for people who want to create a bot for boundary testing or build a little macro scripts.


## Script's Require

Python 2.6.4 or newer is recommended.

## Import Script

```python
from MacroGenerator import MacroGenerator
```

## Functions

```python

# the constructor
# name = file name that you want to created
def __init__(self, target_name):


# write a content in a file line by line
def write_file(self, command):

# insert ctrl + v (paste) in our macro file
def paste_clipboard(self):

# set clipboard with argument text string
def set_clipboard(self, text):

# wait for x millisecconds, e.g. 1000 = 1 seccond
def set_delay(self, delay):

# type text with keyboard
# {#crlf#} = new line (but doesnt mean it press 'Enter' key)
def typetext(self, text):
  self.write_file('TYPE TEXT : {0}'.format(re.sub(r'\n', '{#crlf#}', text)))
  
# Click a mouse in current position	
# mouse_event: ['Click', 'RightClick']
def mouse_click(self, mouse_event = 'Click'):
  self.write_file('Mouse : 0 : 0 : {0} : 0 : 1 : 0'.format(mouse_event));

# YOU MUST CLOSE A FILE AFTER YOU'VE OPENED IT UP
# close a file that we've opened
def close(self):
  self.__fopen.close();
```

## Building Script

### Python

```bash
python [file_name.py]
```

### [Tips] Sublime Text

On Sublime Text you can open *.py file and press 'Ctrl + B' for building a script.


## Usage example

- [helloMacro](https://github.com/blackSourcez/MacroGenerator/blob/master/sample/helloMacro.py)








