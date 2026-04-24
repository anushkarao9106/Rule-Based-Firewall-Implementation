# Hybrid Rule-Based Firewall

## 📌 About

This project is a simple firewall simulation that filters network requests using both **URLs and IP addresses**.

When we enter a website name, it gets converted into an IP address using DNS. In this project, we first resolve the URL into an IP and then apply filtering rules on that IP.

The goal of this project was to understand how firewall systems work at a basic level. We also used Wireshark to observe real network activity like DNS requests and ping packets.

---

## 🚀 What it does

* Takes input as URL or IP
* Converts URL → IP using DNS resolution
* Checks whether the request should be allowed or blocked
* Uses rules like:

  * Blacklist checking
  * IP classification (public/private, etc.)
* Stores the result in a log file

---

## 🧠 How it works

1. User enters a URL or IP
2. If it’s a URL → DNS resolution is performed
3. The IP is checked against rules:

   * Whether it is in the blacklist
   * What type of IP it is
4. Based on this, the request is:

   * Allowed
   * Blocked
5. The result is saved in a log file

---

## 🛠️ Tech Used

* Python
* Basic Networking Concepts (DNS, IP, ICMP)
* Wireshark

---

## ⚙️ How to Run

You can run the project using Command Prompt:

```bash
git clone https://github.com/your-username/firewall-project.git
cd firewall-project
python main.py
```

No extra setup is required apart from Python.

---

## 📂 Files

* `main.py` → Main firewall logic
* `blacklist.txt` → List of blocked IPs/URLs (editable)
* `logs.txt` → Sample log file

---

## 🧾 Blacklist

The blacklist is customizable.

You can add:

* IP addresses
* URLs

Example:

```
123.45.67.89
example.com
```

If the input matches anything in this file, it will be blocked.

---

## 📁 Log File

`logs.txt` is a sample file showing how logs are stored.

Actual logs will update when the program runs.

Each entry includes:

* Timestamp
* IP / URL
* Action (ALLOW / BLOCK)
* Reason

---

## 📊 Output

When you run the program, it shows:

* Resolved IP address
* IP classification
* Firewall decision (ALLOW / BLOCK)
* Ping result

You can also open Wireshark to observe real network activity:

* DNS requests and responses
* ICMP (ping) packets

This helps connect what the code is doing with actual network behavior.
