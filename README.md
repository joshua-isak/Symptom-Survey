# Symptom-Survey
A python script for automatically filling out BU's Covid-19 symptom survey.



## Usage
Install selenium with pip as well as the Firefox web driver (change the code to fit another web driver if you would like).

Change the login constants at the start of the script with you BU Kerberos login credentials.

Before running this script ensure that you have used 2fA on the web browser this is running on and set the option to remember this device for 30 days. You will still have to use a 2fA method every 30 days.

For best results pair this script with a batchfile to automatically execute it every morning using Windows Task Scheduler, or the relevant automator for your platform.
