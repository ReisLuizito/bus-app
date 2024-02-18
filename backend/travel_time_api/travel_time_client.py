import asyncio
from traveltimepy import Location, Coordinates, Transportation, TravelTimeSdk


async def main():
    sdk = TravelTimeSdk("8097a90e", "90bf31f1a51cfd508e0d50b0f6ef69a7")

    locations = [
        
    ]

    results = await sdk.time_filter_fast_async(
        locations=locations,
        search_ids={

        },
        transportation=Transportation(type="public_transport"),
        one_to_many=False
    )

    print(results)

asyncio.run(main())
