#!/usr/bin/python

import sys
import argparse
from controller import salamaclass
from datetime import datetime, timedelta
import numpy as np


def main(argv):

        
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--verbose", action="store_true", help = "Verbose mode")
    parser.add_argument("--starttime" , help = "Starttime in ISO format, default: 6 hours from now.")
    parser.add_argument("--endtime"   , help = "Endtime in ISO format, default: now.")
    parser.add_argument("--format"    , help = "Supported return formats: ascii, csv, json, array")
    parser.add_argument("--bbox"      , help = "lon,lat,lon,lat. default: 19.2,58.7,31.7,70.6.")
    parser.add_argument("--crs"       , help = "Projection, default: EPSG::3067.")
    parser.add_argument("--lines"     , help = "Set a maximum number of lightning observations to be returned.")
    parser.add_argument("--outputfile", help = "Set output file i.e. outputdata.csv")
    parser.add_argument("--database"  , help = "Write data to database: on")
    
    args = parser.parse_args()

    endtime    = datetime.now()
    starttime  = datetime.now() - timedelta(hours=6)

    # set default vakues
    # timestaps and timestep
    endtime    = endtime.strftime('%Y-%m-%dT%H:%M:%S')
    starttime  = starttime.strftime('%Y-%m-%dT%H:%M:%S')
    # return format
    format     = "ascii"
    # bbox and projection
    bbox       = "19.2,58.7,31.7,70.6"
    projection = "EPSG::3067"
    # verbose mode
    verbose    = False
    # number of observations
    lines      = -1
    outputfile = "-1"
    database = "off"
    
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
        verbose = True
    if(args.lines):
        lines   = args.lines
    if(args.outputfile):
        outputfile  = args.outputfile
    if(args.database):
        database = args.database


    # create salama class    
    salama = salamaclass(verbose)
        
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
            return(data)
        if(format == "array"):
            print(data)
            return data
        else:
            for i in range(0,len(data)):
                print(data[i])
        
    # print data to a file if needed    
    if(outputfile != "-1"):
        header = "time,lat,lon,peakcurrent,multiplicity,cloudindicator,ellipsemajor"
        np.savetxt(str(outputfile), data, delimiter=",", fmt='%s', header=header)

    # write data to database if needed
    if(database == "on"):
        salama.insert_db(data)
        
    

if __name__ == "__main__":
    main(sys.argv[1:])
