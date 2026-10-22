# Satellite-Based Assessment of River Water Quality and Human Influence Using Geospatial ML
Satellite Remote Sensing | Google Earth Engine | Geospatial ML | Python | QGIS

## Project Overview

This project focuses on satellite-based geospatial analysis of the Ganga River corridor to study land-use and land-cover (LULC) patterns, surrounding human influence, and their relevance to river water quality assessment.

Developed during a summer internship at the Indian Institute of Technology (IIT) Roorkee, the project integrates multiple satellite datasets and geospatial technologies to support large-scale, automated, and repeatable environmental analysis.

The study covers the Ganga River corridor from Kanpur to Varanasi, with a 150 km buffer zone on either side of the river. Google Earth Engine, Python, and QGIS are used to support satellite imagery processing, spatial analysis, and visualization.

## Project Objectives

Process multi-source satellite imagery using Google Earth Engine.

Analyze Land Use and Land Cover (LULC) patterns across the Ganga River corridor.

Investigate surrounding human influence using satellite-derived observations, including night-time light data.

Explore satellite-based approaches relevant to river water quality assessment.

Integrate Python and QGIS into a unified geospatial analysis workflow.

Support repeatable processing of large-scale satellite datasets for environmental monitoring.

## Study Area

Region: Ganga River corridor, Uttar Pradesh, India

Study stretch: Kanpur to Varanasi

Spatial coverage: 150 km buffer zone on either side of the river

Research domains: Remote sensing, LULC analysis, human influence assessment, and river environmental monitoring

## Satellite Datasets

### 1. Sentinel-2

Used for optical satellite observations and detailed analysis of land-surface and environmental characteristics.

Potential applications within the workflow include:

Multispectral imagery analysis

Vegetation and land-surface characterization

Water-related spectral analysis, where implemented

Image selection and cloud-cover filtering

### 2. Landsat

Used to support satellite-based land-surface analysis and investigation of spatial patterns across the study region.

Potential applications include:

Multispectral image analysis

Land-use and land-cover assessment

Surface change analysis, where implemented

Environmental monitoring across the study area

### 3. VIIRS

Used for satellite-derived night-time light observations to investigate patterns associated with human activity across the Ganga River corridor.

Potential applications include:

Night-time light intensity analysis

Spatial assessment of human activity patterns

Comparison of urbanized and less-developed areas, where implemented

### 4. Land Use and Land Cover (LULC)

LULC analysis is an important component of the project, connecting satellite observations with the spatial distribution of land-cover types and surrounding human activity.

Depending on the implemented workflow, this may include:

Identification or classification of land-use categories

Spatial distribution of land-cover patterns

Mapping of built-up areas, vegetation, agricultural land, and water bodies

Geospatial visualization of classified results


## Technology Stack

## Technology Stack

| Technology / Tool | Purpose |
|---|---|
| **Google Earth Engine (GEE)** | Cloud-based satellite imagery processing and geospatial analysis |
| **Sentinel-2** | Multispectral satellite imagery for land-surface and water-related analysis |
| **Landsat** | Satellite imagery for land-use analysis and environmental monitoring |
| **VIIRS** | Night-time light analysis to assess spatial patterns of human activity |
| **Python** | Data processing, automation, and geospatial workflow development |
| **QGIS** | Geospatial visualization, spatial analysis, and map generation |
| **Google Colab / Jupyter Notebook** | Interactive coding, experimentation, and analysis |
| **Google Earth Engine Python API (`ee`)** | Programmatic access to Google Earth Engine datasets and processing capabilities |
| **Pandas** | Tabular data manipulation and analysis |
| **NumPy** | Numerical computation and array operations |
| **Matplotlib** | Data visualization and analytical plotting, where applicable |

## Methodology

### The project follows a multi-source geospatial workflow.

Study area definition: Define the Ganga River corridor and the corresponding buffer zone from Kanpur to Varanasi.

Satellite data acquisition: Access relevant Sentinel-2, Landsat, and VIIRS datasets through suitable data collections and platforms.

Data filtering and preprocessing: Apply appropriate spatial, temporal, and data-quality filters.

Optical imagery analysis: Process Sentinel-2 and Landsat imagery for relevant land-surface and environmental analysis.

Human influence assessment: Analyze VIIRS night-time light observations to investigate spatial patterns associated with human activity.

LULC analysis: Examine land-use and land-cover patterns using the implemented classification or mapping workflow.

Python and QGIS integration: Combine programmatic processing with spatial visualization and analysis.

Result generation: Prepare maps, tables, and analytical outputs to support interpretation of the study area.


## Expected Applications

Multi-source satellite image processing

Land-use and land-cover mapping

Spatial assessment of human activity patterns

River corridor environmental monitoring

Satellite-based investigation of water-related characteristics

Geospatial analysis to support river basin management and environmental research

## Limitations

Optical satellite observations can be affected by cloud cover, atmospheric conditions, and spatial resolution.

Night-time light intensity is an indirect indicator of human activity and does not independently establish environmental impact.

LULC classification accuracy depends on the classification method, input data, and validation process.

Reliable quantitative water quality assessment requires suitable spectral indicators or models and, where possible, independent field measurements.

Findings should be interpreted in the context of the implemented methods and available data.

## Internship

Indian Institute of Technology Roorkee (IIT Roorkee)
Summer Internship | June 2026 – August 2026

The internship work involved automated satellite imagery processing, large-scale geospatial analysis, and integration of Python and QGIS to support repeatable environmental and land-use assessment workflows.

## Acknowledgements

I acknowledge the Indian Institute of Technology Roorkee and Water Resources & Development Management Department for the internship opportunity and the providers of the satellite datasets and open-source geospatial tools used in this project.

License

A suitable license may be added after confirming permission to publish the code, data products, and associated research materials.

Author: Yuvraj Makani, Aanya Aggarwal

Focus Areas: Remote Sensing · Geospatial Machine Learning · Satellite Image Processing · LULC Analysis · Environmental Monitoring
