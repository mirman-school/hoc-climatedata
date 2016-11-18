# Visualizing Climate Data: Hour of Code 2016

In this exercise, you will use the Python programming language to analyze a dataset to discover patterns, trends, and truths about weather data in our area.

## What's in the box
Having downloaded this folder, you see several files:

* `README.md`: This file you're reading RIGHT NOW
* `dataloader.py`: A helper library that will load the data usefully for us to explore
* `explorer.py`: Helper functions for you to explore and filter the data
* `visualizer.py`: Where you create the visualizations of the data
* `tempdata.csv`: Highs, lows, and precipitation for 90049 from 2011 - 2016. The raw data. You can look at this if you want, but we actually don't use it once it passes through the code in `dataloader.py`

## How to read these files
### `explorer.py`
This file defines _functions_ that parse the data. Let's take the function `higher_than()`:

    def higher_than(data, temp):
        '''
        Returns a list of all DataPoints that had temps higher than the given temp
        '''
        return list(filter(lambda d: d.high >= temp, data))

Functions in Python are just like functions in math: they take _arguments_ in, and use them to perform and operation. Then they _return_ a result. In math, we use `f(x)` to define functions. In Python, we use the keyword `def`. Then, in tabbed-in lines below, we describe the operations of the function. In this case, we returned a "filtered" list of datapoints from the full dataset; the filter make sure the remaining datapoints have a high temperature that is greater than or equal to the temperature passed to the function.

See if you can similarly interpret the other functions in this file.

If you've read to the bottom, you've discovered a "broken" function: `has_precip()`. That's yours to implement. Using the other functions as a pattern, implement the `has_precip()` function so it returns only datapoints with precipitation.

### `dataloader.py`
Although you don't have to modify this file, it is helpful to see exactly how we load our data. Simply put, we pull the raw text from `tempdata.csv` and turn it into a useful data structure. We call these objects `DataPoint`s, and each one has `high`, `low`, and `precip` properties.

Starting on line 21, we define a function called `load_data()` that returns a _list_ of `DataPoint` objects that we can work with. They are helpfully in chronological order.

### `visualizer.py`
This is where we write our code. You'll see two example functions: one for printing text to the Terminal, and one for creating graphs of our data. We use [pyplot](http://matplotlib.org/users/pyplot_tutorial.html) to generate our graphs.

## Running your code
To run the Python code, you will use Terminal. Open it up, and use the `cd` command to navigate to this folder. Terminal opens one level above your `Downloads/` folder, so if you downloaded/unzipped this folder in your Downloads, enter:

    cd Downloads/hoc-climatedata-master

If it's on your Desktop, same thing, but `Desktop` in lieu of `Downloads`.

From there, to run and re-run your code, enter:

    python3 visualizer.py
