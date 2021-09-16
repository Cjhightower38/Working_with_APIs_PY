'''
Import Pygal and from the style module import lightcolorized and 
lightenstyle as LCS and LC respectively.
'''

import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

'''
Using my style variable to store the RGB and default background then 
store pygal.Bar() with the attributes as before in the the chart 
variable. Add the title and x-aixs label then create a list of 
dictionaries to store each project having two keys one for value which
represents the star totals and label which store a description of the
project or tooltip. The add() takes a sting and a list(which is left
empty because there is no need to label the data series) and the render
the results to a .svg file. 
'''

my_style = LS('#333366', base_style = LCS)
chart = pygal.Bar(style = my_style, x_label_rotation = 45,
    show_legend = False)
    
chart.title = 'Python Projects.'
chart.x_labels = ['httpie', 'django', 'flask']

plot_dicts = [
    {'value': 16101, 'label': 'Description of httpie.'},
    {'value': 15028, 'label': 'Description of django.'},
    {'value': 14798, 'label': 'Description of flask.'},
    ]
    
chart.add('', plot_dicts)
chart.render_to_file('bar_descriptions.svg')

