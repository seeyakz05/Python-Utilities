lst = [[1, 2, 3], [4, 5, 6], [7], [8, 9]]

# method1
flat_list = []
for sublist in lst:
	for item in sublist:
		flat_list.append(item)
print(flat_list)

# method2
flat_list = [item for sublist in lst for item in sublist	]
print(flat_list)
