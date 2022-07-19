import pandas as pd
import matplotlib.pyplot as plt

def data_vis_ages():
    df = pd.read_csv('csv/survey_results_public.csv')
    df2 = df.groupby(['Age'])['Age'].count()
    plot = df2.plot.pie(y='Category',  startangle=0)
    plt.ylabel('')
    percents = df2.to_numpy() * 100 / df2.to_numpy().sum()
    plt.legend( bbox_to_anchor=(1.35,1.1), loc='best',
                labels=['%s, %1.1f %%' % (l, s) for l, s in zip(df2.index,percents)])
    plt.show()




if __name__ == '__main__':
    data_vis_ages()