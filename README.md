# DNS-Based Ad Blocker

A lightweight Python-based DNS proxy that intercepts DNS queries on `127.0.0.1` and blocks domains based on a user-defined blacklist. Acts as a local DNS forwarder while filtering out ad and tracking domains, offering system-wide ad-blocking functionality.

---

## 🚀 Features

- 🚫 Blocks domains listed in a `blocked.txt` file
- 📡 Intercepts and parses DNS requests manually
- 🔄 Forwards allowed DNS traffic to an upstream DNS server (Google DNS)
- 🔒 Runs locally and requires no browser plugins
- 💻 Compatible with Linux and Windows

---

## 📂 Setup

- Ensure the system is configured to use `127.0.0.1` as the only DNS server.  
- Turn off "Use Secure DNS" in your browser.

---

## 🧪 Usage

### Run the script:

```bash
python adblocker.py
```
