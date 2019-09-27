from jira import JIRA
import json
import requests
from datetime import date
import calendar
import os
print(os.environ['JIRA_SERVER_URL'])
print(os.environ['JIRA_USERNAME'])
print(os.environ['JIRA_PASSWORD'])

cal = dict((v,k) for k,v in enumerate(calendar.month_abbr))
options = {'server': os.environ['JIRA_SERVER_URL']}
credentials = (os.environ['JIRA_USERNAME'], os.environ['JIRA_PASSWORD'])



def main():
	jira = JIRA(options, basic_auth=credentials)
	#print(dir(jira))
	board = jira.boards()[0]
	sprint = jira.sprints(board.id)[0]
	print(board)
	print(dir(board))
	print("########################################################################")
	print(sprint)
	print(dir(sprint))
	#sprints = jira.sprints('10710')
	'''projects = jira.projects()
	data_dict = {}
	for project in projects[:2]:
		print ( project.id + " : " + project.name )
		data_dict[project.name] = {}
		data_dict[project.name]['id'] = project.id
		sprints = requests.get( options['server'] + '/rest/greenhopper/1.0/integration/teamcalendars/sprint/list?jql=project=' + project.id, auth=credentials ).json()['sprints']
		durationList = []
		for sprint in sprints:
			sprint1 = jira.sprint(sprint['id'])
			data_dict[project.name][sprint1.name] = {}
			data_dict[project.name][sprint1.name]['id'] = sprint1.id
			strtD = sprint1.startDate
			endD = sprint1.endDate
			comD = sprint1.completeDate
			print("  " + str(sprint['id']) + " : " + sprint['name'])
			print("    -------------------------------------------------------------")
			print("    Start Date : " + strtD)
			data_dict[project.name][sprint1.name]['start_time'] = strtD
			print("    Estimated End Date : " + endD)
			data_dict[project.name][sprint1.name]['end_time'] = endD
			print("    Completed Date :" + comD)
			data_dict[project.name][sprint1.name]['complete_time'] = comD
			if strtD != 'None' and comD != 'None':	
				startl = strtD[:9].split('/')
				compl = comD[:9].split('/')
				date1 = date(int('20' + startl[2]),cal[startl[1]],int(startl[0]))
				date2 = date(int('20' + compl[2]),cal[compl[1]],int(compl[0]))
				duration = (date2-date1).days
				durationList.append(duration)
				data_dict[project.name][sprint1.name]['sprint_duration'] = str(duration) + ' Days'
				print("    Duration : " + str(duration) + " Days")
			else:
				print("    Ongoing Sprint")
			print("    -------------------------------------------------------------\n")
		try:
			avgDuration = sum(durationList) / len(durationList)
			data_dict[project.name]['average_sprint_duration'] = avgDuration
			print("  Average Sprint Duration : " + str(avgDuration))
		except ZeroDivisionError:
			print("  Average Sprint Duration : 14 days ")
			data_dict[project.name]['average_sprint_duration'] = 14.0
	json_data = json.dumps(data_dict, indent=4)
	with open('result.json', 'w') as fp:
		json.dump(data_dict, fp, indent=4)'''
   	#print(str(sprint) + "\n\n")
	# gh = GreenHopper(options, basic_auth=('farid.roshan@altimetrik.com', 'cA1AvOAgGdMaccejfgwy8919'))
	# boards = gh.boards()

	# print (str(dir(boards[0])) + "\n\n")

	# sprints = gh.sprints(boards[0].id)

	# for sprint in sprints:
	# 	print(sprint.name)



	'''print(jira)
	issue = jira.issue()
	print (issue.fields.assignee)
	print (issue.fields.reporter)'''

	#proj = jira.project('SAM')
	'''j=1
	issues=jira.search_issues('project=DC',maxResults=3)#gives the first 0 issues
	print("Issues...")
	for issue in issues:
		print (issue.fields.created)
		print (issue.fields.status.name)
		j+=1
	Projects,i = [],1
	for project in jira.projects():
		print (str(i) + " Key :" + project.key + " Name : " + project.name)
		i+=1'''
	#print(Projects)
	#print(dir(jira.issue('DC-214')))

	#print("\n\n")
	#print(dir(jira.project('DC')))
	#print(jira.sprints( jira.boards()[0].id ))		

	#jiraResponse1 = requests.get('https://altimetrik.atlassian.net/rest/api/2/project/DC', auth=('farid.roshan@altimetrik.com','cA1AvOAgGdMaccejfgwy8919')).json()
	#jiraResponse2 = requests.get('https://altimetrik.atlassian.net/rest/agile/1.0/sprint/468', auth=('farid.roshan@altimetrik.com','cA1AvOAgGdMaccejfgwy8919')).json()

	#jiraResponse3 = requests.get('https://altimetrik.atlassian.net/rest/greenhopper/1.0/integration/teamcalendars/issue/list?jql=project=DC', auth=('farid.roshan@altimetrik.com','cA1AvOAgGdMaccejfgwy8919')).json()
	#print(jiraResponse3)
	#print(jiraResponse3['sprints'][0])

	'''
	'_get_url', '_load', '_options', '_parse_raw', '_resource', '_session', 'canUpdateSprint', 'completeDate', 'daysRemaining',
	 'delete', 'endDate', 'find', 'goal', 'id', 'isoCompleteDate', 'isoEndDate', 'isoStartDate', 'linkedPagesCount', 'name', 
	 'raw', 'remoteLinks', 'self', 'sequence', 'startDate', 'state', 'update']

	'''

	#print(jiraResponse2['values'][468]['startDate'][:10])
	#print(jira.sprint(468).startDate)
	#print(jira.sprint(468).endDate)
	'''sprint1 = jira.sprint(606)
	print("\n\n\n")
	print(" Sprint 606 " )
	print("\nURL : " + str(sprint1._get_url))
	print("\noptions : " + str(sprint1._options))
	print("\nresource " + str(sprint1._resource))
	print("\nsession " + str(sprint1._session))
	print("\ncanUpdateSprint " + str(sprint1.canUpdateSprint))
	
	print("\n-------------------------------------------------------------")
	print(sprint1.startDate)
	print(sprint1.endDate)
	print("completeDate " + str(sprint1.completeDate))
	print("-------------------------------------------------------------\n")
	print("\nfind " + str(sprint1.find))
	print("\ngoal " + str(sprint1.goal))
	print("\nid " + str(sprint1.id))
	print("\nisoCompleteDate " + str(sprint1.isoCompleteDate))
	print("\nisoEndDate " + str(sprint1.isoEndDate))
	print("\nisoStartDate " + str(sprint1.isoStartDate))'''


	#create_date = datetime.date.today().strftime("%I:%M%p on %B %d, %Y")
	#print(create_date)
	#print(jira.sprints())
	#print(jira.sprints( jira.boards()[0].id ))	
	#sprints = jira.sprints('DC')

	#print("\n\n\n\n")
	#print(jiraResponse1)

if __name__== "__main__" :
    main()