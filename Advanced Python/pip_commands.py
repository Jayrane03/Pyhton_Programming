from cgi import print_environ
from ensurepip import version
import imp
from importlib.metadata import packages_distributions
from importlib.resources import Package
from tabnanny import check


# pip --version  --to check pip version
# C:\Users\Your Name\AppData\Local\Programs\Python\Python36-32\Scripts>pip uninstall camelcase -- uninstall a package
# pip install –upgrade pip 
# pip list will show all the install packages

import camelcase

c = camelcase.CamelCase()

text = "Hello World"
print(c.hump(text))







