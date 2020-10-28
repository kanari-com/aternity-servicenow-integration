from __app__.shared_code import config
import requests
import logging

service_now_event_template = {
    "records": [{
        "source": "Aternity",
        "event_class": "",
        # "node": "name.of.node.com",
        # "metric_name": "Percentage Logical Disk Free Space",
        # "type": "Disk space",
        # "severity": "4",
        "message_key": "key-here",
        "description": "The disk C: on computer V-W2K8-dfg.dfg.com is running out of disk space. The value that exceeded the threshold is 41% free space.",
        "additional_info": {
        #"dynatrace-severity": "",
        #"metric-value": "",
        "key": "",
        "application" : "",
        #"agents" : "",
        "open": "",
        #"queue_manager" : "",
        #"queue_name": "",
        #"channel_name" : ""
    }
  }]
  }

def push_servicenow_event(service_now_event_template_json):
  r = requests.post(config.SERVICE_NOW_EVENT_URL, auth=(config.SERVICENOW_USER, config.SERVICENOW_PW), json=service_now_event_template_json)
  logging.info(f'Pushed SNOW Event: {r.json()}')