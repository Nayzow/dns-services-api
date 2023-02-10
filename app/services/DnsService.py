import requests


class DnsService:
    URL_PHISHING_API = "https://dnstwister.report/api/fuzz/"
    URL_DOMAIN_TO_HEXA_API = "https://dnstwister.report/api/to_hex/"
    URL_IP_API = "https://dnstwister.report/api/ip/"
    URL_LOCATION_API = "http://ip-api.com/json/"

    @staticmethod
    async def convert_to_hexadecimal(domain):
        url = DnsService.URL_DOMAIN_TO_HEXA_API + domain
        response = requests.get(url).json()["domain_as_hexadecimal"]
        if response:
            return response
        else:
            return "No data found"

    @staticmethod
    async def find_all_phishing_sites_by_domain(domain):
        hexadecimal = await DnsService.convert_to_hexadecimal(domain)
        url = DnsService.URL_PHISHING_API + hexadecimal
        response = requests.get(url).json()["fuzzy_domains"]
        if response:
            return response
        else:
            return "No data found"

    @staticmethod
    async def find_all_phishing_sites_by_domain_hexadecimal(hexadecimal):
        url = DnsService.URL_PHISHING_API + hexadecimal
        response = requests.get(url).json()["fuzzy_domains"]
        if response:
            return response
        else:
            return "No data found"

    @staticmethod
    async def find_ip_by_domain(domain):
        hexadecimal = await DnsService.convert_to_hexadecimal(domain)
        url = DnsService.URL_IP_API + hexadecimal
        response = requests.get(url).json()["ip"]
        if response:
            return response
        else:
            return "No data found"

    @staticmethod
    async def find_location_by_ip(ip):
        if ip:
            url = DnsService.URL_LOCATION_API + ip
            response = requests.get(url).json()
            if response:
                return response
            else:
                return "No data found"

    @staticmethod
    async def find_location_by_domain(domain):
        ip = await DnsService.find_ip_by_domain(domain)
        return await DnsService.find_location_by_ip(ip)
