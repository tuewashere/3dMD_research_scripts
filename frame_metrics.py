import yaml
import os
from pathlib import Path
import re


study_id = input('Please enter study ID: ')
subject_id = input('Please enter subject ID: ')
session_id = study_id + '_' + subject_id
session_dir = Path('/directory/' + sessionlabel).iterdir() 
yaml_path = '/directory/' + sessionlabel + '.yaml' 

total_frame_count = 0
gestures = {}
protocol = {}

def get_fc(unique_id):
	txt = unique_id + '/meshes/gridreport.txt'
	try:
		f = open (txt)
	except:
		print ('no grid report for ' + unique_id + ' remove the sequence that failed to process and run again')
	else:
		first = f.readline()
		return int(re.search(r'\d+', first).group())

def protocol_metrics(gesture):
	if gesture in protocol.keys():
		count = protocol[gesture]
		count +=1
		protocol[gesture] = count
	else:
	   	protocol[gesture] = 1

def get_gesture(unique_id):
    with open (yaml_path, 'r') as f:
        session_yaml = yaml.safe_load(f)
        for x in session_yaml['ids']:
        	for k, v in x.items():
        		if str(k) in str(unique_id):
        			gesture = v[0]
        			protocol_metrics(gesture)
        			return gesture

def gesture_count(key, frame_count):
	if key in gestures.keys():
		total = gestures[key]
		total += frame_count
		gestures[key] = total
	else:
		gestures[str(key)] = frame_count

def save_metrics(total_fc, gestures_fc, protocol_metrics):
	f = open(sessionlabel + "_metrics.txt", "w+")
	f.write(('total: ' + str(total_frame_count)+"\n"))
	f.write((str(gestures)[1:-1]+"\n"))
	f.write((str(protocol)[1:-1]+"\n"))
	f.close()
	os.system('mv ' + sessionlabel + "_metrics.txt" + " /directory/")


for x in session_dir:
	unique_id = str(x)
	if (unique_id[-8:]) == 'DS_Store':
		continue
	framecount = get_fc(unique_id)
	if framecount == None:
		continue
	total_frame_count += framecount
	gesture_count(get_gesture(timestamp), framecount)

save_metrics(total_frame_count, gestures, protocol)

