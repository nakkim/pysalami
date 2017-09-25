### pysalami ###
Pysalami lightning observation tool

Usage and examples:
```
$ ./salama.py -h
usage: salama.py [-h] [--verbose VERBOSE] [--starttime STARTTIME]
                 [--endtime ENDTIME] [--format FORMAT] [--bbox BBOX]
                 [--crs CRS] [--lines LINES] [--outputfile OUTPUTFILE]

optional arguments:
  -h, --help            show this help message and exit
  --verbose VERBOSE     Verbose mode on
  --starttime STARTTIME
                        Starttime in ISO format, default: 6 hours from now.
  --endtime ENDTIME     Endtime in ISO format, default: now.
  --format FORMAT       Supported return formats: ascii, csv
  --bbox BBOX           lon,lat,lon,lat. default: 19.2,58.7,31.7,70.6.
  --crs CRS             Projection, default: EPSG::3067.
  --lines LINES         Set a maximum number of lightning observations to be
                        returned.
  --outputfile OUTPUTFILE
                        Set output file i.e. outputdata.csv

Example:
$ ./salama.py --starttime 2017-08-12T22:00:00 --endtime 2017-08-13T00:00:00 --format ascii --lines 10
2017-08-12T23:50:37Z 60.59950 31.26990 16.0 1.0 1.0 13.2
2017-08-12T23:50:37Z 60.46640 31.69870 15.0 1.0 1.0 1.2
2017-08-12T23:50:37Z 60.47060 31.68640 12.0 1.0 1.0 0.7
2017-08-12T23:37:27Z 60.95650 31.19530 16.0 1.0 0.0 0.6
2017-08-12T23:33:41Z 63.85020 25.57600 47.0 1.0 0.0 0.1
2017-08-12T23:33:41Z 62.82350 27.25980 8.0 1.0 0.0 6.7
2017-08-12T23:33:41Z 63.85210 25.59430 24.0 1.0 1.0 0.2
2017-08-12T23:33:21Z 60.89610 31.24260 11.0 1.0 1.0 0.4
2017-08-12T23:31:51Z 60.88530 31.22060 10.0 1.0 1.0 0.6
2017-08-12T23:31:48Z 64.85560 30.46130 -7.0 1.0 1.0 9.0
```
