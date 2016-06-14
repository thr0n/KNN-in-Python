# K-Nearest Neighbors (in Python)

This repository contains two K-Nearest Neighbors (KNN) examples written in Python.  

## Movie genre classification

A basic KNN implementation. An unknown movie genre will be calculated with the use of six sample data sets.

### Sample output

```
([Movie] : title='He's not reall into dudes'; #kisses=2; #kicks=100, genre='Romance', 18.867962264113206)
([Movie] : title='Beautiful Woman'; #kisses=1; #kicks=81, genre='Romance', 19.235384061671343)
([Movie] : title='California Man'; #kisses=3; #kicks=104, genre='Romance', 20.518284528683193)
([Movie] : title='Kevin Longblade'; #kisses=101; #kicks=10, genre='Action', 115.27792503337315)
([Movie] : title='Robo Slayer 3000'; #kisses=99; #kicks=5, genre='Action', 117.41379816699569)
([Movie] : title='Amped'; #kisses=98; #kicks=2, genre='?', 118.92854997854805)

Genre 'Romance' has been added to '?'! Check next line:
[Movie] : title='?'; #kisses=18; #kicks=90, genre='Romance'
```

## Wine quality classification

This is an extendend version of the previous movie classification.  

A `.csv`-file will be used to support sample data. This file contains various information about several variants of the Portuguese "Vinho Verde" wine (source: https://archive.ics.uci.edu/ml/datasets/Wine+Quality) including a "score" that describes the quality of the wine. The last row of of the `.csv`-file has been taken as "wine to be classified" - the corresponding score shall be calculated using KNN.  

In contrast to the movie classifier, this application is able to normalize the values of the sample data set.

### Execution options

There are five constants to define the application's behavior:  
`INPUT_FILE` - the `csv`.file to be read
`EXPECTED_SCORE` - the original score of the regarded wine (taken from the original `.csv`-file)
`NORMALIZE` - enable or disable sample data normalization (`boolean`)
`DEBUG` - enable or disable the debug/verbose mode (`boolean`)
`FIND_SMALLEST_K` - enable or disable the `FIND_SMALLES_K` mode (otherwise we )

### Sample output

```
# ------------------------------------------------------
#  File = winequality-red.csv
#  K = 500
#  Expected result = 6
#  FIND_SMALLEST_K = False
#  NORMALIZE = False
#  DEBUG = True
# ------------------------------------------------------

[DEBUG] The wine to be classified: (6, 0.31, 0.47, 3.6, 0.067, 18, 42, 0.99549, 3.39, 0.66, 11, '?')
[DEBUG] CSV file read! Size of the sample data set: 1598 rows

[DEBUG] These are the top 10 candidates (this is just to show that sorting is working!):
[DEBUG] 0.36 -> 1.893854480180565
[DEBUG] 0.36 -> 1.893854480180565
[DEBUG] 0.6 -> 2.91786671909462
[DEBUG] 0.55 -> 2.957259097897917
[DEBUG] 0.58 -> 3.1041112454936277
[DEBUG] 0.73 -> 3.152948449324853
[DEBUG] 0.83 -> 3.203012871173015
[DEBUG] 0.55 -> 3.3127065991572513
[DEBUG] 0.31 -> 3.3173818143982166
[DEBUG] 0.31 -> 3.3173818143982166

[DEBUG] This is the score count:
[DEBUG] 3 -> 3
[DEBUG] 4 -> 13
[DEBUG] 5 -> 189
[DEBUG] 6 -> 231
[DEBUG] 7 -> 61
[DEBUG] 8 -> 3

--------------------------------------------------------
Nearest Score = 6
Nearest score and expected score are matching!
```

## Known issues

The nearest score will be evalutated to `5` instead of `6` if `NORMALIZATION` is enabled.


## Author
Hendrik Thorun  
hendrik.thorun@stud.fh-luebeck.de  
Date: 14 June 2016


