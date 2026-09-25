# Study area: provisional investigation AOI covering the Bhote Koshi /
# Trishuli corridor. It will be refined after visual scene inspection.
AOI_BBOX = {
    "min_lon": 85.80,
    "min_lat": 27.60,
    "max_lon": 86.20,
    "max_lat": 28.20,
}

# Verified event information
EVENT_NAME = "Rasuwa–Bhote Koshi flash flood"
EVENT_DATE = "2026-08-26"
EVENT_CAUSE = (
    "Ice–rock avalanche in the upper Lhende Khola watershed near "
    "the Nepal–China border, producing a debris-laden flood."
)

# Analysis windows
BASELINE_START = "2026-06-01"
BASELINE_END = "2026-07-31"

POST_EVENT_START = "2026-08-26"
POST_EVENT_END = "2026-09-10"

# Selected primary Sentinel-1 acquisition geometry
S1_ORBIT_PASS = "DESCENDING"
S1_RELATIVE_ORBIT = 19

S1_POLARIZATIONS = ["VV", "VH"]
# Baseline dates used to make the same-orbit composite
S1_BASELINE_DATES = [
    "2026-06-06",
    "2026-06-18",
    "2026-07-07",
    "2026-07-19",
]

# Selected post-event scene: first same-orbit descending acquisition after flood
S1_POST_EVENT_DATE = "2026-09-05"

# Sentinel-2 is only used for optical validation where usable.
S2_CLOUD_COVER_MAX = 20

# Data export settings
EXPORT_SCALE_S1 = 10
EXPORT_SCALE_S2 = 10
EXPORT_SCALE_VIIRS = 500
EXPORT_SCALE_DEM = 30
MAX_PIXELS = 1_000_000_000_000