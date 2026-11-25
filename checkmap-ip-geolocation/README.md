# CheckMap - Domain IP Lookup & Geolocation Tool

A lightweight Python CLI tool built for basic **Network Reconnaissance** in Kali Linux. It resolves a target domain to its IPv4 address, fetches server geolocation data via a public API, and generates a clickable Google Maps link directly in the terminal.

## Features
- **URL Sanitization:** Automatically strips protocols (`http://`, `https://`) and paths using `urllib.parse`, so you can paste either a bare domain or a full URL.
- **DNS Resolution:** Resolves domain names to IPv4 addresses using Python's built-in `socket` library.
- **IP Geolocation:** Fetches country, state, city, and coordinates (`latitude`, `longitude`) from `geolocation-db.com`.
- **Google Maps Integration:** Outputs a direct Google Maps coordinate URL for quick visual inspection.

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/maul2arajak/checkmap-ip-geolocation.git
   cd checkmap-ip-geolocation
   ```

2. Install the required dependency:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the script using Python 3:
```bash
python3 checkmap.py
```

Example output:
```text
Enter a domain name: facebook.com
Target : facebook.com
IPv4   : 57.144.100.1

--- Geolocation Info ---
'country_code : BE'
'country_name : Belgium'
'city : None'
'postal : None'
'latitude : 50.85'
'longitude : 4.35'
'IPv4 : 57.144.100.1'
'state : None'

Google Maps: https://www.google.com/maps?q=50.85,4.35
```

> **Note:** If a target website uses a CDN or WAF (such as Cloudflare), the resolved IP and geolocation will point to the CDN's Anycast/proxy server rather than the website's physical origin server.

## Disclaimer
This tool is intended strictly for educational purposes and authorized network reconnaissance.
