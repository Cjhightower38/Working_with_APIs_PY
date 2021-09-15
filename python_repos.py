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
shade and store it in the variable my_style. Using the style objects in
Pygal set the title, label, and major label which represent only the 
increments of 5k mark offs. Next creat a instance of Pygal's Config
class setting attributes for label rotation, show legend, truncate,
y guide, and the width. As before rotation and legend remain the same
adding truncate to shorten the project names to 15 character unless the
cursormhovers over. Setting y guide lines to False removes them just as
setting legend to False removes the charts legend and finally adding
a width of 1000 better uses the screen real estate. Passing pygal.Bar()
the my_config as the first argument allows pygal to implement personal
changes above Pygal's style objects.
'''
	
my_style = LS('#333366', base_style = LCS)
my_style.title_font_size = 24
my_style.label_font_size = 14
my_style.major_label_font_size = 18

my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000

chart = pygal.Bar(my_config, style = my_style)
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

