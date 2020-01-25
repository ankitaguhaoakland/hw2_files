# -*- coding: utf-8 -*-
"""
Created on 2018-03-20

@author: misken
"""

import re


def process_youtube(fn_youtube , fn_out):
    """
    Function
    --------
    process_youtube

    Use regex to create a file with records only from a specific category_id.

    Parameters
    ----------
    fn_youtube : str
        Name of YouTube trending stats file

    fn_out : str
        Name of new YouTube trending stats file containing only records of
        interest.

    Returns
    -------
    Nothing. Counts of lines matched and not matched are displayed
    at the end. For lines in category_id 28, the counts by date are captured
    in a dictionary and displayed at the end.

    Example
    -------
    process_youtube('USvideos.csv' , 'USvideos_SciTech.csv')

    """

    # Initialize empty dict for counts by date
    daily_counts = ???

    # regex for line filter - only include lines from category_id = 28
    # Snippet from first line:
    # 2kyS6SvSYSE	17.14.11	WE WANT TO TALK ABOUT OUR MARRIAGE	CaseyNeistat

    re_filter = re.compile(???)

    # Initialize counters
    num_lines_matched = 0
    num_lines_not_matched = 0

    # Initialize list to store output lines
    outputlines = ???

    # Open the input file
    with open(???) as ???:

        # Loop over the lines in the file
        for line in ???:
            # Let's strip off any end of line characters
            line = ???

            # See if regex for filtering matches this line
            mfilter = ????

            # If we matched, update counters and store line in list for output
            if ???:

                # Increment counter of number of lines matched
                ???

                # Get the date from first capture group
                trending_date = ???

                # Increment count by trending date
                daily_counts[???] = ??? + 1

                # Append line to master output list
                ????

            else:
                # Increment number of lines not matched counter
                ???


    # Write the output file
        # There are a few ways to write out a list of strings to a file. Figure
        # out one way to do it and then do it.

    # # Print out the counts dictionary
    for ??? in daily_counts.???:
        print (???)

    # All done, print the results
    print("\nNum lines matched --> {}".???)
    print(???)


if __name__ == '__main__':
    process_youtube('./data/USvideos.csv', 'USvideos_SciTech.csv')