import pandas as pd
import matplotlib.pyplot as plt
from functions.unanswerd_questions_percentage import unanswered_questions_percentage
import numpy as np


def unanswered_questions_percentage_visualization():  # pragma: no cover
    """
    this function will call the unanswered_questions_percentage function and represent the output in a bar chart
    :param:None
    :return:None
    """
    list_of_dicts = unanswered_questions_percentage()
    df = pd.DataFrame(list_of_dicts, columns=['tag', 'unanswered_7days', 'unanswered_30days', 'unanswered_all_time'],
                      index=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    x_var = df['tag'].values
    w = 0.2
    bar1 = np.arange(len(x_var))
    bar2 = [i + w for i in bar1]
    bar3 = [i + w for i in bar2]
    plt.bar(bar1, df['unanswered_7days'], w, label="unanswered question in the last 7 days")
    plt.bar(bar2, df['unanswered_30days'], w, label="unanswered question in the last 30 days")
    plt.bar(bar3, df['unanswered_all_time'], w, label="unanswered question all time")
    plt.legend()

    plt.xticks(bar1 + w / 2, x_var, rotation=45)
    plt.xlabel("Tags")
    plt.ylabel("Unanswered questions percentage")
    plt.title("Tags Vs Unanswered questions")
    plt.show()


if __name__ == '__main__':  # pragma: no cover
    unanswered_questions_percentage_visualization()
