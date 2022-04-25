# Geoparsing: Solved or Biased? An Evaluation of Geographic Biases in Geoparsing
In this repository, we provide descriptions about how to reproduce our evaluation study. More information can found in our paper "Geoparsing: Solved or Biased? An Evaluation of Geographic Biases in Geoparsing" accepted by [AGILE 2022](https://agile-online.org/index.php/conference-2022). 

## Downloading Datasets
To reproduce our data preprocessing steps, you need to download several datasets first and put them in corresponding directories. Alternatively, you can also directly use our shared preprocessed datasets and jump to the **Running Geoparsers** section.

The country/region shapefile can be accessed as [Admin-0 Countries](https://www.naturalearthdata.com/http//www.naturalearthdata.com/download/10m/cultural/ne_10m_admin_0_countries.zip) from [Natural Earth](https://www.naturalearthdata.com), and should be put in [`data/admin0-natural-earth/`](data/admin0-natural-earth/). LGL, GeoVirus, and WikToR can be accessed [here](https://github.com/milangritta/Geocoding-with-Map-Vector/tree/master/data), and should be put in [`data/evaluation-corpora/original-datasets/`](data/evaluation-corpora/original-datasets/). Their data patches can be accessed [here](https://github.com/google-research-datasets/mlg_evaldata), and should be put in [`data/evaluation-corpora/data-patches/`](data/evaluation-corpora/data-patches/). GeoCorpora can be accessed [here](https://github.com/geovista/GeoCorpora), and should be put in [`data/evaluation-corpora/original-datasets/`](data/evaluation-corpora/original-datasets/). GeoWiki can be accessed [here](https://www.repository.cam.ac.uk/bitstream/handle/1810/277772/geowiki.txt.zip?sequence=5&isAllowed=y), and should be put in
[`data/training-corpora/`](data/training-corpora/). The [GeoNames](http://www.geonames.org/) gazetteer used by [CamCoder](https://github.com/milangritta/Geocoding-with-Map-Vector) can be accessed [here](https://www.repository.cam.ac.uk/bitstream/handle/1810/277772/allCountries.txt.zip?sequence=4&isAllowed=y), and should be put in [`data/gazetteers/`](data/gazetteers/).

## Data Preprocessing
### Annotated Location Extraction
To achieve both our spatially-explicit geoparsing performance evaluation and geographic bias evaluation, we extracted all annotated locations from training and evaluation corpora as well as the GeoNames gazetteer. The script used is [`scripts/annotated-poi-extraction.ipynb`](scripts/annotated-poi-extraction.ipynb). These extracted locations are stored in [`data/extracted-annotated-locations/`](data/extracted-annotated-locations/). 

### Splitting Articles in LGL, GeoVirus, and WikToR
To more easily run [Edinburgh Geoparser](https://www.inf.ed.ac.uk/research/isdd/admin/package?view=1&id=199), we split articles in LGL, GeoVirus, and WikToR into separate datasets, which can be found at [`data/evaluation-corpora/split-datasets/`](data/evaluation-corpora/split-datasets/).

### Grid Summary Generation
For the representation bias analysis, we generated grids containing a summary about the number of annotated locations located within for different datasets, respectively. This grid summary generation process was done in ArcGIS Pro 2.9.0. An example of using extracted annotated locations from WikToR is attached below.

First, use [XY Table To Point](https://pro.arcgis.com/en/pro-app/latest/tool-reference/data-management/xy-table-to-point.htm) to convert WikToR's annotated locations into point features.

<div align=center>
<img src="screenshots/grid-summary-generation-1.PNG" width='20%' height = '20%'>
</div>


## Running Geoparsers

## Spatially-Explicit Geoparsing Performance Evaluation

## Geographic Bias Evaluation