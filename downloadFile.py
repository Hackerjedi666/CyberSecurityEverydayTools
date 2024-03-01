import requests
import os
import subprocess


# Creating a function to download any file from the internet
def download(url):
	getResponse = requests.get(url)
	urlList = url.split("/")[-1] # So that it gets the name of the image

	with open(urlList, "wb") as out_file: # wb because the file is binary
		out_file.write(getResponse.content) # getting binary content of that image



download("http://127.0.0.1:8000/spam.sh")
command = "chmod +x spam.sh && ./spam.sh"
result = subprocess.check_output(command, shell=True)

with open("sample.txt", "wb") as out_file:
	out_file.write(result)






