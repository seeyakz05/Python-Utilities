import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
from scipy.stats import norm

file_path = r'C:\Users\jjenn\Google Drive\Jie Jenn (YouTube)\Python\100 Powerful Women List Data Analysis' + '\\data.csv'
raw_data = pd.read_csv(file_path, skiprows=2, encoding='utf-8')

"""
Let's say I am interested in understand how age plays a factor
"""

""" Step 1. Data Cleanup """
# Remove people with no age information available
data = raw_data[raw_data['Age'].apply(lambda x:x.isnumeric())]
# Convert Age field from object dtype to integer dtype
data['Age'] = data['Age'].astype(int).values.tolist()
# Reset row index
data.reset_index(inplace=True)

""" Step 2. Perform simple summary statistics """
# 50% = Median
# count = Sample population size
summary = data['Age'].describe()

# here, there are few other things like variance, Skewness, Coefficient of variation I would like to add
summary['Skewness'] = data['Age'].skew()
summary['Variance'] = data['Age'].var()
summary['CV'] = summary['std'] / summary['mean']


# here, we can ask questions like.
# who are the youngest and oldest woman on the Forbe most powerful women in 2018 list
print(data[data['Age']==sorted(data['Age'], reverse=True)[0]])
print(data[data['Age']==sorted(data['Age'], reverse=False)[0]])

# which country accounted for most of the women on the list
print(Counter(data['Country']))

# which industry sector accounted for most of the women on the list
print(Counter(data['Category']))

# graph normal distribution
# pdf --> Probability density function
plt.plot(sorted(data['Age']), norm.pdf(sorted(data['Age']), summary['mean'], summary['std']), '-o')
plt.hist(data['Age'], normed=True)
plt.show()


# Plot between -10 and 10 with .001 steps.
x_axis = np.arange(-10, 10, 0.001)
# Mean = 0, SD = 2.
plt.plot(x_axis, norm.pdf(x_axis,0,2))
plt.show()