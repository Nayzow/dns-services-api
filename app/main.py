from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.controllers.DomainsController import DomainsController

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


@app.get("/api/domains/{domain}")
async def find_phishing_sites_by_domain(domain):
    return await DomainsController.find_all_phishing_sites_by_domain(domain)


@app.get("/api/domain/{domain}")
async def find_data_by_domain(domain):
    return await DomainsController.find_data_by_domain(domain)


@app.get("/api/ip/{domain}")
async def find_ip_by_domain(domain):
    return await DomainsController.find_ip_by_domain(domain)


@app.get("/api/location/{domain}")
async def find_location_by_domain(domain):
    return await DomainsController.find_location_by_domain(domain)


@app.get("/api/available/{domain}")
async def find_if_domain_is_available(domain):
    return await DomainsController.find_available_domain(domain)
