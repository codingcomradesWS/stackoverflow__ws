import pandas as pd


def annual_salary_calculator():
    """
    this function will calculate the  Median Annual Compensation for the top 10 countries in programming
    :param:None
    :return: 2D list with the top 10 countries and their median annual compensation
    """
    countries_list = ['Germany', 'India', 'France', 'United States of America', 'China', "Taiwan", "Russian Federation",
                      'Poland', "Canada", "Brazil"]
    currency_list = ['EUR European Euro', 'INR	Indian rupee', 'EUR European Euro', 'USD	United States dollar',
                     'CNY	Chinese Yuan Renminbi', "USD	United States dollar", 'RUB	Russian ruble',
                     'PLN	Polish zloty', 'CAD	Canadian dollar', "BRL	Brazilian real"]
    exchange_list = [1.023, 0.012, 1.023, 1, 0.148, 1, 0.018, 0.22, 0.77, 0.18]
    annual_salary_list = []
    df = pd.read_csv('../csv/survey_results_public.csv')

    for i in range(len(countries_list)):
        data_yearly = df.loc[
            (df['Country'] == f"{countries_list[i]}") & (df['CompTotal'].notnull()) & (df['CompFreq'] == "Yearly") & (
                    df['Currency'] == f'{currency_list[i]}')]
        data_monthly = df.loc[
            (df['Country'] == f"{countries_list[i]}") & (df['CompTotal'].notnull()) & (df['CompFreq'] == "Monthly") & (
                    df['Currency'] == f'{currency_list[i]}')]
        comp_yearly = data_yearly["CompTotal"].median()
        comp_monthly = data_monthly["CompTotal"].median()
        annual_salary = (comp_yearly + comp_monthly * 12) / 2
        # print(f'annual_salary for {countries_list[i]} is {int(annual_salary * exchange_list[i])} $')
        annual_salary_list.append(int(annual_salary * exchange_list[i]))
    return [countries_list, annual_salary_list]

# if __name__ == "__main__":
#     print(annual_salary_calculator())

