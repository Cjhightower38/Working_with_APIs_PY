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

# Print the total count of repositories on GitHub.
print('Toltal repositories:', response_dict['total_count'])

# Store the list of dictionaries(items) from response_dict into the 
# repo_dicts variable and print the length of the variable.
repo_dicts = response_dict['items']
print('Repositoires returned:', len(repo_dicts))

# Pull the first iteam[0] from repo_dicts storing the result in a 
# variable and print the length of repo_dict. Iterate through each key 
# and call the sorted() to sort the results in ascending order.
repo_dict = repo_dicts[0]
print('\nKeys:', len(repo_dict))
for key in sorted(repo_dict.keys()):
	print(key)

