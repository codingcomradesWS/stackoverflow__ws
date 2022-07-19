from functions.most_active_community import most_active_community
import matplotlib.pyplot as plt


def data_vis_most_active_community():
    """
    this function will plot a pie chart for the top 5 weekly active communities in stack overflow
    :param:
    :return:
    """
    top_10_data = []
    labels = []
    data = most_active_community()
    total = 0
    for i in range(5):
        total += data[i]['max_weekly']

    for i in range(5):
        top_10_data.append(data[i]['max_weekly'] / total)
        labels.append(data[i]['community'])
    plt.pie(top_10_data, labels=labels, autopct='%2.1f%%', explode=[0, 0.1, 0, 0, 0], shadow=True)
    plt.axis('equal')
    plt.legend(loc="upper left")
    plt.title("Top 5 weekly active communities")
    plt.show()


# if __name__ == '__main__':
#     data_vis_most_active_community()
