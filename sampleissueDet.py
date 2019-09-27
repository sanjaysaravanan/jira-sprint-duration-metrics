from jira import JIRA
import json
import requests
from datetime import date
import calendar

cal = dict((v,k) for k,v in enumerate(calendar.month_abbr))
#options = {'server': 'https://sanjaysaravanan.atlassian.net'}
#credentials = ('sanjaysaravanan1997@gmail.com', '3YBtc505zNEqCZZLC9C72519')#username and api token
options = {'server': 'https://altimetrik.atlassian.net'}
credentials = ('farid.roshan@altimetrik.com', 'cA1AvOAgGdMaccejfgwy8919')

def main():
	jira = JIRA(options, basic_auth=credentials)
	#project = jira.project('DC')
	#sprints = requests.get( options['server'] + '/rest/greenhopper/1.0/integration/teamcalendars/sprint/list?jql=project=' + project.id, auth=credentials ).json()['sprints']

	response = requests.get('https://altimetrik.atlassian.net/rest/greenhopper/latest/rapid/charts/sprintreport?rapidViewId=274&sprintId=647', auth=credentials ).json()
	sprint_stroy_details = {}
	#print( "sprint_name : " + response['sprint']['name'])
	sprint_stroy_details['sprint_name'] = response['sprint']['name']
	#print( "sprint_id : " + str(response['sprint']['id']))
	sprint_stroy_details['sprint_id'] = str(response['sprint']['id'])
	#print("summary : ")
	sprint_stroy_details['summary'] = {}
	#print("num_of_stories_completed:" + str(len(response['contents']['completedIssues'])))
	sprint_stroy_details['summary']['num_of_stories_completed'] = str(len(response['contents']['completedIssues']))
	i,j = 1,0
	changed_estimate_stories = {}
	for issue in response['contents']['issuesNotCompletedInCurrentSprint']:
		key = issue['key']
		#print(str(i) + str(issue))
		try:
			currentStory = issue['currentEstimateStatistic']['statFieldValue']['value']	
			estimateStory = issue['estimateStatistic']['statFieldValue']['value']
			#print("Current Story Points : " + str(issue['currentEstimateStatistic']['statFieldValue']['value']))
			#print("Estimated Story Points : " + str(issue['estimateStatistic']['statFieldValue']['value']))
			if currentStory != estimateStory:
				j+=1
				changed_estimate_stories[key] = {}
				changed_estimate_stories[key]['from'] = str(estimateStory)
				changed_estimate_stories[key]['to'] = str(currentStory)
		except KeyError:
			pass
	#print("num_of_stories_estimate_changed:" + str(j))
	sprint_stroy_details['summary']['num_of_stories_estimate_changed'] = str(j)
	#print("details:")
	sprint_stroy_details['details'] = changed_estimate_stories
	#print("changed_estimate_stories:" + str(changed_estimate_stories))
	print(str(sprint_stroy_details))
	print(json.dumps(json.loads(str(sprint_stroy_details)), sort_keys=True, indent=4, separators=("," , ": ")))
	#print("" + len(response['issuesNotCompletedInCurrentSprint']))
	#sprint = jira.sprint('647')


main()