# Import the requests module which allows Python to easily request info
import requests

'''
Store the url in url variable and use requests.get() to make the call to
url and store it in a variable. Use the status_code attribute and print
the results to screen(200 indicates success.) Finally convert the 
returned results from JSON format to a Python list using the json().
'''
  
url = 'http://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print('Status code:', r.status_code)
# Store API response in a variable.
response_dict = r.json()

# Process results.
print(response_dict.keys())

