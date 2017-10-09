#!/usr/bin/python

import sys
import argparse
from controller import salamaclass
from datetime import datetime, timedelta


def main(argv):

    #print(argv)
    salama = salamaclass()
        
    parser = argparse.ArgumentParser()
    parser.add_argument("--verbose"   , help = "Verbose mode on")
    parser.add_argument("--starttime" , help = "Starttime in ISO format, default: 6 hours from now.")
    parser.add_argument("--endtime"   , help = "Endtime in ISO format, default: now.")
    parser.add_argument("--format"    , help = "Supported return formats: ascii, csv")
    parser.add_argument("--bbox"      , help = "lon,lat,lon,lat. default: 19.2,58.7,31.7,70.6.")
    parser.add_argument("--crs"       , help = "Projection, default: EPSG::3067.")
    parser.add_argument("--lines"     , help = "Set a maximum number of lightning observations to be returned.")
    parser.add_argument("--outputfile", help = "Set output file i.e. outputdata.csv")

    args = parser.parse_args()

    endtime    = datetime.now()
    starttime  = datetime.now() - timedelta(hours=6)

    # set default vakues
    # timestaps and timestep
    #endtime    = endtime.strftime('%Y-%m-%dT%H:%M:%S')
    #starttime  = starttime.strftime('%Y-%m-%dT%H:%M:%S')
    starttime   = '2017-08-12T19:00:00'
    endtime     = '2017-08-12T20:00:23'
    # return format
    #format     = "ascii"
    format     = "array"
    # bbox and projection
    bbox       = "19.2,58.7,31.7,70.6"
    projection = "EPSG::3067"
    # verbose mode
    verbose    = "off"
    # number of observations
    lines      = -1
    outputfile = "-1"
    
    if(args.verbose):
        verbose = "on"
    if(args.starttime):
        starttime = args.starttime
    if(args.endtime):
        endtime = args.endtime
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
    if(args.outputfile):
        outputfile   = args.outputfile
    
    # initialize parameters
    parameters = salama.get_parameters(verbose, starttime, endtime,
                                       bbox, projection, format, lines, outputfile)
    data = salama.parse_data(parameters)
    
    if not data:
        print("No observations")
    else:
        # print data
        if(format == "json"):
            print(data)
        if(format == "array"):
            print(data);
            return data
        else:
            for i in range(0,len(data)):
                print(data[i])
        
    # print data to a file is needed    
    if(outputfile != "-1"):
        f = open(str(outputfile), "w")
        f.write(data)
        f.close()


if __name__ == "__main__":
    main(sys.argv[1:])
