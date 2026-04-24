# Hybrid Rule-Based Firewall

## 📌 About

This project is a simple firewall simulation that filters network requests using both **URLs and IP addresses**.

Normally, when we enter a website name, it gets converted into an IP address using DNS. In this project, we first resolve the URL into an IP and then apply filtering rules on that IP.

The main aim was to understand how firewall systems work at a basic level. We also used Wireshark to observe real network activity like DNS requests and ping packets.

---

## 🧠 How it works

1. User enters a URL or IP
2. If it’s a URL → DNS resolution is performed
3. The IP is checked against rules:

   * Whether it is in the blacklist
   * What type of IP it is (public/private, etc.)
4. Based on this, the request is:

   * Allowed
   * Blocked
5. The result is saved in a log file

---

## 🛠️ Tech Used

* Python
* Basic Networking Concepts (DNS, IP, ICMP)
* Wireshark
* HTML
* CSS

---

## ⚙️ How to Run

### ▶️ Run using Command Line (CLI)

```bash id="cli123"
git clone https://github.com/your-username/firewall-project.git
cd firewall-project
python main.py
```

---

### 🌐 Run with UI (Recommended)

```bash id="ui123"
python app.py
```

Then open the local server link shown in the terminal.

👉 This version provides a **simple UI/UX interface** to enter URL/IP and view results more easily.

---

## 📂 Files

* `main.py` → Core firewall logic (CLI version)
* `app.py` → Web application for UI-based interaction
* `index.html` → Frontend interface
* `blacklist.txt` → List of blocked IPs/URLs (editable)
* `log.txt` → Stores firewall logs

---

## 🧾 Blacklist

The blacklist is customizable.

You can add:

* IP addresses
* URLs

Example:

```id="blk123"
123.45.67.89
example.com
```

If the input matches anything in this file, it will be blocked.

---

## 📁 Log File

`log.txt` is a sample file showing how logs are stored.

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

If you use the UI (`app.py`), the results are displayed in a cleaner and more interactive way.

---

## 🔍 Using Wireshark

You can open Wireshark while running this project to observe:

* DNS requests and responses
* ICMP (ping) packets

This helps connect the code with real network behavior.

---

## 📌 Final Note

This project is mainly for learning purposes and gives a basic idea of how firewall systems work using simple rule-based filtering.
