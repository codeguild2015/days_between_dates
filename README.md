# days_between_dates
Calculate the number of days from a given date (month, day, and year) to the next occurrence of another date (month and day).

## Purpose
This project requires more complex loop logic and, because of the overall complexity, it requires an incremental approach to development. You need to break the logic down into functions. It is essential to have a clear design before writing code, and to build the code part-by-part, testing each part before moving on. 

## Pair Assignment
Work together with one classmate.

Before writing code at the computer, you should work together and independently on the design. Each of you should be able to clearly explain how the program or a part of the program will work. When you are convinced that you both understand how the code will work, then and only then are you ready to write the code.
Write the code part by part. Start with an overall design, then work out the details of one part at a time. Typically you will sit down to code and test one function. When that function is working, leave the computer to finish designing details of the next function, and return to the computer to write and test it. Don't be too surprised if you need to make some revisions to previously written functions.
When you are ready to write and test some code, one person (the “driver”) controls the keyboard and mouse, while the other makes comments and suggestions. Take turns, so each person experiences both roles.
Both students should turn in the identical work, and the program you turn in should clearly indicate both authors. You should not share code with other teams, but you may discuss design approaches with others. If you do, you should also credit your collaborators in the header comment (docstring) of your program.

## How many days until my next birthday?
The overall problem is to calculate the number of days from a given date (month, day, and year) to the next occurrence of another date (month and day). For example, we could be determing the number of days until winter break, or until your birthday. The answer will always be less than a year (the number of days from June 12 to June 12 is 0, not 365).

Examples:
How many days from the first day of fall term 2012 until the first day of summer break (September 24, 2012 to June 15, 2013)?
```
$ python3 days_till.py 2012 9 24 6 15
264
``` 
How many days in fall term, i.e., from the first day of classes in fall term until the Saturday that starts winter break (September 30, 2013 to December 14, 2013)?
```
$ python3 days_till.py 2013 9 30 12 14
75
```
Note there is one day until tomorrow, and zero days until today:
```
$ python3 days_till.py 2013 1 17 1 18
1
$ python3 days_till.py 2013 1 17 1 17
0
```
If we try to start on a non-existent date, an error message is printed:
```
$ python3 days_till.py 2013 2 29 3 13
Must start on a valid date between 1800 and 2500
```
But for the ending date, we treat March 1 as being equal to February 29 (so we can ask how many days until February 29 even in a non-leap year).
```
$ python3 days_till.py 2013 1 31 2 29
29
```

## Input specification
The integers given as the start date should be a valid date between January 1, 1800 and December 31, 2500, inclusive. If the integers entered do not form a valid date in that range, the program will print an error message and exit.
Examples
```
$ python3 days_till.py 1498 12 15 1 25
Must start on a valid date between 1800 and 2500
$ python3 days_till.py 2011 2 29 3 15
Must start on a valid date between 1800 and 2500
$ python3 days_till.py 2011 9 31  3 15
Must start on a valid date between 1800 and 2500
```
Notes: February 29 is a valid starting date in leap years but not in other years. It is always valid to give February 29 as an ending date. If the ending year is not a leap year, we treat Feb 29 as equivalent to March 1.
Usually, a year is a leap year if it is divisible by four, but the rules are a little more complicated:

Divisible by 4 |	Divisible by 100 | Divisible by 400 |	Leap year?
---------------|--------------------|-----------------|-------------
No |	No | No |	No
Yes |	No |	No |Yes
Yes |	Yes |	No | No
Yes |	Yes |	Yes |	Yes

Note that leap years are important not only in determining whether an input date is valid, but also in determining the number of days between two dates.

## Other requirements
Your program must be divided into at least four well-designed functions.

Although Python has some special libraries for manipulating dates and times, your program may not use them.
The input and output of your program should follow exactly the form shown in the examples above. 

Be sure to include a documentation string in each function, except that you may omit them from “scaffolding” functions that are used only for testing and debugging your program.

## Incremental development
Don't try to tackle this project all at once. Write and test one part at a time.

# Starter code
I have provided a skeleton file to get you started, and to provide an example of how we process the command line in a typical Python program. The starter code uses the Python argparse library module to read the command line, provide a usage method, and make sure the year, month, and day numbers that we expect are really integers. It's tedious but not complicated. The argparse module does not check for the year being within range 1800-2500, the month being in the range 1-12, etc. You'll have to do that data validation in your code.
The starter code also demonstrates another Python idiom:

  if __name__ == "__main__":
    main()
  
It is very common for a Python file foo.py to be used in two different ways. It can be run as a main program from the command line, or within a batch script, and it can also be loaded as a module to makes its functions available to another program. This little test at the end of the code check to see if the program is being run as a main program, and invokes the main( ) function only if it is. We'll make more use of this later when we decompose programs into multiple modules.
I've placed FIXME comments in a couple of places to indicate where you will need to make most of your changes in the skeleton code. Don't forget to delete these comments before turning in your program.


  <h1>Grading rubric</h1>
  <table width="85%" border="0" cellpadding="2">
    <tr>
      <th colspan="2" scope="col">Functional correctness</th>
      <th width="8%" scope="col">&nbsp;</th>
      <th width="60%" scope="col">&nbsp;</th>
      <th width="1%" scope="col">&nbsp;</th>
      <th width="3%" scope="col">40</th>
    </tr>
    <tr>
      <td width="5%">&nbsp;</td>
      <td width="23%"><p>Exactly meets input/output spec</p>        </td>
      <td>10</td>
      <td>5 = minor discrepancy, 0 = ignored spec</td>
      <td>&nbsp;</td>
      <td>&nbsp;</td>
    </tr>
    <tr>
      <td>&nbsp;</td>
      <td>Correct calculations</td>
      <td>20</td>
      <td><p>20 = works for all cases, 15 = works for almost all cases, 
      10 = works for most cases (e.g., except some leap years), 
      5 = works for some cases</p></td>
      <td>&nbsp;</td>
      <td>&nbsp;</td>
    </tr>
    <tr>
      <td>&nbsp;</td>
      <td>Input validation</td>
      <td>10</td>
      <td>10 = rejects all improper dates exactly as specified, 
      5 = mostly validates data, some problems, 0 = doesn't validate data</td>
      <td>&nbsp;</td>
      <td>&nbsp;</td>
    </tr>
    <tr>
      <th colspan="2">Other requirements</th>
      <td>&nbsp;</td>
      <td>&nbsp;</td>
      <td>&nbsp;</td>
      <td>40</td>
    </tr>
    <tr>
      <td>&nbsp;</td>
      <td><p>Header docstring</p>        </td>
      <td>10</td>
      <td>10 = as specified, 7 = minor issue, 5 = as #comment, 0 = missing</td>
      <td>&nbsp;</td>
      <td>&nbsp;</td>
    </tr>
    <tr>
      <td>&nbsp;</td>
      <td>Function header docstrings</td>
      <td>8</td>
      <td>8 = good docstrings in all functions, 6 = minor problems, 
      4 = incorrect or multiple missing, 0 = docstrings not provided</td>
      <td>&nbsp;</td>
      <td>&nbsp;</td>
    </tr>
    <tr>
      <td>&nbsp;</td>
      <td>Functional decomposition</td>
      <td>12</td>
      <td><p>12 = good decomposition into at least four functions (main counts), 
      8 = decomposition has some issues, such as misuse of global variables,
      6 = serious problems in functional decomposition, 
      0 = did not decompose into functions, or other serious problem</p></td>
      <td>&nbsp;</td>
      <td>&nbsp;</td>
    </tr>
    <tr>
      <td>&nbsp;</td>
      <td>Program style and readability</td>
      <td>10</td>
      <td><p>10 Good variable names, indentation, etc --- 
      very readable code, 8 = minor issues, such as inconsistent indentation, 
      5 = major issues that interfere with readability of code, 
      0 = unreadable mess </p></td>
      <td>&nbsp;</td>
      <td>&nbsp;</td>
    </tr>
    <tr>
      <th colspan="2">Total</th>
      <td>&nbsp;</td>
      <td>&nbsp;</td>
      <td>&nbsp;</td>
      <td>80</td>
    </tr>
  </table>
