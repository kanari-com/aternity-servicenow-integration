import pytz
import logging
import requests
from __app__.shared_code import config
from datetime import datetime, timedelta
import datetime as dt

def fetch_aternity_incidents():
    time_now = dt.datetime.now().astimezone().replace(microsecond=0).isoformat()  # UTC ISO861 Time Now
    time_10min_ago = (dt.datetime.now(pytz.utc) - timedelta(seconds=600)).astimezone().replace(microsecond=0).isoformat()  # UTC ISO861 Time 1 min ago

    url= config.ATERNITY_INCIDENT_URL+'?$filter=(INCIDENT_CREATION_TIMESTAMP gt 2010-01-01T12:00:00+00:00 and INCIDENT_LAST_UPDATE_TIMESTAMP gt '+ str(time_10min_ago) +' and INCIDENT_LAST_UPDATE_TIMESTAMP lt ' + str(time_now)+')'
    #url = config.ATERNITY_INCIDENT_URL+"?$filter=(INCIDENT_CREATION_TIMESTAMP gt 2020-08-02T09:00:00+01:00 and INCIDENT_CREATION_TIMESTAMP lt " + time_now + ")"
    #url= config.ATERNITY_INCIDENT_URL+"$filter=relative_time(last_15_minutes)"
    #url = config.ATERNITY_INCIDENT_URL+"?$filter=(INCIDENT_CREATION_TIMESTAMP gt "+ str(time_5min_ago) +" and INCIDENT_CREATION_TIMESTAMP lt " + str(time_now) + ")"
    #url= config.ATERNITY_INCIDENT_URL+"?$filter=(INCIDENT_CREATION_TIMESTAMP gt 2020-09-02T09:00:00+01:00 and INCIDENT_CREATION_TIMESTAMP lt 2020-09-02T12:00:00+01:00)'"
    r = requests.get(url, auth=(config.ATERNITY_USER, config.ATERNITY_PW))
    incident_data = r.json()
    logging.info(f'Incident Data From Aternity: {incident_data}')
    return incident_data

