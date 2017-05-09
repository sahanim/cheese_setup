
import ystockquote
import time
import datetime

class server:
	while True:
		
		
		now = datetime.datetime.now()
		second = now.second
		minute = now.minute
		hour = now.hour
		day = now.day
		month = now.month
		year = now.year
		# Monday = 1, Sunday = 7
		weekday = now.weekday() + 1
		filename = 'TSLA_' + str(year) + "_" + str(month) + "_" + str(day) + ".txt"
		f = open(filename, 'a')
		try:
			price = ystockquote.get_last_trade_price('TSLA')

			timestamp = ystockquote.get_last_trade_time('TSLA')
			volume = ystockquote.get_volume('TSLA')
			# print(price + " " + timestamp + " " + volume + "\n")
		except:
			print("JSON DECODE ERROR") 
		time.sleep(.1)
		if (weekday <= 5):
			if (hour == 16 and minute <= 30):
				quote = str(price) + " " + str(volume) + " " + str(year) + " " +  str(month) + " " + str(day) + " " + str(hour) + " " + str(minute) + " " + str(second)
				print(quote)
				f.write(quote + '\n')
			if (hour >= 9 and hour <= 24):
				quote = str(price) + " " + str(volume) + " " + str(year) + " " +  str(month) + " " + str(day) + " " + str(hour) + " " + str(minute) + " " + str(second)
				print(quote)
				f.write(quote + '\n')
		f.close()

newserver = server()