from dataloader import *

DATA_PATH = "tempdata.csv"

data = load_data(DATA_PATH)

def get_date(datestamp):
    '''
    Loads data for a specific date, given a datestamp in YYYYMMDD format
    '''
    global data
    date = DataPoint.create_date(datestamp)
    print("Searching for {}".format(date))
    filtered = list(filter(lambda d: d.date == date, data))
    if len(filtered) > 0:
        return filtered.pop()
    else:
        raise ValueError("No such date!")

def get_range(data,start,end):
    '''
    Takes dataset and start/end YYYYMMDD strings and returns datapoints only between them
    '''
    start_date = DataPoint.create_date(start)
    end_date = DataPoint.create_date(end)
    return list(filter(lambda d: d.date >= start_date and d.date <= end_date, data))

def higher_than(data, temp):
    '''
    Returns a list of all DataPoints that had temps higher than the given temp
    '''
    return list(filter(lambda d: d.high >= temp, data))

def lower_than(data, temp):
    '''
    Returns a list of all DataPoints that had temps lower than the given temp
    '''
    return list(filter(lambda d: d.low <= temp, data))

def has_precip(data,precip):
    '''
    Returns a list of all DataPoints with precipitation > 0
    '''
    return None # You need to implement this, using the above functions as a pattern!
