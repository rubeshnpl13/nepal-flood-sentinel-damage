# Data Inventory and Scene Selection

## Event

- **Event:** Rasuwa–Bhote Koshi flash flood
- **Date:** 26 August 2026
- **Primary area affected:** Upper Lhende Khola, Bhote Koshi, and downstream Trishuli corridor in central Nepal
- **Cause:** An ice–rock avalanche in the upper Lhende Khola watershed near the Nepal–China border triggered a debris-laden flood.
- **Primary event-source types:** Government of Nepal situation updates, NDRRMA situation reporting, hydrology assessments, and ICIMOD reporting.

## Initial study area

- **Initial AOI bounding box:** 85.80–86.20° E, 27.60–28.20° N
- **Purpose:** Exploratory coverage for inspecting the Bhote Koshi / Trishuli corridor.
- **Status:** Provisional; it will be refined into a smaller analysis corridor after visual scene inspection.

## Dataset inventory

| Dataset | Earth Engine ID / source | Spatial resolution | Intended use | Selected data |
|---|---|---:|---|---|
| Sentinel-1 GRD | `COPERNICUS/S1_GRD` | 10 m | Primary flood/debris-change mapping | Descending, relative orbit 19 |
| Sentinel-2 SR Harmonized | `COPERNICUS/S2_SR_HARMONIZED` | 10–20 m | Optical validation where cloud-free | Baseline scenes available; no post-event scenes below 20% scene-level cloud cover |
| VIIRS DNB Monthly | `NOAA/VIIRS/DNB/MONTHLY_V1/VCMSLCFG` | Approximately 500 m | Coarse nighttime-light disruption proxy | Date pair to be selected later |
| SRTM DEM | `USGS/SRTMGL1_003` | Approximately 30 m | Elevation, slope, terrain masking | Static terrain layer |

## Sentinel-1 scene availability

The initial availability query returned:

- **Baseline period:** 1 June–31 July 2026
  - 27 scenes across all orbit directions
  - 11 descending scenes
- **Post-event search period:** 26 August–10 September 2026
  - 8 scenes across all orbit directions
  - 3 descending scenes

## Selected Sentinel-1 geometry

To reduce differences caused by acquisition geometry, analysis uses the same Sentinel-1 orbit configuration:

- **Orbit pass:** Descending
- **Relative orbit:** 19
- **Baseline acquisition dates:** 6 June, 18 June, 7 July, and 19 July 2026
- **Baseline method:** Median composite of the four selected scenes
- **Post-event acquisition date:** 5 September 2026

## Selection rationale

The 5 September 2026 scene is the first available post-event acquisition with the selected descending relative-orbit-19 geometry after the 26 August flood. The 24 August scene was excluded because it predates the documented event.

This scene is approximately 10 days after the flood. Therefore, it may underrepresent temporary open-water inundation that receded before acquisition, while still capturing potentially persistent debris, channel, and land-surface changes. The project will state this limitation clearly and test complementary imagery where appropriate.

## Sentinel-2 availability limitation

Five baseline Sentinel-2 scenes met the project’s 20% scene-level cloud filter. No post-event Sentinel-2 scenes met that criterion, although 28 post-event scenes exist without the cloud filter. This supports the decision to use Sentinel-1 SAR as the primary flood-mapping input.

## Current limitations

- The AOI is a broad exploratory bounding box and may include terrain not directly affected by flooding.
- Himalayan terrain creates radar shadow and layover, which can resemble flood-related backscatter change.
- The selected same-geometry post-event Sentinel-1 scene is 10 days after the event.
- VIIRS monthly data is a coarse area-level proxy and must not be interpreted as building-level damage.