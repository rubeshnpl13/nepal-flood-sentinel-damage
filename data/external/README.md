# External Reference Data

## `impact_locations.csv`

This file contains approximate point locations for settlements and corridors reported as affected by the 26 August 2026 Rasuwa–Bhote Koshi flood.

These points are used for exploratory spatial validation only. They are not a pixel-level flood reference dataset and must not be used to calculate conventional classification accuracy metrics such as IoU, precision, recall, or F1 score.

Location coordinates are approximate and should be refined when authoritative geospatial event products become available.

### Current fields

- `location_name`: settlement/corridor name
- `latitude`, `longitude`: approximate WGS84 coordinates
- `impact_type`: reported impact category
- `source`: broad evidence/source category
- `confidence`: confidence in the coordinate as a spatial reference
- `notes`: limitations or interpretation notes

### Important interpretation rule

A candidate SAR pixel near one of these points is not automatically confirmed flooding, and a candidate pixel far from these points is not automatically false. The point dataset is intentionally incomplete and is used only for exploratory spatial-reference validation.
