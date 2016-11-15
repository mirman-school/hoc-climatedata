import csv
import datetime as dt

class DataPoint:
	@staticmethod
	def create_date(datestr):
		year = int(datestr[0:4])
		month = int(datestr[4:6])
		day = int(datestr[6:8])
		return dt.date(year,month,day)

	def __init__(self,data):
		self.date = DataPoint.create_date(data[5])
		self.precip = float(data[6])
		self.high = int(data[7])
		self.low = int(data[8])

	def __str__(self):
		return "On {}, the high was {} and the low was {}.".format(self.date, self.high, self.low)

def load_data(path):
	data = []

	with open(path) as f:
		rows = csv.reader(f)
		next(rows)
		for r in rows:
			data.append(DataPoint(r))

	return data
