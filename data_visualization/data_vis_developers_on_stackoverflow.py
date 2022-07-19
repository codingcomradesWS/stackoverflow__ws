import pandas as pd
import matplotlib.pyplot as plt


def developers_on_stackoverflow():  # pragma: no cover
    """
    This function is returning a graph with the kind of developers who is visiting and acting on stackoverflow with a
    percentage
    :return:
    """
    # If you want to start it in pycharm terminal, use this line:
    # visitors = pd.read_csv('../csv/survey_results_public.csv')

    # If you want to start it in the main terminal, use this line:
    visitors = pd.read_csv('csv/survey_results_public.csv')

    employment = visitors['Employment'].value_counts()
    type_of_emp = employment.index.tolist()
    number = employment.values.tolist()
    counts = pd.Series(number,
                       index=type_of_emp)

    explode = (0, 0, 0, 0.1, 0.1, 0.2, 0.3, 0.4, 0.6)
    colors = ['#191970', '#001CF0', '#0038E2', '#0055D4', '#0071C6', '#008DB8', '#00AAAA',
              '#00C69C', '#00E28E', '#00FF80', '#00FF80']

    counts.plot(kind='pie', fontsize=8, colors=colors, explode=explode, figsize=(15,8), autopct='%1.2f%%')
    plt.axis('equal')
    plt.ylabel('')
    plt.legend(labels=counts.index, loc="best")
    plt.title("The percentage of developers who are visiting Stackoverflow")
    plt.show()


if __name__ == '__main__':  # pragma: no cover
    developers_on_stackoverflow()

