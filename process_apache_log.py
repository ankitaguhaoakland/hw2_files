# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 23:50:39 2013

@author: mark
"""

# Import the re module to gain regex functionality.
import re

# Define a function for processing apache log files
def process_apache_log(logfile):
   """
   Count server hits per month from Apache log file.
   
   Returns dict containing number of server hits by month 
   using regex to find the month
   and using a dictionary keyed by month to keep track of running count.
   
   This is NOT a MapReducey approach. It's the first way I did it before
   even reading the MapReduce paper. See process_apache_log_mr.py for
   an attempt at something done in context of MapReduce.
   """

   # local - - [24/Oct/1994:13:41:41 -0600] "GET index.html HTTP/1.0" 200 150

   # Create a compiled regex pattern to capture the three letter month
   # abbreviation. the re.I is to specify case insensitive match.
   rgx = re.compile('(local|remote) - - \[[0-9]{1,2}/([a-zA-Z]{3,3})/',re.I)

   monthly_counts = {}  # Create an empty dictionary
   monthly_counts['NO_MONTH'] = 0  # Add a key called 'NO_MONTH' for counting
                                   # recs with missing months. Init value is 0.
   
   with open(logfile) as f: # The file named logfile is opened and f is the
                            # file 'handle'. By doing it this way, the file
                            # will automatically get closed when the with
                            # block completes.
       
       for line in f:       # Loop one line at a time through the file
       
           m = re.match(rgx,line) # Attempt the regex match and store result in m
           
           if m:                  # As long the regex matches, m will be non-empty
                                  # and thus will get interpreted as True for the if
           
               month = m.group(2) # The month abbreviation is the 2nd capture group
               
               # Note the use of .get which allows a default value to
               # be returned if the month key doesn't yet exist. For
               # example monthly_counts['Jan'] will cause an error if
               # Jan hasn't been added yet to the dictionary.
               monthly_counts[month] = monthly_counts.get(month, 0) + 1
               
           else:
               
               # If the regex didn't match, increment the 'NO_MONTH' value
               monthly_counts['NO_MONTH'] = monthly_counts['NO_MONTH'] + 1
   
   # The following two statements are OUTSIDE the with block. They will
   # execute one time only, at the end of the program.            
   print (monthly_counts)
   print (sum(monthly_counts.values()))    
            

def findbadline(logfile):
    with open(logfile) as f: # The file named logfile is opened and f is the
                            # file 'handle'. By doing it this way, the file
                            # will automatically get closed when the with
                            # block completes.
       
       for line in f:       # Loop one line at a time through the file
           print (line)

# The lines below are NOT part of the function above, they are just part of
# this Python script file. They represent a common "pattern" in creating
# Python scripts. Essentially, the if is checking to see if this 
# process_apache_log.py script was run as a 'main' program (either run
# from the command line or run by pushing the Run button in the IDE). If it
# was, it simply calls the function above with a default filename. If instead,
# this file was imported by another script and then the function called from
# that program, the filename to process would be passed in as part of the
# function call. Of course, instead of supplying a default filename here,
# we could instead allow for the filename to be passed in as a command line
# argument. See p202-205 in PCfB for basic info on dealing with command line
# arguments. See the accepted answer in the following StackOverflow question
# for more details: http://stackoverflow.com/questions/419163/what-does-if-name-main-do

if __name__ == '__main__':
    process_apache_log('data/apache.log')
    #findbadline('apache.log')
    
