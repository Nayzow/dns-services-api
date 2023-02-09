from fastapi import FastAPI
from app.services.DnsService import DnsService

app = FastAPI()


@app.get("/phishing/{dns}")
async def phishing_sites_from_name(dns):
    return DnsService.phishing_sites_from_name(dns)


@app.get("/phishing/hexa/{dns}")
async def phishing_sites_from_hexadecimal(dns):
    return DnsService.phishing_sites_from_hexadecimal(dns)


@app.get("/ip/{dns}")
async def ip_from_dns(dns):
    return DnsService.ip_from_name(dns)


@app.get("/location/{dns}")
async def location_from_dns(dns):
    return DnsService.location_from_dns(dns)
