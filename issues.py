import json
from jira import JIRA
import requests
import os
print(os.environ['JIRA_SERVER_URL'])
print(os.environ['JIRA_USERNAME'])
print(os.environ['JIRA_PASSWORD'])
'''options = {'server': 'https://altimetrik.atlassian.net'}
credentials = ('farid.roshan@altimetrik.com', 'cA1AvOAgGdMaccejfgwy8919')
jira = JIRA(options, basic_auth=credentials)

jiraResponse3 = jira.search_issues("project=DC  and IssueType=10003 and 'Fields'=assignee",maxResults=1000)
print(jiraResponse3)'''