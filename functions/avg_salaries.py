import numpy as np
import pandas as pd
data_set_one = pd.read_csv('../csv/survey_results_public.csv')
# print(data_set_one.head())
x_var = data_set_one['Country'].values
print(x_var[0])
# print(x_var)
