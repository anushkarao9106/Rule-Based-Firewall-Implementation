Hybrid Rule-Based Firewall
DNS Resolution + IP Filtering
About

This project is a basic firewall simulation where we filter network requests using both URLs and IP addresses.

Usually, when we enter a website name, it gets converted into an IP address using DNS. So in this project, we first resolve the URL into an IP and then apply filtering rules on that IP.

The goal was to understand how firewall systems work at a simple level. We also used Wireshark to observe real network activity like DNS requests and ping packets.

What it does
Takes input as URL or IP
Converts URL → IP using DNS
Checks whether it should be allowed or blocked
Uses rules like:
blacklist checking
IP classification (public/private etc.)
Stores the result in a log file
How it works
User enters a URL or IP
If it’s a URL, DNS resolution happens
The IP is then checked against rules:
whether it is in the blacklist
what type of IP it is
Based on this, the request is either:
allowed
blocked
The result is saved in the log file

(The full flow is shown in the network diagram in the report – page 5.)

Tech used
Python
Basic networking concepts (DNS, IP, ICMP)
Wireshark
How to run

You can run the project using Command Prompt (CMD):

git clone https://github.com/your-username/firewall-project.git
cd firewall-project
python main.py

No extra setup is required apart from Python.

Files
main.py → main firewall logic
blacklist.txt → list of blocked IPs/URLs (can be edited)
logs.txt → sample log file
Blacklist
The blacklist is customizable
You can add:
IP addresses
URLs

Example:

123.45.67.89
example.com

If the input matches anything in this file, it will be blocked.

Log file
logs.txt is just a sample file
It shows how logs will be stored

Actual logs will update when the program runs.

Each entry includes:

timestamp
IP / URL
action (ALLOW / BLOCK)
reason
Output

When you run the program, it shows:

resolved IP address
IP classification
firewall decision (allow or block)
ping result

You can also open Wireshark and observe the real implementation, where:

DNS requests and responses are visible
ICMP (ping) packets can be seen

This helps connect what the code is doing with actual network behavior.
