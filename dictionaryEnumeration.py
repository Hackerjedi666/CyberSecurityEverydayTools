import requests 
import sys 

sub_list = open("Your wordlist path").read() 
directories = sub_list.splitlines()

for dir in directories:
    dir_enum = f"http://{sys.argv[1]}/{dir}.html" 
    r = requests.get(dir_enum)
    if r.status_code==404: 
        print("404 not found")
    else:
        print("Valid directory:" ,dir_enum)

