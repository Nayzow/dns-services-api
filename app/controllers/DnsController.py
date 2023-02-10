from app.models.Dns import Dns
from app.services.DnsService import DnsService


class DnsController:

    @staticmethod
    async def find_all_phishing_sites_and_location_by_domain(domain):
        sites = []
        phishing_sites = await DnsService.find_all_phishing_sites_by_domain(domain)
        for site in phishing_sites:
            sites.append(await DnsController.data_to_object(site))
        return sites

    @staticmethod
    async def find_all_phishing_sites_by_domain(domain):
        return await DnsService.find_all_phishing_sites_by_domain(domain)

    @staticmethod
    async def find_location_by_domain(domain):
        return await DnsService.find_location_by_domain(domain)

    @staticmethod
    async def find_ip_by_domain(domain):
        return await DnsService.find_ip_by_domain(domain)

    @staticmethod
    async def data_to_object(site):
        domain = site["domain"]
        hexadecimal = site["domain_as_hexadecimal"]
        ip = await DnsService.find_ip_by_domain(domain)
        location = await DnsService.find_location_by_domain(domain)

        return Dns(
            domain,
            hexadecimal,
            ip,
            location
        )
