lstX = list(range(1, 101))

def chunk_list(lst, chunk_size):
	for i in range(0, len(lst), chunk_size):
		yield lst[i:i + chunk_size]

print(list(chunk_list(lstX, 16)))

chunk_size = 16
output = [lstX[i:i + chunk_size] for i in range(0, len(lstX), chunk_size)]
print(output)
