🛡️ TCP Port Scanner

A simple multithreaded TCP port scanner written in Python.
This tool is designed for educational and cybersecurity learning purposes.

⚙️ Features
🔍 Scans ports from 1 to 1024
⚡ Multi-threaded scanning (fast execution)
🌐 Domain → IP resolution
📡 Detects open TCP ports
🧾 Basic service/banner detection
💾 Saves results to a file (scan_results.txt)
🚀 How It Works

The scanner:

Takes a domain or IP address as input
Resolves domain to IP (if needed)
Scans ports using multi-threading
Detects open ports via TCP connection
Tries to read service banners
Saves results to a text file
📦 Installation

Clone the repository:

git clone https://github.com/your-username/port-scanner.git
cd port-scanner
▶️ Usage

Run the script:

python scanner.py

Then enter target:

Hedef (IP veya domain) gir: example.com
📄 Output Example
[+] Port 80 AÇIK | Servis: HTTP
[+] Port 443 AÇIK | Servis: HTTPS

Results are saved in:

scan_results.txt
⚠️ Disclaimer

This tool is created for educational purposes only.
Do not use it on networks or systems without permission.

Unauthorized scanning may be illegal.

🧠 Technologies Used
Python 3
socket library
concurrent.futures (ThreadPoolExecutor)
datetime
📌 Future Improvements
Full port range scanning (1–65535)
JSON/CSV export
GUI version
Stealth scanning mode (SYN scan)
Service detection improvements

👨‍💻 Author
ESMA ŞİŞMAN
