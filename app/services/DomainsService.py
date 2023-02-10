import requests


class DomainsService:
    URL_PHISHING_API = "https://dnstwister.report/api/fuzz/"
    URL_DOMAIN_TO_HEXA_API = "https://dnstwister.report/api/to_hex/"
    URL_IP_API = "https://dnstwister.report/api/ip/"
    URL_LOCATION_API = "http://ip-api.com/json/"
    URL_MX_API = "https://dnstwister.report/api/mx/"

    @staticmethod
    async def convert_to_hexadecimal(domain):
        url = DomainsService.URL_DOMAIN_TO_HEXA_API + domain
        response = requests.get(url).json()["domain_as_hexadecimal"]
        if response:
            return response
        else:
            return "No data found"

    @staticmethod
    async def find_all_phishing_sites_by_domain(domain):
        hexadecimal = await DomainsService.convert_to_hexadecimal(domain)
        url = DomainsService.URL_PHISHING_API + hexadecimal
        response = requests.get(url).json()["fuzzy_domains"]
        if response:
            return response
        else:
            return "No data found"

    @staticmethod
    async def find_all_phishing_sites_by_domain_hexadecimal(hexadecimal):
        url = DomainsService.URL_PHISHING_API + hexadecimal
        response = requests.get(url).json()["fuzzy_domains"]
        if response:
            return response
        else:
            return "No data found"

    @staticmethod
    async def find_ip_by_domain(domain):
        hexadecimal = await DomainsService.convert_to_hexadecimal(domain)
        url = DomainsService.URL_IP_API + hexadecimal
        response = requests.get(url).json()["ip"]
        if response:
            return response
        else:
            return "No data found"

    @staticmethod
    async def find_location_by_ip(ip):
        if ip:
            url = DomainsService.URL_LOCATION_API + ip
            response = requests.get(url).json()
            if response:
                return response
            else:
                return "No data found"

    @staticmethod
    async def find_location_by_domain(domain):
        ip = await DomainsService.find_ip_by_domain(domain)
        return await DomainsService.find_location_by_ip(ip)

    @staticmethod
    async def find_available_domain(domain):
        url = DomainsService.URL_MX_API + await DomainsService.convert_to_hexadecimal(domain)
        response = requests.get(url).json()
        if response["mx"]:
            return False
        else:
            return True
