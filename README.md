Hybrid Rule-Based Firewall

(DNS Resolution + IP Filtering)

About

This project is a basic firewall simulation where we try to filter network requests using both URLs and IP addresses.

Normally when we type something like a website name, it gets converted into an IP using DNS. So instead of directly filtering only IPs, this project first resolves the URL and then applies rules on the IP.

The main idea was to understand how firewalls actually work at a simple level. We also used Wireshark to see what’s really happening in the network when DNS requests and ping packets are sent.

What it does
Takes input as URL or IP
Converts URL to IP using DNS
Checks if it should be allowed or blocked
Uses simple rules like:
blacklist checking
IP type (public/private etc.)
Stores the result in a log file
How it works (in short)
Enter URL/IP
If URL → DNS converts it to IP
Firewall checks:
whether it’s in blacklist
what type of IP it is
Then it either allows or blocks the request
Everything gets logged

The full flow is shown in the diagram in the report (page 5).

Tech used
Python
Basic networking (DNS, IP, ICMP)
Wireshark
How to run

You can run it directly using Command Prompt (CMD):

git clone https://github.com/your-username/firewall-project.git
cd firewall-project
python main.py

That’s all, nothing complicated.

Files
main.py → main code
blacklist.txt → where blocked IPs/URLs are stored
logs.txt → sample log file
Blacklist
You can edit blacklist.txt anytime
Add IPs or URLs depending on what you want to block

Example:

123.45.67.89
example.com

If something matches this list, it gets blocked

Log file
The logs.txt file is just a sample
It’s there to show how the data will be stored

Actual logs will keep updating when you run the program

Each entry usually has:

time
IP / URL
action (allow/block)
reason
Output

When you run it, you’ll see:

resolved IP
IP type
whether it’s allowed or blocked
ping result

Also, if you open Wireshark, you can actually see:

DNS requests happening
ICMP (ping) packets

So you can connect what your code is doing with real network traffic.
