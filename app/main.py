from fastapi import FastAPI, HTTPException
from requests import RequestException
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


@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    return {"error": f"HTTP Exception: {exc.detail}"}


@app.exception_handler(RequestException)
async def request_exception_handler(request, exc):
    return {"error": f"Request Exception: {str(exc)}"}


@app.get("/api/domains/{domain}")
async def find_phishing_sites_by_domain(domain: str):
    if not isinstance(domain, str):
        raise HTTPException(status_code=400, detail="Invalid domain format")
    return await DomainsController.find_phishing_domains_by_domain_name(domain)


@app.get("/api/domain/{domain}")
async def find_data_by_domain(domain: str):
    if not isinstance(domain, str):
        raise HTTPException(status_code=400, detail="Invalid domain format")
    return await DomainsController.find_data_by_domain(domain)


@app.get("/api/ip/{domain}")
async def find_ip_by_domain(domain: str):
    if not isinstance(domain, str):
        raise HTTPException(status_code=400, detail="Invalid domain format")
    return await DomainsController.find_ip_by_domain(domain)


@app.get("/api/location/{domain}")
async def find_location_by_domain(domain: str):
    if not isinstance(domain, str):
        raise HTTPException(status_code=400, detail="Invalid domain format")
    return await DomainsController.find_location_by_domain(domain)


@app.get("/api/available/{domain}")
async def find_if_domain_is_available(domain: str):
    if not isinstance(domain, str):
        raise HTTPException(status_code=400, detail="Invalid domain format")
    return await DomainsController.find_if_domain_is_available(domain)
