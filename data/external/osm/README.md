# OpenStreetMap Data

## Source

Vector data were retrieved from Overpass Turbo using OpenStreetMap tags within the project analysis bounding box:

- South: 28.00° N
- West: 85.05° E
- North: 28.45° N
- East: 85.45° E

## Overpass queries

### Major rivers

```overpass
[out:json];

way["waterway"="river"](28.00,85.05,28.45,85.45);

out geom;
```

### Roads

```overpass
[out:json];

way
  ["highway"~"^(motorway|trunk|primary|secondary|tertiary|unclassified|residential)$"]
  (28.00,85.05,28.45,85.45);

out geom;
```

### Buildings

```overpass
[out:json];

way["building"](28.00,85.05,28.45,85.45);

out geom;
```

## Files

- `rivers.geojson`: Features tagged `waterway=river`; 37 features returned in the initial query.
- `roads.geojson`: Mapped vehicular road features.
- `buildings.geojson`: Mapped building-footprint ways.

## Purpose

- Major rivers provide a river-corridor reference geometry for evaluating spatial concentration of the Sentinel-1 flood-like candidate layer.
- Roads and buildings support mapped infrastructure-exposure analysis.

## Limitations

OpenStreetMap is volunteer-maintained. Completeness varies by area and feature type. The presence of a mapped feature does not verify flood damage, and an absent mapped feature does not prove that an asset does not exist.

All later metrics are reported as mapped exposure, not confirmed destruction, complete asset inventory, or total real-world damage.

- `relevant_rivers.geojson`: Major-river features selected because they intersect a 5 km buffer around approximate reported-impact reference points.