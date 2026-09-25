from pathlib import Path

# Project root
ROOT = Path(__file__).resolve().parents[1]

# Directories
DATA_DIR = ROOT / "data"
FIGURES_DIR = ROOT / "figures"
NOTEBOOKS_DIR = ROOT / "notebooks"
DOCS_DIR = ROOT / "docs"

# Study area: Bhote Koshi corridor (approximate bounding box)
# You can refine this later after visual inspection in GEE.
AOI_BBOX = {
    "min_lon": 85.80,
    "min_lat": 27.60,
    "max_lon": 86.20,
    "max_lat": 28.20,
}

# As a GeoJSON-like dict (useful for geemap / GEE)
AOI_GEOJSON = {
    "type": "Feature",
    "properties": {"name": "Bhote Koshi corridor"},
    "geometry": {
        "type": "Polygon",
        "coordinates": [[
            [AOI_BBOX["min_lon"], AOI_BBOX["min_lat"]],
            [AOI_BBOX["max_lon"], AOI_BBOX["min_lat"]],
            [AOI_BBOX["max_lon"], AOI_BBOX["max_lat"]],
            [AOI_BBOX["min_lon"], AOI_BBOX["max_lat"]],
            [AOI_BBOX["min_lon"], AOI_BBOX["min_lat"]],
        ]],
    },
}

# Provisional study area: Bhote Koshi / Sindhupalchok investigation area.
# These coordinates are an initial discovery AOI and will be refined after
# satellite-scene availability and event-location verification.
AOI_BBOX = {
    "min_lon": 85.80,
    "min_lat": 27.60,
    "max_lon": 86.20,
    "max_lat": 28.20,
}

# Provisional investigation dates.
# Final dates will be selected after checking the documented event timeline
# and available Sentinel-1 / Sentinel-2 scenes.
EVENT_NAME = "Nepal flood event — date under verification"

FLOOD_START = "2026-08-24"
FLOOD_END = "2026-09-10"

BASELINE_START = "2026-06-01"
BASELINE_END = "2026-07-31"

# Event windows


# Optional: second event (Oct 2025 monsoon floods)
EVENT_2025_START = "2025-10-03"
EVENT_2025_END = "2025-10-06"
BASELINE_2025_START = "2025-07-01"
BASELINE_2025_END = "2025-09-01"

# Sentinel-1 / Sentinel-2 / VIIRS settings (defaults; can be overridden in notebooks)
S1_POLARIZATIONS = ["VV", "VH"]
S1_ORBIT_PASS = "DESCENDING"  # prefer, but we'll accept both if needed
S2_CLOUD_COVER_MAX = 20  # percent

# CRS and resolution (for exported rasters)
TARGET_CRS = "EPSG:4326"
TARGET_RESOLUTION = 20  # meters (good compromise for S1/S2)

EXPORT_SCALE_S1 = 10
EXPORT_SCALE_S2 = 10
EXPORT_SCALE_VIIRS = 500
EXPORT_SCALE_DEM = 30

MAX_PIXELS = 1_000_000_000_000