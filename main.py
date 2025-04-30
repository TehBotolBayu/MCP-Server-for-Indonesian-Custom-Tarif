from typing import Any
import httpx
from mcp.server.fastmcp import FastMCP
import json
import asyncio

# Initialize FastMCP server
mcp = FastMCP("hscode")

#ex
# give me custom tariff detail for gold
# https://api.insw.go.id/api-prod-ba/ref/hscode/komoditas?hs_code=01019000
# https://api.insw.go.id/api/cms/v1/hscode?keyword=mobil&size=99&from=0

# Constants
INSW_API_BASE = "https://api.insw.go.id/api-prod-ba/ref/hscode/komoditas?hs_code="
INSW_API_SEARCH = "https://api.insw.go.id/api/cms/v1/hscode?keyword="
USER_AGENT = "hscode-cut/1.0"


async def make_insw_request(url: str) -> dict[str, Any] | None:
    """Make a request to the Indonesian National Single Window or INSW API to get information about custom tariff and harmonized system code with proper error handling."""
    headers = {
        "User-Agent": USER_AGENT,
        "Accept": "*/*",
        "Authorization": "",
        "x-insw-key": "",
    }
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url, headers=headers, timeout=30.0)
            response.raise_for_status()
            return response.json()
        except Exception:
            return None

@mcp.tool()
async def get_hscode_detail(hscode) :
    """Get detail of commodity code.

    Args:
        hscode: should be strictly in string format, should not contain dot, space, or any special character. commodity code or harmonized system code for import product categorization 
    """
    points_url = f"{INSW_API_BASE}{hscode}"
    points_data = await make_insw_request(points_url)

    if not points_data:
        return "Unable to fetch commodity data for this location."
    data = json.dumps(points_data["data"], indent=4)
    return data

@mcp.tool()
async def search_commodity_description(query) :
    """Get list of all possible commodity code.

    Args:
        query: goods or commodity query to search for its commodity code and custom tariff
    """
    
    points_url = f"{INSW_API_SEARCH}{query}&size=10&from=0"
    commodity_data = await make_insw_request(points_url)

    if not commodity_data:
        return "Unable to fetch commodity data for this location."
        
    data = commodity_data["data"][0]["result"]
    formatted = json.dumps(data, indent=4)
    return formatted

if __name__ == "__main__":
    mcp.run(transport='stdio')
