# Phase 2 — Baseline Sentinel-1 Candidate Change Mapping

## Purpose

Produce an initial candidate mask of flood/debris-related surface change associated with the 26 August 2026 Rasuwa–Bhote Koshi flash flood.

## Input imagery

- **Sensor:** Sentinel-1 GRD SAR
- **Collection:** `COPERNICUS/S1_GRD`
- **Acquisition geometry:** Descending, relative orbit 19
- **Baseline:** Median composite of all matched scenes from 1 June–31 July 2026
- **Post-event image:** 5 September 2026

## Method

1. Select same-orbit Sentinel-1 VV/VH imagery.
2. Build a pre-event median composite.
3. Apply a 30 m focal-median filter to VV backscatter.
4. Calculate post-event minus pre-event VV backscatter change.
5. Flag negative change below an initial threshold of −2.0 dB.
6. Exclude terrain with slope greater than 15°.
7. Exclude persistent water identified by JRC Global Surface Water occurrence of at least 90%.
8. Remove components with fewer than 8 connected 10 m pixels.

## Interpretation

The output is a candidate flood/debris-related change mask, not validated flood extent. False positives can arise from SAR terrain effects, radar shadow, channel morphology changes, land-surface moisture, and acquisition timing. The post-event scene was acquired 10 days after the event and may not capture maximum temporary inundation.

## Planned evaluation

- Visually inspect the mask against terrain and available cloud-permitting Sentinel-2 imagery.
- Perform sensitivity analysis across VV thresholds and slope limits.
- Compare candidate-change zones with reported impact locations and available satellite-derived event products.

## Threshold sensitivity and interpretation

The mapped candidate area is sensitive to the selected VV-change threshold. Under the same slope, historical-water, smoothing, and connected-component filters, candidate area decreases as the VV-change threshold becomes more negative.

The selected post-event Sentinel-1D acquisition was obtained on 28 August 2026, approximately two days after the 26 August event. The baseline consists of five geometrically matched Sentinel-1D acquisitions acquired between 29 June and 16 August 2026.

Using a −3 dB VV-change threshold, the flood-like candidate mask covers approximately 1.38 km² within the analysis AOI. This is an exploratory SAR-derived flood-like surface-change estimate, not verified inundation extent.

The broader SAR surface-change layer is analytically separate from the flood-like candidate layer. It identifies substantial positive or negative backscatter changes and must not be interpreted as a direct debris-area estimate.

Validation against independent optical imagery, river/channel information, reported impact locations, or authoritative event mapping is required before making stronger impact claims.