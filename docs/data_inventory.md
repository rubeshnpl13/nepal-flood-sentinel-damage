# Data Inventory

## Study area

- Initial AOI: Bhote Koshi / Sindhupalchok investigation area, Nepal
- AOI bounding box: longitude 85.80 to 86.20; latitude 27.60 to 28.20
- Event: Nepal flood event — date under verification
- Status: AOI and event dates are provisional discovery settings

## Satellite and contextual datasets

| Dataset | Earth Engine ID / source | Intended use | Selected date(s) | Notes |
|---|---|---|---|---|
| Sentinel-1 GRD | `COPERNICUS/S1_GRD` | Primary SAR flood mapping | Candidate dates pending final event verification | Use matched direction and relative orbit where possible |
| Sentinel-2 SR Harmonized | `COPERNICUS/S2_SR_HARMONIZED` | Optical validation | Pending | Post-event low-cloud coverage unavailable in provisional window |
| VIIRS Monthly | `NOAA/VIIRS/DNB/MONTHLY_V1/VCMSLCFG` | Coarse nighttime-lights disruption/damage proxy | Pending | Approximately 500 m; not building-level damage |
| SRTM DEM | `USGS/SRTMGL1_003` | Elevation and slope masking | Static | Approximately 30 m |

## Phase 1 availability check

### Sentinel-1

- Baseline window: `2026-06-01` to `2026-07-31`
- Provisional post-event window: `2026-08-24` to `2026-09-10`
- Baseline availability: 27 scenes across all orbits; 11 descending scenes
- Post-event availability: 8 scenes across all orbits; 3 descending scenes

Promising same-track descending candidates:

| Relative orbit | Baseline acquisitions | Post-event acquisitions | Status |
|---|---|---|---|
| 19 | 2026-06-06, 2026-06-18, 2026-06-25, 2026-07-07, 2026-07-19 | 2026-08-24, 2026-09-05 | Initial candidate |
| 121 | 2026-06-01, 2026-06-13, 2026-06-25, 2026-07-02, 2026-07-14, 2026-07-26 | 2026-08-31 | Secondary candidate |

Initial Sentinel-1 analysis candidate: descending pass, relative orbit 19. This is provisional pending authoritative event-date verification and visual inspection of imagery.

### Sentinel-2

- Baseline scenes satisfying the configured cloud threshold: 5
- Post-event scenes satisfying the configured cloud threshold: 0
- Post-event scenes with no cloud filter: 28

Interpretation: optical imagery is available but cloud contamination is substantial during the provisional post-event monsoon window. Sentinel-2 will not be used as primary post-event validation unless a suitable nearby clear acquisition is found.

### VIIRS and terrain

- VIIRS Monthly images available over AOI: 152
- SRTM DEM loaded successfully.
- Terrain slope was derived successfully using `ee.Terrain.slope()`.

## Data management

- Imagery is currently queried and processed remotely in Google Earth Engine.
- No Sentinel-1, Sentinel-2, VIIRS, or SRTM rasters have been downloaded locally during Phase 1.
- `data/raw/` is intentionally empty except for `.gitkeep`.
- Later exports will be limited to selected analysis products, not the entire source image collections.

## Decisions log

- Event date and final AOI will be chosen only after reviewing authoritative event documentation and satellite-scene availability.
- Sentinel-1 is the primary flood-mapping input because SAR can observe through monsoon cloud cover.
- Prefer matched orbit direction and relative orbit number for pre/post Sentinel-1 comparison.
- A slope mask will be considered later to reduce terrain-related flood false positives.
- VIIRS will be used only as a coarse-scale disruption/damage proxy and never as building-level damage evidence.