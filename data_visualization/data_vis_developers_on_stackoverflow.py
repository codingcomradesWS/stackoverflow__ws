import pandas as pd
import matplotlib.pyplot as plt


def developers_on_stackoverflow():  # pragma: no cover
    visitors = pd.read_csv('csv/survey_results_public.csv')
    employment = visitors['Employment'].value_counts()
    type_of_emp = employment.index.tolist()
    number = employment.values.tolist()
    fig = plt.figure(figsize=(10, 8))
    plt.pie(number, labels=type_of_emp, autopct='%1.2f%%')
    plt.show()


if __name__ == '__main__':  # pragma: no cover
    developers_on_stackoverflow()

