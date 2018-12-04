# Tech Company and their IPO year
d = {'Apple':2017, 'Microsoft':1985, 'Comcast':1990, 'Facebook':2012, 'IBM':1978, 'Salesforce':2004, 'Amazon':1997, 'Sony':1978}

# sort by dictionary key
sorted_d = dict(sorted(d.items(), reverse=False))
print(sorted_d)

# sort by dictionary value
sorted_d = dict(sorted(d.items(), key=lambda kv:kv[1], reverse=False))
print(sorted_d)
