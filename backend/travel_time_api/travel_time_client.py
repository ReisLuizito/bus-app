import asyncio
from traveltimepy import Location, Coordinates, Transportation, TravelTimeSdk


async def main():
    sdk = TravelTimeSdk("8097a90e", "90bf31f1a51cfd508e0d50b0f6ef69a7")

    locations = [
        Location(id="London center", coords=Coordinates(
            lat=51.508930, lng=-0.131387)),
        Location(id="Hyde Park", coords=Coordinates(
            lat=51.508824, lng=-0.167093)),
        Location(id="ZSL London Zoo", coords=Coordinates(
            lat=51.536067, lng=-0.153596))
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
