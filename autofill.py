# A script that autofills BU's Covid-19 Symptom Screen (As of 9/7/2020)
# Joshua Isak 2020
USERNAME = ""
PASSWORD = ""
# Add some real page load checking you cheat...
LOADTIME = 1

import selenium
from selenium import webdriver
import time

# Use Firefox as our browser
driver = webdriver.Firefox()

# Open the website
driver.get("https://patientconnect.bu.edu")

# Enter our username
user_form = driver.find_element_by_id("j_username")
user_form.send_keys(USERNAME)

# Enter our password
psswd_form = driver.find_element_by_id("j_password")
psswd_form.send_keys(PASSWORD)

# Press the login button
login_button = driver.find_element_by_name("_eventId_proceed")
login_button.click()

# Navigate to the survey
time.sleep(LOADTIME)    # allot some time for the page to load...
driver.get("https://patientconnect.bu.edu/Mvc/Patients/QuarantineSurvey")
time.sleep(LOADTIME)
driver.get("https://patientconnect.bu.edu/CheckIn/Survey/ShowAll/21")

# Fill out the survey
q1 = driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/main/form/div[2]/fieldset/div/div[1]")
q2 = driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/main/form/div[3]/fieldset/div/div[1]")
q3 = driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/main/form/div[4]/fieldset/div/div[1]")
q4 = driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/main/form/div[5]/fieldset/div/div[1]")
q5 = driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/main/form/div[6]/fieldset/div/div[1]")
q6 = driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/main/form/div[7]/fieldset/div/div[1]")
q7 = driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/main/form/div[8]/fieldset/div/div[1]")
q8 = driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/main/form/div[9]/fieldset/div/div[1]")

q1.click()
q2.click()
q3.click()
q4.click()
q5.click()
q6.click()
q7.click()
q8.click()

# Submit the survey
submit = driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/footer/div/div[2]/input")
submit.click()

# Make sure that survey submits...
time.sleep(LOADTIME)

# Close the driver
driver.close()
