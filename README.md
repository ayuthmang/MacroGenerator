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
def write_file(self, command): # write a content in a file line by line

def paste_clipboard(self): # insert ctrl + v (paste) in our macro file

def set_clipboard(self, text): # set clipboard with argument text string

def set_delay(self, delay): # wait for x millisecconds, e.g. 1000 = 1 seccond
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








