import asyncio
from traveltimepy import TravelTimeSdk


async def main():
    sdk = TravelTimeSdk("8097a90e", "90bf31f1a51cfd508e0d50b0f6ef69a7")

    results = await sdk.geocoding_async(query="Parliament square", limit=30)
    print(results.features)

asyncio.run(main())
