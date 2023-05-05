from operator import itemgetter

import requests
from plotly.graph_objs import Bar
from plotly import offline

#Make an API call and store the responses
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print(f"Status code : {r.status_code}")

# Process information about each submission.
submissions_id = r.json()
submissions_dict = []
for submission_id in submissions_id[:30]:
	# Make a separate API call for each submission.
	url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
	r = requests.get(url)
	print(f"id: {submission_id}\tstatus: {r.status_code}")
	response_dict = r.json()

	# Build a dictionary for each article.
	submission_dict = {
						'title': response_dict['title'],
						'hn_link': f"http://news.ycombinator.com/item?id={submission_id}",
						'score': response_dict['score'],
	}
	submissions_dict.append(submission_dict)

submissions_dict = sorted(submissions_dict, key=itemgetter('score'), reverse=True)

submissions_links, score = [], []
for submission_dict in submissions_dict:
	print(f"\nTitle: {submission_dict['title']}")
	print(f"Discussion link: {submission_dict['hn_link']}")
	print(f"Score: {submission_dict['score']}")

	subm_title = submission_dict['title']
	subm_url = submission_dict['hn_link']
	subm_link = f"<a href='{subm_url}'>{subm_title}</a>"
	submissions_links.append(subm_link)
	score.append(submission_dict['score'])


#Visualise the submissions
data = [{
			'type': 'bar',
			'x': submissions_links,
			'y': score,
}]

my_layout = {
				'title':'Hacker News submissions bar',
				'titlefont':{'size':28},
				'xaxis':{'title':'Submissions'},
				'yaxis':{'title':'Score',},
}
fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='hn_submissions.html')

