import re
def fractor(seconds):
	m, s = divmod(seconds, 60)
	h, m = divmod(m, 60)
	d, h = divmod(h,24)
	w, d = divmod(d, 7)
	mn, w = divmod(w, 4)
	y, mn = divmod(mn, 12)
	return (y, mn, w, d, h, m, s)


def downtime(spd, siz):
	has_error = False
	time_dict = {}
	time_dict1 = {}
	has_error,time_dict1 = check(spd,siz)

	if has_error == True:
		time_dict['error'] = "INVALID ENTRIES. PLEASE TRY AGAIN!"
		time_dict['viz'] = "none"
		return time_dict, has_error
	speed_limit = float(''.join(str(e) for e in(re.findall(r'(?<![a-zA-Z:])[-+]?\d*\.?\d+', spd))))	 #finds the speed digit
	speed_unit = ''.join(re.findall(r'[a-zA-Z]',spd)) #finds the unit whether is in kbps or mbps or tbps
	size_limit = float(''.join(str(e) for e in(re.findall(r'(?<![a-zA-Z:])[-+]?\d*\.?\d+', siz))))
	size_unit =''.join( re.findall(r'[a-zA-Z]', siz))
	speed_unit = speed_unit.lower()
	size_unit = size_unit.lower() 
	speed = speed_limit
	unit_dict = {"kb": 1,"mb": 1024,"gb": 1024**2,"tb": 1024**3}
	speed = float(''.join(str(e) for e in[(value) for key, value in unit_dict.iteritems() if key.startswith(speed_unit[:2])])) * speed_limit #converts the speed in kbps
	size = float(''.join(str(e) for e in[(value) for key, value in unit_dict.iteritems() if key.startswith(size_unit[:2])])) * size_limit #converts the size to kilobytes
	years, months, weeks, days, hours, minutes, seconds = fractor(size/speed)
	time_dict = {'years': years, 'months': months, 'weeks': weeks, 'days': days, 'hours': hours, 'minutes': minutes, 'seconds': seconds}
	for key, value in time_dict.iteritems(): time_dict[key] = int(value)
	time_dict.update(time_dict1)
	time_dict['viz'] = "block"
	return  time_dict,has_error
	
def check(spd,siz):
	has_error = False
	dic1 = {}
	dic = dict(speed = spd, size = siz )
	for key,value in dic.iteritems():
		if re.search('[0-9]+',value) and re.search('[a-zA-Z]+',value) and not re.search('^$',value):
			has_error = False
			dic1[key] = dic[key]
		else: has_error = True
	return has_error, dic1

#print downtime("120kbps","700")
