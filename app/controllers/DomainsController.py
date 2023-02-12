from app.models.Domain import Domain
from app.services.DomainsService import DomainsService


class DnsController:

    @staticmethod
    async def find_all_phishing_sites_by_domain(domain):
        return await DomainsService.find_all_phishing_sites_by_domain(domain)

    @staticmethod
    async def find_location_by_domain(domain):
        return await DomainsService.find_location_by_domain(domain)

    @staticmethod
    async def find_ip_by_domain(domain):
        return await DomainsService.find_ip_by_domain(domain)

    @staticmethod
    async def find_available_domain(domain):
        return await DomainsService.find_available_domain(domain)

    @staticmethod
    async def data_to_object(site):
        domain = site["domain"]
        hexadecimal = site["domain_as_hexadecimal"]
        ip = await DomainsService.find_ip_by_domain(domain)
        location = await DomainsService.find_location_by_domain(domain)

        return Domain(
            domain,
            hexadecimal,
            ip,
            location
        )
