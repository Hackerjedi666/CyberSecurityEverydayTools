import requests

# Creating a function to download any file from the internet

def download(url):
	getResponse = requests.get(url)
	urlList = url.split("/")[-1] # So that it gets the name of the image

	with open(urlList, "wb") as out_file: # wb because the file is binary
		out_file.write(getResponse.content) # getting binary content of that image


download("https://imgd.aeplcdn.com/370x208/n/cw/ec/130591/fronx-exterior-right-front-three-quarter-109.jpeg")