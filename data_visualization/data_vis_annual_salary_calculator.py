import pandas as pd
import matplotlib.pyplot as plt
from functions.annual_salary_calculator import annual_salary_calculator


def data_vis_annual_salary_calculator():  # pragma: no cover
    """
    This function is used to visualize the data from the annual_salary_calculator function
    :param: None
    :return: None
    """
    annual_salary_caller = annual_salary_calculator()
    df = pd.DataFrame({'countries': annual_salary_caller[0],
                       'comp': annual_salary_caller[1]})
    plt.figure(figsize=(9, 6))
    ax1 = plt.subplot(111)
    df.sort_values("comp", inplace=True)

    ret = ax1.barh(df.countries, df.comp, color="#99ccff")
    ret[5].set_color("#404040")
    ret[9].set_color("#CC0000")
    ax1.xaxis.grid(linestyle='--', linewidth=0.2)
    for pY, pX in enumerate(df.comp):
        ax1.annotate("{:,}".format(pX) + "$", xy=(pX, pY), fontstyle="italic", va="center")
    ax1.set_xlim(0, df.comp.max() * 1.2)
    plt.title("Median Annual Compensation")
    plt.show()


# if __name__ == "__main__":
#     data_vis_annual_salary_calculator()
