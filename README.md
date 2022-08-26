# 3dmd_research_scripts
I created these scripts to automate tasks when conducting research using 3dMD systems

setup_3dmd_session.py 
 1. Generates an xml file that can be imported to 3dMD systems' software. 
 2. The xml file with generate 60 unique IDs for each recording of the collection session.
 3. Generates a yaml file containing the 60 unique IDs. This yaml file can be used for several purposes. (refer to example_output.yaml)

upload_ht_data.py is an example of how the yaml file can be used (refer to example_with_gestures.yaml) 
  1. This script uses Datalab CLI which was scheduled to be deprecated on August 11, 2022.
  2. Once the yaml file is edited it is able to upload the data to a GCP database with the proper tags.



