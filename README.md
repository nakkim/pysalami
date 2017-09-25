# pysalami
Pysalami lightning observation tool

´´´
Info:
$ python pysalami.py -h</b>
usage: pysalami.py [-h] [--verbose VERBOSE] [--starttime STARTTIME]
                   [--endtime ENDTIME] [--timestep TIMESTEP] [--format FORMAT]
                   [--bbox BBOX] [--crs CRS] [--lines LINES]

optional arguments:
  -h, --help            show this help message and exit
  --verbose VERBOSE     Verbose mode on
  --starttime STARTTIME
                        Start time in ISO format (default: 6 hours from now).
  --endtime ENDTIME     End time in ISO format (default: now).
  --timestep TIMESTEP   Timestep in minutes (default: 5 minutes).
  --format FORMAT       Starttime in ISO format (default: now).
  --bbox BBOX           bbox: lon,lat,lon,lat (default: 19.2,58.7,31.7,70.6).
  --crs CRS             Projection (default: EPSG::3067).
  --lines LINES         Set a maximum number of lightning observations to be
                        returned.

Example:
$ python pysalami.py --starttime 2017-08-12T23:00:00 --endtime 2017-08-13T00:00:00 --lines 3 --format ascii
2017-08-12T23:50:37Z,60.59950,31.26990,16.0,1.0,1.0,13.2
2017-08-12T23:50:37Z,60.46640,31.69870,15.0,1.0,1.0,1.2
2017-08-12T23:50:37Z,60.47060,31.68640,12.0,1.0,1.0,0.7
´´´