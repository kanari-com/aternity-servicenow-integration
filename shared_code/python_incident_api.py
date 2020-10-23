from __app__.shared_code import config
import requests, json , pytz  ,copy
import pandas as pd
import datetime as dt
from datetime import datetime, timedelta
from pandas.io.json import json_normalize

from __app__.shared_code import servicenow

#pushing incoming aternity incident data as snow events
def push_aternity_incidents_to_snow_events(aternity_incident_data):
    incident_data_df =  json_normalize(aternity_incident_data ['value'])
    
    if incident_data_df.empty:
        print("No Incident Reported in last 5 minutes" ,incident_data_df )
    else : 
        for index,row in incident_data_df.iterrows():
            snow_event = copy.deepcopy(servicenow.service_now_event_template)
            snow_event['records'][0]['source']='Aternity'
            snow_event['records'][0]['event_class']=''
            snow_event['records'][0]['message_key']=str(row['INCIDENT_ID'])
            snow_event['records'][0]['description']=row['APPLICATION_NAME'] + ' application has issues with ' + row['ACTIVITY_NAME'] + ' activity'
            
            if str(row['INCIDENT_STATE']).lower() == 'open':
                snow_event['records'][0]['additional_info']['open']='True'
            else: 
                print(snow_event['records'][0]['additional_info'])
                snow_event['records'][0]['additional_info']['open']='False'

            snow_event['records'][0]['additional_info']['key'] = str(row['ACTIVITY_ID'])
            snow_event['records'][0]['additional_info']['application'] = row['APPLICATION_NAME'] + ' - ' + row['ACTIVITY_NAME']
            snow_event['records'][0]['additional_info'] = json.dumps(snow_event['records'][0]['additional_info'])
            
            servicenow.push_servicenow_event(snow_event)
