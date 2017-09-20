#!/usr/bin/python

import sys
import argparse
from controller import salamiclass
from datetime import datetime, timedelta


def main(argv):

    salami = salamiclass()
        
    parser = argparse.ArgumentParser()
    parser.add_argument("--verbose"   , help = "Verbose mode on")
    parser.add_argument("--starttime" , help = "Start time in ISO format (default: 6 hours from now).")
    parser.add_argument("--endtime"   , help = "End time in ISO format (default: now).")
    parser.add_argument("--timestep"  , help = "Timestep in minutes (default: 5 minutes).")
    parser.add_argument("--format"    , help = "Starttime in ISO format (default: now).")
    parser.add_argument("--bbox"      , help = "bbox: lon,lat,lon,lat (default: 19.2,58.7,31.7,70.6).")
    parser.add_argument("--crs"       , help = "Projection (default: EPSG::3067).")
    parser.add_argument("--lines"     , help = "Set a maximum number of lightning observations to be returned.") 
    args = parser.parse_args()

    endtime    = datetime.now()
    starttime  = datetime.now() - timedelta(hours=6)

    # set default vakues
    # timestaps and timestep
    endtime    = endtime.strftime('%Y-%m-%dT%H:%M:%S')
    starttime  = starttime.strftime('%Y-%m-%dT%H:%M:%S')
    timestep   = 60
    # return format
    format     = "ascii"
    # bbox and projection
    bbox       = "19.2,58.7,31.7,70.6"
    projection = "EPSG::3067"
    # verbose mode
    verbose    = "off"
    # number of observations
    lines      = -1
    
    if(args.verbose):
        verbose = "on"
    if(args.starttime):
        starttime = args.starttime
    if(args.endtime):
        endtime = args.endtime
    if(args.timestep):
        timestep = args.timestep
    if(args.format):
        format = args.format
    if(args.bbox):
        bbox = args.bbox
    if(args.crs):
        projection = args.crs
    if(args.verbose):
        verbose = "on"
    if(args.lines):
        lines   = args.lines

    response = salami.dateinterval_check(starttime, endtime)
    if(response == False):
        print("Invalid time parameters")
        print("Use default values instead")
        endtime    = datetime.now()
        starttime  = datetime.now() - timedelta(hours=6)
    
    # initialize parameters
    parameters = salami.get_parameters(verbose, starttime, endtime, timestep, bbox, projection, format, lines)
    data = salami.parse_data(parameters)

    #print(data)
    for i in range(0,len(data)):
        print(data[i])


if __name__ == "__main__":
    main(sys.argv[1:])
