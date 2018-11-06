import pandas as pd

def chunk_file(file_path):
	chunk_size = 5000
	batch_no = 1
	for chunk in pd.read_csv(file_path, chunksize=chunk_size):
		chunk.to_csv(file_path + str(batch_no) + '.csv', index=False)
		batch_no +=1
