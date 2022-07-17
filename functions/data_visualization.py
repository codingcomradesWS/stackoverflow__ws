import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from functions.unanswerd_questions_percentage import unanswered_questions_percentage
import numpy as np

list_of_dicts = unanswered_questions_percentage()
df = pd.DataFrame(list_of_dicts, columns=['tag', 'unanswered_7days', 'unanswered_30days', 'unanswered_all_time'],
                  index=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(df)
x_var = df['tag'].values
y_var = df['unanswered_7days'].values

w = 0.2
bar1 = np.arange(len(x_var))
bar2 = [i + w for i in bar1]
bar3 = [i + w for i in bar2]
plt.bar(bar1, df['unanswered_7days'], w, label="unanswered question in the last 7 days")
plt.bar(bar2, df['unanswered_30days'], w, label="unanswered question in the last 30 days")
plt.bar(bar2, df['unanswered_30days'], w, label="unanswered question all time")
plt.bar(bar3, df['unanswered_all_time'], w)
plt.xticks(bar1 + w / 2, x_var, rotation=45)
plt.xlabel("Tags")
plt.ylabel("Unanswered questions")
plt.title("Tags Vs Unanswered questions")
plt.legend()
plt.show()
