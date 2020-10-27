import logging
import os
import sys
from functools import partial

import azure.functions as func

from __app__.shared_code import aternity
from __app__.shared_code import python_incident_api as functionlogic

def main(mytimer: func.TimerRequest) -> None:
    try:
        aternity_incident_data = aternity.fetch_aternity_incidents()
        functionlogic.push_aternity_incidents_to_snow_events(aternity_incident_data) 
    except Exception as e:
        logging.error(f'Backend Exception: {str(e)}')

    