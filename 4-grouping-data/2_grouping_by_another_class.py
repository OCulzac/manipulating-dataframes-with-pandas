""" Grouping by another series
In this exercise, you'll use two data sets from Gapminder.org to investigate the average life expectancy (in years) at birth in 2010 for the 6 continental regions. To do this you'll read the life expectancy data per country into one pandas DataFrame and the association between country and region into another.

By setting the index of both DataFrames to the country name, you'll then use the region information to group the countries in the life expectancy DataFrame and compute the mean value for 2010.

The life expectancy CSV file is available to you in the variable life_fname and the regions filename is available in the variable regions_fname.

Instructions
100 XP
Instructions
100 XP
Read life_fname into a DataFrame called life and set the index to 'Country'.
Read regions_fname into a DataFrame called regions and set the index to 'Country'.
Group life by the region column of regions and store the result in life_by_region.
Print the mean over the 2010 column of life_by_region. """
