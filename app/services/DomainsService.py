import requests


class DomainsService:
    URL_PHISHING_API = "https://dnstwister.report/api/fuzz/"
    URL_DOMAIN_TO_HEXA_API = "https://dnstwister.report/api/to_hex/"
    URL_IP_API = "https://dnstwister.report/api/ip/"
    URL_LOCATION_API = "http://ip-api.com/json/"
    URL_MX_API = "https://dnstwister.report/api/mx/"

    @staticmethod
    def handle_request_errors(response):
        try:
            response.raise_for_status()
            return response.json()

        except requests.exceptions.HTTPError as errh:
            return {"error": f"HTTP error: {errh}"}
        except requests.exceptions.ConnectionError as errc:
            return {"error": f"Connection error: {errc}"}
        except requests.exceptions.Timeout as errt:
            return {"error": f"Timeout error: {errt}"}
        except requests.exceptions.RequestException as err:
            return {"error": f"Unknown error: {err}"}

    @staticmethod
    async def convert_to_hexadecimal(domain: str) -> str:
        url = DomainsService.URL_DOMAIN_TO_HEXA_API + domain
        response = requests.get(url)
        return DomainsService.handle_request_errors(response)["domain_as_hexadecimal"]

    @staticmethod
    async def find_data_by_domain(domain: str) -> str:
        url = DomainsService.URL_DOMAIN_TO_HEXA_API + domain
        response = requests.get(url)
        return DomainsService.handle_request_errors(response)

    @staticmethod
    async def find_all_phishing_sites_by_domain(domain: str) -> str:
        hexadecimal = await DomainsService.convert_to_hexadecimal(domain)
        url = DomainsService.URL_PHISHING_API + hexadecimal
        response = requests.get(url)
        return DomainsService.handle_request_errors(response)["fuzzy_domains"]

    @staticmethod
    async def find_all_phishing_sites_by_domain_hexadecimal(hexadecimal: str) -> str:
        url = DomainsService.URL_PHISHING_API + hexadecimal
        response = requests.get(url)
        return DomainsService.handle_request_errors(response)

    @staticmethod
    async def find_ip_by_domain(domain: str) -> str:
        hexadecimal = await DomainsService.convert_to_hexadecimal(domain)
        url = DomainsService.URL_IP_API + hexadecimal
        response = requests.get(url)
        return DomainsService.handle_request_errors(response)["ip"]

    @staticmethod
    async def find_location_by_ip(ip: str) -> str:
        url = DomainsService.URL_LOCATION_API + ip + "?fields=continent,country,regionName,city,zip,lat,lon,timezone,currency,isp,org,reverse,mobile,proxy,hosting,query"
        response = requests.get(url)
        return DomainsService.handle_request_errors(response)

    @staticmethod
    async def find_location_by_domain(domain: str) -> str:
        ip = await DomainsService.find_ip_by_domain(domain)
        return await DomainsService.find_location_by_ip(ip) if ip else {"error": "No IP found"}

    @staticmethod
    async def find_if_domain_is_available(domain: str) -> bool:
        url = DomainsService.URL_MX_API + await DomainsService.convert_to_hexadecimal(domain)
        response = requests.get(url)
        return DomainsService.handle_request_errors(response)["mx"] == []
