from flask import Flask, request, jsonify, send_from_directory
import ipaddress
import socket
from urllib.parse import urlparse
from datetime import datetime
import os

app = Flask(__name__)

# Load blacklist (create a sample one if missing)
if not os.path.exists("blacklist.txt"):
    with open("blacklist.txt", "w") as f:
        f.write("192.168.1.99\n10.0.0.1\n8.8.4.4\n1.2.3.4\n")

with open("blacklist.txt") as f:
    blacklist = f.read().splitlines()


def get_ip_from_url(url):
    try:
        if not url.startswith("http"):
            url = "http://" + url
        domain = urlparse(url).netloc
        ip = socket.gethostbyname(domain)
        return ip, domain
    except:
        return None, None


def log_access(ip, protocol, status, reason):
    with open("log.txt", "a", encoding="utf-8") as log:
        ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log.write(f"[{ts}] {ip} ({protocol}) → {status} ({reason})\n")


def firewall(input_value, protocol):
    result = {
        "input": input_value,
        "protocol": protocol,
        "ip": None,
        "domain": None,
        "status": None,
        "reason": None,
        "classification": None,
        "timestamp": datetime.now().strftime("%H:%M:%S"),
    }

    # Detect input type
    try:
        ip = ipaddress.ip_address(input_value)
        result["ip"] = str(ip)
    except:
        ip_str, domain = get_ip_from_url(input_value)
        if ip_str is None:
            result["status"] = "BLOCKED"
            result["reason"] = "Invalid URL or unresolvable domain"
            return result
        ip = ipaddress.ip_address(ip_str)
        result["ip"] = str(ip)
        result["domain"] = domain

    # Rule 0: Unspecified IP
    if ip.is_unspecified or str(ip) == "0.0.0.0":
        result["status"] = "BLOCKED"
        result["reason"] = "Unspecified / Invalid IP"
        log_access(result["ip"], protocol, "BLOCKED", result["reason"])
        return result

    # Rule 1: Blacklist
    if str(ip) in blacklist:
        result["status"] = "BLOCKED"
        result["reason"] = "Blacklisted IP"
        log_access(result["ip"], protocol, "BLOCKED", result["reason"])
        return result

    # Rule 2: Protocol-based checks
    if protocol == "ICMP":
        result["classification"] = "ICMP ping / diagnostic"
    elif protocol == "TCP":
        result["classification"] = "TCP connection request"
    elif protocol == "UDP":
        result["classification"] = "UDP datagram"

    # Rule 3: IP classification
    if ip.is_loopback:
        result["classification"] = "Loopback (localhost)"
    elif ip.is_private:
        result["classification"] = "Private / Internal network"
    elif ip.is_multicast:
        result["classification"] = "Multicast address"
    elif ip.is_reserved:
        result["classification"] = "Reserved IP range"
    else:
        result["classification"] = "Public / Internet-routable"

    result["status"] = "ALLOWED"
    result["reason"] = f"{result['classification']} via {protocol}"
    log_access(result["ip"], protocol, "ALLOWED", result["reason"])
    return result


@app.route("/")
def index():
    return send_from_directory(".", "index.html")


@app.route("/check", methods=["POST"])
def check():
    data = request.get_json()
    ip_input = data.get("ip", "").strip()
    protocol = data.get("protocol", "TCP").strip().upper()

    if not ip_input:
        return jsonify({"error": "No IP provided"}), 400

    result = firewall(ip_input, protocol)
    return jsonify(result)


@app.route("/logs", methods=["GET"])
def get_logs():
    if not os.path.exists("log.txt"):
        return jsonify({"logs": []})
    with open("log.txt") as f:
        lines = f.readlines()
    return jsonify({"logs": [l.strip() for l in lines[-50:]]})  # last 50 logs


if __name__ == "__main__":
    app.run(debug=True, port=5000)