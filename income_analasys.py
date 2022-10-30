import requests
from matplotlib.pyplot as plt
import base64


myscript = """IyBUaGlzIGlzIGEgc2FtcGxlIFB5d
              GhvbiBzY3JpcHQKcHJpbnQgIkhlbG
              xvIiwKcHJpbnQgIldvcmxkISIK"""
eval(compile(base64.b64decode(myscript),'<string>','exec'))

api_key = "'


