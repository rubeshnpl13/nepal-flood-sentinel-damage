import ee

ee.Initialize()

print(
    ee.Image("USGS/SRTMGL1_003")
    .select("elevation")
    .reduceRegion(
        reducer=ee.Reducer.mean(),
        geometry=ee.Geometry.Point([85.9, 27.9]),
        scale=30,
    )
    .getInfo()
)