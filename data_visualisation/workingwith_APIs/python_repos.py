import requests
from plotly.graph_objs import Bar
from plotly import offline
# Make an API call and store the response.
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers = headers)
print(f"Status code: {r.status_code}")

# Store API response in a variable.
response_dicts = r.json()
print(f"Total repositories : {response_dicts['total_count']}")

# Explore information about the repositories.
repo_dicts = response_dicts['items']
print(f"\nRepositories returned : {len(repo_dicts)}")

# Process results, adding the link for repositories
repo_links, stars, labels = [], [], []
for repo_dict in repo_dicts:
	repo_name = repo_dict['name']
	repo_url = repo_dict['html_url']
	repo_link = f"<a href='{repo_url}'>{repo_name}</a>"
	repo_links.append(repo_link)
	stars.append(repo_dict['stargazers_count'])

	owner = repo_dict['owner']['login']
	description = repo_dict['description']
	label = f"{owner} <br />{description}"
	labels.append(label)

#Make the visualisation
data = [{
		'type':'bar',
		'x': repo_links,
		'y': stars,
		'hovertext': labels,
		'marker': {
					'color': 'rgb(60, 100, 150)',
					'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'}
					},
		'opacity': 0.6,
}]

my_layout = {
				'title': 'Most-Starred Python Projects on GitHub',
				'titlefont':{'size':28},
				'xaxis': {'title':'Repository'},
				'yaxis': {'title':'Stars'},
}	

fig = {'data': data, 'layout': my_layout}
offline.plot(fig,filename="python_repositories.html")