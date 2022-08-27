import os
from pathlib import Path
import yaml
import subprocess

# This script uploads the data to a GCP database
# This script automates tagging of different gestures for each recording using a yaml file
# Datalab CLI was scheduled to be deprecated on August 11, 2022

study_id = input('Please enter study ID: ')
subject_id = input('Please enter subject ID: ')
sessionlabel = study_id + "_" + subject_id
hand_tag = 'tag/hand/' + input('What hand did they use? ')
yaml_path = '/directory/' + sessionlabel + ".yaml" # directory to session yaml
    
session_dir = Path('/directory/' + sessionlabel).iterdir()   # directory to 3dMD data


def add_gesture(unique_id):
    with open (yaml_path, 'r') as f:
        id_yaml = yaml.safe_load(f)
        for x in id_yaml['ids']:
            for k, v in x.items():
                if k == unique_id:
                    gesture = v[0]
                    return gesture

def create_recording(sequence, gesture):
    title = sessionlabel + '_' + str(sequence)
    recording = ('lab datasets recordings create --title ' \
		+ title + ' --tag tag/subject/' + subject_id + ' --tag tag/study/' + study_id + ' --tag tag/sessionlabel/' \
		+ sessionlabel + " --tag tag/3dmd" + " --tag tag/gesture/"
		+ str(gesture) + ' --tag ' + hand_tag + ' --completed --namespace namespace --project project') 
    recording_id = subprocess.check_output(recording, shell=True)
    return (recording_id.decode('utf-8')[76:90])

def upload_recording(directory, recording_id):
    upload = 'lab datasets files upload --namespace namespace --recording ' + recording_id + ' --storage-class files ' + str(directory)
    subprocess.check_call(upload, shell=True)
    
for x in session_dir:
    unique_id = str(x)
    upload_recording(x, create_recording(unique_id, add_gesture(unique_id)))

 
