'''
Import request and itemgetter from the operator module. Store the url 
in a variable and pass the variable to the requests get() and print 
neatly the status code which should be 200 if sucessful.
'''
import requests

from operator import itemgetter

url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print('Status code:', r.status_code)

'''
Using the json() to convert the returned request from variable r then
create a empty dictionary to store each dictionary as json() returns a 
list that Python can read. Next itterate through each result returned 
from the r variable and make a seperate call to each submission or 
returned result from the r variable. The new url call includes the value 
of submission_id which is then printed out with the status code as 
before and stored in another variable(response_dict) with .json() once 
again so Python will be able to work with the list of dictionaries.
'''
# Reminder [:30] means the first 30 submissions.

submission_ids = r.json()
submission_dicts = []
for submission_id in submission_ids[:30]:
	url = ('https://hacker-news.firebaseio.com/v0/item/' +
	        str(submission_id) + '.json')
	submission_r = requests.get(url)
	print(submission_r.status_code)
	response_dict = submission_r.json()
	
	'''
Next create a variable to store the title, link, and comments if any.
The variable can be anything in this case submission dict was used and
then appened into the empty submission dicts dictionary created before.
before a variable can be used it has to be called ahead or an error
will occur. Using the sorted() to sort through the submission dicts
results and using itemgetter to sort each key by the comments then 
passing the reverse argument True to sort in descending order. Finally 
itterate through each of the 30 results([:30]) and printing the title,
discussion link, and the comments.
    '''	
	
# Be careful when entering the url. If the spelling is incorrect a 401
# error will occur

	submission_dict = {
	    'title': response_dict['title'],
	    'link': 'http://news.ycombinator.com/item?id=' + str(submission_id),
	    'comments': response_dict.get('descendants', 0)
	    }
	submission_dicts.append(submission_dict)
	
submission_dicts = sorted(submission_dicts, key=itemgetter('comments'),
                            reverse=True)
                            
for submission_dict in submission_dicts:
	print('\nTitle:', submission_dict['title'])
	print('Discussion link:', submission_dict['link'])
	print('Comments:', submission_dict['comments'])
	
