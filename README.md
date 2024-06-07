# whales-CMIP6
Scripts to extract sea-ice variables from CMIP6 repository for comparison with historical whaling data
It uses the pangeo docker image [https://pangeo.io/]

Launch it as follows, where DIR is the location where you have cloned this repository:
docker run -it --rm --volume DIR:/whales-CMIP6 -p 8888:8888 pangeo/pangeo-notebook:latest jupyter lab --ip 0.0.0.0 /whales-CMIP6

