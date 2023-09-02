import os
import sys
from os import getcwd

where_I_am = getcwd()
print("My Platform: ")
print(sys.platform)
print("Where I am: ")
print(where_I_am)
print(os.environ)
