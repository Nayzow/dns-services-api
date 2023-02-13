from app.models.Domain import Domain
from app.services.DomainsService import DomainsService


class DomainsController:

    @staticmethod
    async def find_all_phishing_sites_and_location_by_domain(domain):
        sites = []
        phishing_sites = await DomainsService.find_all_phishing_sites_by_domain(domain)
        for site in phishing_sites:
            sites.append(await DomainsController.data_to_object(site))
        return sites

    @staticmethod
    async def find_all_phishing_sites_by_domain(domain):
        return await DomainsService.find_all_phishing_sites_by_domain(domain)

    @staticmethod
    async def find_data_by_domain(domain):
        return await DomainsController.data_to_object(domain)

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
    async def data_to_object(domain_name):
        ip = await DomainsService.find_ip_by_domain(domain_name)
        available = await DomainsService.find_available_domain(domain_name)
        location = await DomainsService.find_location_by_domain(domain_name)

        return Domain(
            domain_name,
            ip,
            available,
            location
        )
