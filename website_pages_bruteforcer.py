import requests
def request(url):
    try:
        get_response = requests.get("https://" + url)
        return get_response
    except requests.exceptions.ConnectionError:
        pass
target_url = input("Enter your url --> ")

with open("Your wordlist path") as wordlist_file:
    for line in wordlist_file:
        word = line.strip()
        test_url = target_url + '/' + word
        response = request(test_url)
        if response:
            print("[+] Discovered URL --> " + test_url)
             
