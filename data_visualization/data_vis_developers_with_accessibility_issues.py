import pandas as pd
import matplotlib.pyplot as plt

def devs_with_accessibility_issues():  # pragma: no cover
    final_data =[]
    types_of_issues =['Having difficulty Seeing / Hearing / Walking / Standing without assistance', 'Do not have issues or prefer not to say']

    # If you want to start it in pycharm terminal, use this line:
    # visitors = pd.read_csv('../csv/survey_results_public.csv')

    # If you want to start it in the main terminal, use this line:
    visitors = pd.read_csv('csv/survey_results_public.csv')

    accessibility_total = len(visitors) - visitors['Accessibility'].value_counts()['None of the above'] - visitors['Accessibility'].value_counts()['Prefer not to say']
    other_total = visitors['Accessibility'].value_counts()['None of the above'] + visitors['Accessibility'].value_counts()['Prefer not to say']
    final_data.append(accessibility_total)
    final_data.append(other_total)
    plt.rcParams["figure.figsize"] = [8, 6]
    plt.rcParams.update({'font.size': 6})
    plt.bar(types_of_issues,final_data)
    plt.title("The number of developers who are having issues and who are not")
    plt.show()


if __name__ == "__main__":  # pragma: no cover
    devs_with_accessibility_issues()
