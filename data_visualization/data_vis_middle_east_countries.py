import pandas as pd
import matplotlib.pyplot as plt


def middle_east_countries_on_stackoverflow():  # pragma: no cover
    """
    This function is returning a graph with the number of developers who is visiting and interacting on stackoverflow
    from the middle east countries
    :return:
    """
    countries_names = ['Egypt', 'United Arab Emirates', 'Tunisia', 'Saudi Arabia', 'Lebanon', 'Iraq', 'Jordan',
                         'Qatar',
                         'Kuwait',
                         'Bahrain',
                         'Sudan',
                         'Palestine',
                         'Yemen',
                         'Oman',
                         'Libyan Arab Jamahiriya']
    developers_numbers =[]

    # If you want to start it in pycharm terminal, use this line:
    # visitors = pd.read_csv('../csv/survey_results_public.csv')

    # If you want to start it in the main terminal, use this line:
    visitors = pd.read_csv('csv/survey_results_public.csv')

    countries = visitors['Country'].value_counts()
    for i in range(len(countries_names)):
        developers_numbers.append(countries[countries_names[i]])
    plt.rcParams["figure.figsize"] = [20.00, 6]
    plt.rcParams.update({'font.size': 6})
    plt.bar(countries_names, developers_numbers)
    plt.title("The numbers of developers from the Middle East countries using Stackoverflow")
    plt.show()


if __name__ == '__main__':  # pragma: no cover
    middle_east_countries_on_stackoverflow()
