import socket
import requests
import pprint
import json
from urllib.parse import urlparse


def get_ip_geolocation(domain_input: str):
    raw_input = domain_input.strip()
    hostname = urlparse(raw_input).netloc or raw_input.split("/")[0]

    if not hostname:
        print("Error: Domain tidak boleh kosong.")
        return

    try:
        ip_address = socket.gethostbyname(hostname)
        print(f"Target : {hostname}")
        print(f"IPv4   : {ip_address}\n")
    except socket.gaierror:
        print(f"Error: Domain '{hostname}' tidak ditemukan atau koneksi DNS bermasalah.")
        return

    try:
        request_url = f"http://geolocation-db.com/jsonp/{ip_address}"
        response = requests.get(request_url, timeout=10)
        response.raise_for_status()

        geolocation_str = response.content.decode("utf-8")
        geolocation_json = geolocation_str.split("(", 1)[1].rsplit(")", 1)[0]
        geolocation = json.loads(geolocation_json)

        print("--- Geolocation Info ---")
        for k, v in geolocation.items():
            pprint.pprint(f"{k} : {v}")

        lat = geolocation.get("latitude")
        lon = geolocation.get("longitude")
        if lat and lon:
            print(f"\nGoogle Maps: https://www.google.com/maps?q={lat},{lon}")

    except requests.RequestException as e:
        print(f"Error saat mengambil data geolokasi: {e}")
    except (IndexError, json.JSONDecodeError):
        print("Error: Gagal memproses format respons dari API geolokasi.")


if __name__ == "__main__":
    domain = input("Enter a domain name: ")
    get_ip_geolocation(domain)
