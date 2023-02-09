import requests


class DnsService:
    URL_PHISHING = "https://dnstwister.report/api/fuzz/"
    URL_DOMAIN_TO_HEXA = "https://dnstwister.report/api/to_hex/"
    URL_IP = "https://dnstwister.report/api/ip/"
    URL_LOCATION = "http://ip-api.com/json/"

    @staticmethod
    def convert_to_hexadecimal(dns):
        return requests.get(DnsService.URL_DOMAIN_TO_HEXA + dns).json()["domain_as_hexadecimal"]

    @staticmethod
    def phishing_sites_from_name(name):
        hexadecimal = DnsService.convert_to_hexadecimal(name)
        response = requests.get(DnsService.URL_PHISHING + hexadecimal)
        return response.json()["fuzzy_domains"]

    @staticmethod
    def phishing_sites_from_hexadecimal(hexadecimal):
        response = requests.get(DnsService.URL_PHISHING + hexadecimal)
        return response.json()["fuzzy_domains"]

    @staticmethod
    def ip_from_name(name):
        data = DnsService.convert_to_hexadecimal(name)
        response = requests.get(DnsService.URL_IP + data)
        return response.json()["ip"]

    @staticmethod
    def location_from_ip(ip):
        response = requests.get(DnsService.URL_LOCATION + ip)
        return response.json()

    @staticmethod
    def location_from_dns(dns):
        ip = DnsService.ip_from_name(dns)
        return DnsService.location_from_ip(ip)
