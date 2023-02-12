from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.controllers.DomainsController import DnsController

app = FastAPI()

origins = [
    "http://localhost:4200",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["*"],
)


@app.get("/phishing/{domain}")
async def find_phishing_sites_by_domain(domain):
    return await DnsController.find_all_phishing_sites_by_domain(domain)


@app.get("/ip/{domain}")
async def find_ip_by_domain(domain):
    return await DnsController.find_ip_by_domain(domain)


@app.get("/location/{domain}")
async def find_location_by_domain(domain):
    return await DnsController.find_location_by_domain(domain)


@app.get("/available/{domain}")
async def find_available_domain(domain):
    return await DnsController.find_available_domain(domain)
