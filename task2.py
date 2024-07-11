import os

shells = os.system(' curl   "https://europe-west1-dataimpact-preproduction.cloudfunctions.net/recruitement_test_requests?task=2"')

print(shells) # i used os library to excute shell comande thene i print the result 'Good job! Now we don't know who you are 🫣'

