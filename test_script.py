import requests
from ping3 import ping, verbose_ping

def http_monitoring(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        print(f"HTTP Monitoring - {url} is UP. Status Code: {response.status_code}")
        return True
    except requests.exceptions.RequestException as e:
        print(f"HTTP Monitoring - {url} is DOWN. Error: {e}")
        return False

def icmp_ping_monitoring(host):
    try:
        result = ping(host)
        if result is not None:
            print(f"ICMP Ping Monitoring - {host} is UP. Response Time: {result} ms")
            return True
        else:
            print(f"ICMP Ping Monitoring - {host} is DOWN.")
            return False
    except Exception as e:
        print(f"ICMP Ping Monitoring - {host} is DOWN. Error: {e}")
        return False

if __name__ == "__main__":
    # Example usage
    http_url = "https://wash.upande.com/"
    icmp_host = "upande.com"

    http_monitoring(http_url)
    icmp_ping_monitoring(icmp_host)
