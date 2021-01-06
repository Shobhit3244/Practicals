"""
Open a webpage using the urllib library.
"""
import urllib.request
import webbrowser

x = urllib.request.urlopen('http://shobhit3244.github.io/')
url = x.geturl()
print("now opening the url:", url)
webbrowser.open_new(url)
