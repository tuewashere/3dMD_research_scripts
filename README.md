# 3dmd_research_scripts
I created these scripts to automate tasks when conducting hand tracking research using 3dMD systems (https://3dmd.com/). 

The scripts were originally used for the 3dMDhand system but can be adapted for other 3dMD systems. 
 - A 10 second 4D recording from a 3dMDhand system can be ~30GBs. 
 - The 3dMDhand system can export/process ~50,000 frames in 8 hours. 
 - Managing this amount of data and throughput can be difficult and these scripts should help with the collection process

**setup_3dmd_session.py** generates an session xml file that can be imported to 3dMD systems' software. The script will also generate 60 unique IDs for each recording of a collection session. It also creates a session yaml file containing the 60 unique IDs. This session yaml file can be used for several purposes. **template.yaml** and **session_template.xml** are required files for the script to work. 

**upload_ht_data.py** is an example of how the session yaml file can be used. Once the session yaml file is edited, this script is able to upload the data to a GCP database with the proper gesture tags (refer to example_with_gestures.yaml). This script uses Datalab CLI which was scheduled to be deprecated on August 11, 2022.

**frame_metrics.py** is another example of how the session yaml file can be used. It is important to keep track of frame counts for 3dMD data because exporting/processing is resource heavy. By tracking which gestures have higher frame counts, adjustments to the collection protocol can be made. This script generates a txt file with the total amount of frames collected for a session and how many frames were collected per gesture group.


  


