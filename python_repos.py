'''
Import the requests module which allows Python to easily request info.
and pygal.style from the pygal libray and set LightColorizedStyle and
LightenStyle as LCS and LC alias respectively.
'''
import requests

import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

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

'''
Create two empty dictionaries to store the name and stars given on 
GitHub. Then iterrate through each item in repo_dicts then append each
result to the corresponding dictionary.
'''
names, stars = [], []
for repo_dict in repo_dicts:
	names.append(repo_dict['name'])
	stars.append(repo_dict['stargazers_count'])
	
'''
Used the LS alias and set the shade to dark blue(RGB = 2 digits each 
color) then passed the base style the alias LCS and retained the defualt
shade and store it in the variable my_style. Next using the Bar() method
passing my_style, setting the rotation of the chart to 45 and removing
the chart legend by setting to False. Finally adding the title and the 
names of each project to the x-axis.
'''
	
my_style = LS('#333366', base_style = LCS)
chart = pygal.Bar(stlye = my_style, x_label_rotation = 45,
    show_legend = False)
chart.title = 'Most-Starred Python Projects on GitHub'
chart.x_labels = names

'''
The first attribute is left empty. Since there is no need to lable the
1 through 5 stars only the stars label is needed for the y-axis. Why?
The chart is interative so as I move the cursor over a project the stars
show. The render to a .svg file. Reminder the .svg file can be found in
file explorer.
'''

chart.add('', stars)
chart.render_to_file('python_repos.svg')

