import os
import datetime
import re
import xml.etree.ElementTree as ET
import time
import yaml
import hashlib

# This script helps set up collection sessions for 3dMD systems
# It creates 60 unique ids for sequences and produces an xml file that can imported into 3dMDPerform
# It also produces a yaml file with the unique ids that is used for metadata

study_id = input('Please enter study ID: ')
subject_id = input('Please enter subject ID: ')
session_id = study_id + '_' + subject_id

sequence_label = 'exportdirectory=%2F%2FNAS%2Fvolume1%2Fdata%2F%25sessionlabel%25%2F%25sequencelabel%25&exportimagedir=%25exportdirectory%25%2Fimages&exportmeshdir=%25exportdirectory%25%2Fmeshes&exportsrpfile=P%3A%2Fapp%2Fcfg%2FMLHand12.srp&exportsurfaceformat=obj&overlay=default_overlay&sequencelabel='
xml_path =  '/Users/tue/setup_scripts/session_template.xml' 
yaml_path = '/Users/tue/setup_scripts/template.yaml'   
sequence_tree = ET.parse(xml_path)
root = sequence_tree.getroot()
id_list = list()

def create_unique_id(): 
    unique_id = str(datetime.datetime.now())
    unique_id = re.sub('\W+',' ',unique_id.replace(" ",""))
    unique_id = hashlib.md5(unique_id.encode())
    unique_id = unique_id.hexdigest()
    return (str(unique_id))

def edit_xml():
    for x in root.iter('sequence'):
        x.text = sequence_label + str(create_unique_id())
        sequence = x.text[-12:]
        id_list.append(sequence)
        time.sleep(0.12)

def create_yaml():
    with open (yaml_path, "r") as f:
        data = yaml.safe_load(f)
        data['ids'] = id_list
    with open(yaml_path, 'w') as f:
        yaml.dump(data, f)

edit_xml()
create_yaml()
sequence_tree.write('/Users/tue/setup_scripts/' + session_id + '.xml')
os.system('cp ' + yaml_path + ' ~/setup_scripts/yamls/' + session_id + '.yaml')
print ('Your 3dMD template and yaml file are ready.')




