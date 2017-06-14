#!/usr/bin/env python
import time
import signal
from termcolor import colored
text = input('What do you want to spam? ')
color = ['red', 'yellow', 'green', 'blue', 'magenta']
try:
    interval = input('At what interval? ')
    interval = float(interval)
except ValueError:
    print("That is not an integer...")
else:
    while True:
        print(colored(text, color[0])),
        time.sleep(interval)
        print(colored(text, color[1])),
        time.sleep(interval)
        print(colored(text, color[2])),
        time.sleep(interval)
        print(colored(text, color[3])),
        time.sleep(interval)
        print(colored(text, color[4])),
        time.sleep(interval)
