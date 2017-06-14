#!/usr/bin/env python
text = input('What do you want to spam?')
import time
from termcolor import colored
while True:
     print(colored(text, 'red'))
     time.sleep(0.075)
     print(colored(text, 'yellow'))
     time.sleep(0.075)
     print(colored(text, 'yellow'))
     time.sleep(0.075)
     print(colored(text, 'green'))
     time.sleep(0.08)
     print(colored(text, 'blue'))
