



# Use use the C implementation if possible, since it is
# much faster and consumes significantly less memory
try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET

from datetime import datetime, time
import time
import urllib2
import sys

class salamiclass:

    def dateinterval_check(self, starttime, endtime):
    #    try:
    #        int(datetime.datetime.strptime(starttime, "%Y-%m-%dT%H:%M:%S").strftime("%s"))
    #    except ValueError:
    #        print('starttime not a valid timestamp')
    #    try:
    #        int(datetime.datetime.strptime(endtime, "%Y-%m-%dT%H:%M:%S").strftime("%s"))            
    #    except: ValueError:
    #        print("endtime not a valid timestamp")
        start = datetime.strptime(starttime, "%Y-%m-%dT%H:%M:%S")
        end   = datetime.strptime(endtime, "%Y-%m-%dT%H:%M:%S")
        start = time.mktime(start.timetuple())
        end   = time.mktime(end.timetuple())
        if(end - start > 168*60*60 or end - start < 0):
            return False
        else:
            return True
        
            
    def debug(self, text):
        print("TODO")
    
    def formatter(self, data, format, lines):
        # format data
        # default: ascii

        # if lines != -1, remove excess data
        output = []
        if(lines > 0):
            # output only the number of lines amount of data
            output = data[::-1]
            data = output[0:int(lines)]

        output = []
        if(format == "csv"):
            for row in data:
                row = row.replace(" ", ",")
                output.append(row)
            return output
        
    
    def test_connection():
        print("TODO")
            
    def get_parameters(self, verbose, starttime, endtime, timestep,
                       bbox, crs, format, lines):

        parameters = {}        
        # Configuration directory
        # default: settings/
        CNFDIR       = "settings/"
        # verbose mode on/off
        #verbose      = verbose
        # timesettings and time step
        #starttime    = starttime
        #endtime      = endtime
        #timestep     = timestep
        # bbox and projection
        #bbox         = bbox
        projection   = crs
        # format and number of lines to be returned
        returnformat = format
        lines        = lines
        # get apikey from cnf-file 
        try:
            with open(CNFDIR + 'controller.cnf') as f:
                content = f.readlines()
                # remove white spaces and \n
                content = [x.strip() for x in content]
                # if first character is #, remove the line as a comment
                # save parameters as an array
                for x in content:
                    if(x[0] != '#'):
                        apikey = x.split('=', 1 )
        except Exception as error:
            print(error)
    
        parameters.update({"verbose"    : verbose})
        parameters.update({"starttime"  : starttime})
        parameters.update({"endtime"    : endtime})
        parameters.update({"timestep"   : timestep})
        parameters.update({"bbox"       : bbox})
        parameters.update({"projection" : projection})
        parameters.update({"format"     : returnformat})
        parameters.update({"apikey"     : apikey})
        parameters.update({"lines"      : lines})

        return parameters

    
    # parse data from url
    def parse_data(self, parameters):
        
        starttime  = parameters['starttime']
        endtime    = parameters['endtime']
        timestep   = str(parameters['timestep'])
        bbox       = parameters['bbox']
        projection = parameters['projection']
        format     = parameters['format']
        apikey     = parameters['apikey'][1]
        lines      = parameters['lines']
        params     = "peak_current,multiplicity,cloud_indicator,ellipse_major"
        
        url = ("http://data.fmi.fi/fmi-apikey/"+apikey+
               "/wfs?request=getFeature&storedquery_id=fmi::observations::lightning::simple"
               "&bbox="+bbox+
               "&parameters="+params+
               "&starttime="+starttime+
               "&endtime="+endtime
               )

        # print(url)
        # get data from url
        f = urllib2.urlopen(url,timeout=30)
        tree = ET.ElementTree(file=f)
        root = tree.getroot()
        f.close()
        
        # data contains 4 parameters which are displayed one
        # after another. These parameters have same timestamps
        # and coordinates, so those needs to be outputted only once
        # per observations.
        validparameters = ["peak_current", "multiplicity", "cloud_indicator", "ellipse_major"] 
        timestamps      = []
        values          = []
        coordinates     = []
        names           = []
        for first_child in root.iter("{http://xml.fmi.fi/schema/wfs/2.0}Time"):
            timestamps.append(first_child.text)
        for first_child in root.iter("{http://www.opengis.net/gml/3.2}pos"):
            coordinates.append(first_child.text)
        for first_child in root.iter("{http://xml.fmi.fi/schema/wfs/2.0}ParameterValue"):
            values.append(first_child.text)
        for first_child in root.iter("{http://xml.fmi.fi/schema/wfs/2.0}ParameterName"):
            names.append(first_child.text)

        # combine observations as one array:
        # 1) multiplicity, cloud_indicator ellipse_major
        # add timestamp and coordinates
        # 2) time lat lon peak_current multiplicity cloud_indicator ellipse_major
        index  = 0
        output = ""
        outputarray = []
        for i in xrange(0,len(values)):
            if(index == 4):
                outputarray.append(output)
                output = ""
                output = output + " " + values[i]
                index = 0
            elif(i==len(values)-1):
                output = output + " " + values[i]
                outputarray.append(output)
            else:
                output = output +" " + values[i]
            index = index + 1

        outputcoordinates = []
        outputtimes       = []
        for i in range(0, len(names), len(validparameters)):
            # remove possible leading and trailing spaces
            # and add every nth value to new arrays
            # i.e. 4 parameters, every 4th time and coordinate value
            cord = coordinates[i].strip()
            time = timestamps[i].strip()
            outputcoordinates.append(cord)
            outputtimes.append(time)

        output = []
        data   = ""
        for i in range(0, len(outputarray)):
            # remove leading and trailing spaces
            data = outputtimes[i]+" "+outputcoordinates[i]+" "+outputarray[i].strip()
            output.append(data)

        output = self.formatter(output, "csv", lines)
        return output

        
#if __name__ == '__main__':
    #salamiclass.run_class()

    

# testing
# test = salamiclass()    
# test.parse_data()
