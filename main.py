import ipaddress
import socket
from urllib.parse import urlparse
import os

# Load blacklist
with open("blacklist.txt") as f:
    blacklist = f.read().splitlines()

def get_ip_from_url(url):
    try:
        domain = urlparse(url).netloc
        ip = socket.gethostbyname(domain)
        return ip, domain
    except:
        return None, None

def log_access(ip, status):
    with open("log.txt", "a") as log:
        log.write(f"{ip} - {status}\n")

def firewall(input_value):
    print("\n Input:", input_value)

    # STEP 1: Detect input type
    try:
        ip = ipaddress.ip_address(input_value)
        print(" IP Address:", ip)
    except:
        # Treat as URL
        ip_str, domain = get_ip_from_url(input_value)
        if ip_str is None:
            print(" Invalid URL")
            return
        ip = ipaddress.ip_address(ip_str)
        print(" Domain:", domain)
        print(" Resolved IP:", ip)

    # STEP 2: Apply rules

    # ⭐ Rule 0: Invalid / unspecified IP
    if ip.is_unspecified or str(ip) == "0.0.0.0":
        print(" Warning: Invalid IP (unspecified)")
        print(" Firewall Decision: BLOCKED")
        print(" Rule Triggered: Unspecified IP Check")
        log_access(ip, "BLOCKED")
        return

    # ⭐ Rule 1: Blacklist
    if str(ip) in blacklist:
        print(" BLOCKED (Blacklisted IP)")
        print(" Rule Triggered: Blacklist Check")
        log_access(ip, "BLOCKED")
        return

    # ⭐ Rule 2: IP Classification
    if ip.is_loopback:
        print(" Warning: Loopback address (localhost)")
        print(" Rule Triggered: Loopback Check")

    elif ip.is_private:
        print(" Warning: Private IP (internal network)")
        print(" Rule Triggered: Private IP Check")

    elif ip.is_multicast:
        print(" Warning: Multicast IP")
        print(" Rule Triggered: Multicast Check")

    elif ip.is_reserved:
        print(" Warning: Reserved IP")
        print(" Rule Triggered: Reserved IP Check")

    else:
        print(" Public IP (internet routable)")
        print(" Rule Triggered: Public IP Check")

    # Final decision
    print(" Firewall Decision: ALLOWED")
    log_access(ip, "ALLOWED")

    # Send ping (network activity)
    print(" Sending test packet (ping)...")
    os.system(f"ping -n 1 {ip}")


# ⭐ Menu system
while True:
    print("\n========== FIREWALL SYSTEM ==========")
    print("1. Check IP/URL")
    print("2. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        user_input = input("\nEnter URL or IP: ")
        firewall(user_input)

    elif choice == "2":
        print(" Exiting Firewall System...")
        break

    else:
        print(" Invalid choice")