import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
from scipy.stats import norm

file_path = 'data.csv'
raw_data = pd.read_csv(file_path, skiprows=2)

""" Step 1. Data Cleanup """
# Remove people with no age information available
data = raw_data[raw_data['Age'].apply(lambda x:x.isnumeric())]
# Convert Age field from object dtype to integer dtype
data['Age'] = data['Age'].astype(int).values.tolist()
# Reset row index
data.reset_index(inplace=True)

""" Step 2. Perform simple summary statistics """
summary = data['Age'].describe()

# There are few other things like variance, Skewness, Coefficient of variation I would like to add
summary['Skewness'] = data['Age'].skew()
summary['Variance'] = data['Age'].var()
summary['CV'] = summary['std'] / summary['mean']

# Now, we can ask questions like
# Who are the youngest and oldest woman on the Forbe most powerful women of 2018 list
print(data[data['Age']==sorted(data['Age'], reverse=True)[0]])
print(data[data['Age']==sorted(data['Age'], reverse=False)[0]])

# Which country accounted for most of the women on the list
print(Counter(data['Country']))

# Which industry sector accounted for most of the women on the list
print(Counter(data['Category']))

# ---------------------------------
# Graph normal distribution
# ---------------------------------
plt.plot(sorted(data['Age']), norm.pdf(sorted(data['Age']), summary['mean'], summary['std']), '-o')
plt.hist(data['Age'], normed=True)
plt.show()
