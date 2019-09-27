from jira import JIRA
from jira.client import GreenHopper
import json
import requests
from datetime import date
import calendar
import os
from pymongo import MongoClient

cal = dict((v,k) for k,v in enumerate(calendar.month_abbr))
options = {'server': os.environ['JIRA_SERVER_URL']}
credentials = (os.environ['JIRA_USERNAME'], os.environ['JIRA_PASSWORD'])
endpoint = '/rest/greenhopper/1.0/integration/teamcalendars/sprint/list?jql=project='
url = options['server'] + endpoint
db_host,db_name,db_collection = 'mongodb://localhost:27017/','sampledb','average_sprint_duration'

jira = JIRA(options, basic_auth=credentials)

def detailedSprintInfo(sprintId):
	sprint = jira.sprint(sprintId)
	dates = (sprint.startDate, sprint.endDate, sprint.completeDate)
	return [ sprintId, dates ]

def assignSprintDetails(sprintDetails):
	sprint_dict = {}
	sprint_dict['id'] = str(sprintDetails[0])
	(strtD,endD,comD) = sprintDetails[1]
	sprint_dict['start_time'] = strtD
	sprint_dict['end_time'] = endD
	sprint_dict['complete_time'] = comD
	sprint_dict['sprint_duration'] = sprintDuration(sprintDetails[1])
	return sprint_dict

def sprintDuration(dates):
	(strtD, endD, comD) = dates
	startl = strtD[:9].split('/')
	date1 = date(int('20' + startl[2]),cal[startl[1]],int(startl[0]))
	if comD != 'None':	
		compl = comD[:9].split('/')
		date2 = date(int('20' + compl[2]),cal[compl[1]],int(compl[0]))
		return (date2-date1).days
	else:
		endl = endD[:9].split('/')
		date2 = date(int('20' + endl[2]),cal[endl[1]],int(endl[0]))
		return (date2-date1).days

def averageDuration(durationList):
	try:
		avgDuration = sum(durationList) / len(durationList)
		return str(round(avgDuration)) + ' Days'
	except ZeroDivisionError:
			return '14 Days'

def insertToDatabase():
	client = MongoClient(db_host)
	db = client[db_name]
	collection_currency = db[db_collection]
	with open('result.json') as f:
	    file_data = json.load(f)
	collection_currency.insert(file_data, check_keys=False)  
	client.close()

def sprintDurationMetric():
	#projects = jira.projects()
	projects = jira.boards()
	data_dict = {}
	for project in projects[:3]:
		data_dict[project.name] = {}
		data_dict[project.name]['id'] = project.id
		#sprints = requests.get( url + project.id, auth=credentials ).json()['sprints']
		sprints = jira.sprints(project.id)
		durationList = []
		for sprint in sprints:
			sprintDetails = assignSprintDetails( detailedSprintInfo(sprint['id']) )
			data_dict[project.name][sprint['name']] = sprintDetails
			durationList.append(sprintDetails['sprint_duration'])
		data_dict[project.name]['average_sprint_duration'] = averageDuration(durationList)
	with open('resultByBoard.json', 'w') as fp:
		json.dump(data_dict, fp, indent=4)

if __name__== "__main__" :
    sprintDurationMetric()
    insertToDatabase()