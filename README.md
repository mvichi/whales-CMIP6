# whales-CMIP6
Scripts to extract sea-ice edge outputs from the Pangeo CMIP6 repository for comparison with historical whaling data.

**Historical catch records of humpback whales and the assessment of early 20th century sea ice edge in climate models**

_Marcello Vichi1,2, Elisa Seyboth3, Thando Mazomba1, Els Vermeulen3, Ken Findlay4, Jan-Olaf Meynecke5,6, Jasper De Bie6, Eduardo Secchi7, Luciano Dalla Rosa7, and Alakendra Roychoudhury8_

1 Department of Oceanography, University of Cape Town, Rondebosch, South Africa; 
2 Marine and Antarctic Research centre for Innovation and Sustainability (MARIS), University of Cape Town, Rondebosch, South Africa; 
3 Mammal Research Institute Whale Unit, Faculty of Natural and Agricultural Sciences, University of Pretoria, South Africa;
4 Centre for Sustainable Oceans, Cape Peninsula University of Technology, Cape Town, South Africa; 
5 Whales and Climate Research Program, Griffith University, Gold Coast, Australia; 
6 Centre for Marine and Coastal Research, Griffith University, Gold Coast, Australia; 
7 Institute of Oceanography, Federal University of Rio Grande, Rio Grande, Brazil; 
8 Department of Earth Sciences, Stellenbosch University, Stellenbosch, South Africa

Submitted for publication in Env. REs. Clim

Note that the historical whaling data must be obtained from the International Whaling Commission (IWC). They cannot be used and distributed without their permission. Version 5.1 was used for this analysis since there is no change in V7.1 for humpback whales
Allison, C. “IWC Individual Large Whale Catch Database.” Available from the International Whaling Commission, 135 Station Road, Impington, Cambridge, CB24 9NP UK. [statistics@iwc.int]. International Whaling Commission., 2013. https://iwc.int.
———. “IWC Individual Large Whale Catch Database.” Available from the International Whaling Commission, 135 Station Road, Impington, Cambridge, CB24 9NP UK. [statistics@iwc.int]. International Whaling Commission., 2020. https://iwc.int.

## Using the scripts
It is recommended to use the pangeo docker image [https://pangeo.io/]
Launch it as follows, where DIR is the location where you have cloned this repository:
`docker run -it --rm --volume DIR:/whales-CMIP6 -p 8888:8888 pangeo/pangeo-notebook:latest jupyter lab --ip 0.0.0.0 /whales-CMIP6`

## Workflow
These scripts download the data from the Pangeo Google repository. They do not need to be called again since the outpur is stored in csv files
* CMIP-SIE-pangeo-google, CMIP-ice-edge: Extracts the model output from the pangeo catalogue and calculate SIE (CMIP6-26_SIE_m_18500115-20141215.csv)
* CMIP-SIE-pangeo-google-piControl, CMIP-ice-edge-piControl: Same for the pi-Control experiment
* OSI-SAF-450-CDR_SIE.ipynb: Calculates sea ice extent from OSI-SAF monthly means and writes OSI-450-CDR_SIE_clim_1979-2014.csv

These scripts do the analyses and generate the figures
* Catches_map_histogram: extract the 1930-39 data and generates figure 1 in the paper
* CMIP-SIE_ts_ranking: rank the climatological SIE and show the timeseries
* Catches-CMIP-ice_edge: generate figure 4 and figure 5
