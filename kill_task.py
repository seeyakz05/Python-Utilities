import os

taskName = 'EXCEL.EXE'
os.system("taskkill /f /im " + taskName)
input('Press to exit')
