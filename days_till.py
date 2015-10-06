"""
How many days from yyyy mm dd until the next mm dd
Authors: #FIXME: List both authors here
Credits:  #FIXME: If you discussed design with others who are not authors
  of this code, credit them here. 

Usage example: python days_till.py  2012 09 24 06 14
    (first day of fall classes until end of spring finals)
"""

import sys  # For exit with a message
import argparse # Fancier command line parsing

# FIXME: Most of your code goes here
        

def main():
    """
    Main program gets year number from command line, 
    invokes computation, reports result on output. 
    args: none (reads from command line)
    returns: none (write to standard output)
    effects: message or result printed on standard output
    """
    ## The standard way to get arguments from the command line, 
    ##    make sure they are the right type, and print help messages
    parser = argparse.ArgumentParser(description="Compute days from yyyy-mm-dd to next mm-dd.")
    parser.add_argument('year', type=int, help="Start year, between 1800 and 2500")
    parser.add_argument('start_month', type=int, help="Starting month, integer 1..12")
    parser.add_argument('start_day', type=int, help="Starting day, integer 1..31")
    parser.add_argument('end_month', type=int, help="Ending month, integer 1..12")
    parser.add_argument('end_day', type=int, help="Ending day, integer 1..12")
    args = parser.parse_args()  # will get arguments from command line and validate them
    year = args.year
    start_month = args.start_month
    start_day = args.start_day
    end_month = args.end_month
    end_day = args.end_day
    
    #FIXME: The first print commands below are just for debugging, and will need
    #  be be removed or commented out. Calls to is_valid can be uncommented when
    #  you have written a function to check validity. 
    print("Checking date ", str(year) + "/" + str(start_month) + "/" + str(start_day))
    # if not is_valid(year, start_month, start_day) : 
    #     sys.exit("Must start on a valid date between 1800 and 2500")
    # if not is_valid(2000, end_month, end_day):
    #    sys.exit("Ending month and day must be part of a valid date")
    # print("Days in starting month:", days_in_month(start_month, year))
    # print(days_between(year, start_month, start_day, end_month, end_day))   


if __name__ == "__main__":
    main()
        
