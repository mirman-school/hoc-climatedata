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
    filtered = list(it.takewhile(lambda d: d.date == date, data))
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
    filtered = list(filter(lambda d: d.high >= temp, data))
    return filtered

def lower_than(data, temp):
    '''
    Returns a list of all DataPoints that had temps lower than the given temp
    '''
    filtered = list(filter(lambda d: d.low <= temp, data))
    return filtered

def had_precip(data,precip):
    '''
    Returns a lits of all DataPoints that had precipitation
    '''
