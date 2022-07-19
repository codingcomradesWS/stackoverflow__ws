import data_visualization.data_vis_developers_on_stackoverflow
from functions.newest_questions import get_recent_questions
from functions.no_answers import get_questions_with_no_answers
from functions.new_duplicate_question import new_duplicate_question
from functions.stack_api import *
from functions.most_frequent_answers import get_frequent
from functions.best_companies_hiring import get_best_companies_hiring
from data_visualization import (data_vis_unanswered_percentage,
                                data_vis_most_active_community,
                                data_vis_developers_on_stackoverflow,
                                data_vis_middle_east_countries,
                                data_vis_developers_with_accessibility_issues)
from pick import pick
from colorama import Fore, Back, Style
from halo import Halo
import json
import colorama


def check_duplication_and_fill(data):
    """
    This function checks if the question is a duplicat of another, and gets the title and link of the original
    :param data: dictionary
    :return: dictionary value
    """
    if new_duplicate_question(data) is not None:
        data_with_dup = new_duplicate_question(data)
        data["originalData"] = {"Title": data_with_dup["Title"], "Link": data_with_dup["Link"]}
    else:
        return


def link(uri, label=None):
    """
    This function gives a creates a hyperlink with a label.
    :param uri: the link
    :param label: label string
    :return: string that is a hyperlink
    """
    if label is None:
        label = uri
    parameters = ''

    # OSC 8 ; params ; URI ST <name> OSC 8 ;; ST
    escape_mask = '\033]8;{};{}\033\\{}\033]8;;\033\\'

    return escape_mask.format(parameters, uri, label)


def get_continue_message():  # pragma: no cover
    spinner = Halo(text='Press Enter to continue...', spinner='dots', color="grey")
    spinner.start()
    input()
    spinner.stop()
    print("\033[A                             \033[A")


def print_formatted_results(data, input_filter=None):  # pragma: no cover
    for i in data:
        print(f"{Fore.LIGHTGREEN_EX}----------------------------")

        print()
        spinner = Halo(text="Getting Data...", text_color="green", spinner='dots', color="grey")
        spinner.start()
        check_duplication_and_fill(i)
        spinner.stop()
        print(f"{Fore.LIGHTGREEN_EX}\033[A                             \033[A")

        print(f"\n{Fore.GREEN}Title: {Fore.LIGHTBLUE_EX + link(i['Link'], i['Title'])}")

        if input_filter == "Newest questions":
            print(f"{Fore.GREEN}Time: {Fore.LIGHTGREEN_EX + i['Date&Time']}\n")

        if input_filter == "Questions without answers":
            print(f"{Fore.GREEN}Number of answers: {Fore.LIGHTGREEN_EX + i['NumberOfAnswers']}\n")

        if input_filter == "Most voted questions":
            print(f"{Fore.GREEN}Number of votes: {Fore.LIGHTGREEN_EX + str(i['Votes'])}\n")

        if "originalData" in i:
            print(f"{Fore.GREEN}This question is a duplicate of:"
                  f"\n{Fore.GREEN}Original: {Fore.LIGHTBLUE_EX}{link(i['originalData']['Link'], i['originalData']['Title'])}\n")
    # print(json.dumps(data, indent=4))
    print(f"{Fore.LIGHTGREEN_EX}----------------------------\n")
    get_continue_message()


class AppManager:  # pragma: no cover

    def __init__(self):
        # self.is_on = True
        self.option = ""
        self.text_user_input = ""
        self.tag_user_input = ""
        self.filter_user_input = ""
        self.questions_number_user_input = ""
        self.chart_input_option = 0
        # Options to choose from
        self.chart_select_options = ["Percentage of unanswered questions for popular tags",
                                     "Community activity on Stack overflow",
                                     "Kinds of developers on Stack overflow",
                                     "Developers of Stack overflow in middle east countries",
                                     "Developers of Stack overflow with accessibility issues"]
        self.chart_option_to_show = [data_vis_unanswered_percentage.unanswered_questions_percentage_visualization,
                                     data_vis_most_active_community.data_vis_most_active_community,
                                     data_vis_developers_on_stackoverflow.developers_on_stackoverflow,
                                     data_vis_middle_east_countries.middle_east_countries_on_stackoverflow,
                                     data_vis_developers_with_accessibility_issues.devs_with_accessibility_issues]

    def _continue_process(self):
        """
        This function goes through the main program options, or quiting.
        :return: Nothing
        """
        title = 'Please choose the preferred action: '
        options = ['Search by tag', 'Search by text', "Access some interesting insights",
                   "Best hiring companies for a specific programming language",
                   "Quit"]

        option = pick(options, title, indicator='=>', default_index=0)
        self.option = option[0]
        print(f"{Fore.LIGHTGREEN_EX}\nAction: {Fore.LIGHTYELLOW_EX}{self.option[0]}\n")

    def _input_options(self):
        print(f"{Fore.LIGHTGREEN_EX}Enter a tag name: \n(ex: {Fore.LIGHTBLUE_EX}"
              f"python, javascript, c#, etc...{Fore.LIGHTGREEN_EX})\n")
        self.tag_user_input = input("> ")

        if self.option[0] == "Search by tag":
            self._get_filter()
            self._get_requested_number()

        if self.option[0] == "Search by text":
            print(f"\n{Fore.LIGHTGREEN_EX}Search for:\n")
            self.tag_user_input = input("> ")
            self._get_requested_number()

    def _get_filter(self):
        title = 'Please choose the preferred filter: '
        options = ["Newest questions", "Questions without answers", "Most frequent questions", "Most voted questions"]

        option = pick(options, title, indicator='=>', default_index=0)

        self.filter_user_input = option[0]
        print(f"{Fore.LIGHTGREEN_EX}\nAction: {Fore.LIGHTYELLOW_EX}{self.filter_user_input[0]}\n")

    def _get_requested_number(self):
        print(f"\n{Fore.LIGHTGREEN_EX}Enter the number of questions to return: \n({Fore.LIGHTBLUE_EX}"
              f"max is {Fore.LIGHTYELLOW_EX}50 {Fore.LIGHTBLUE_EX}questions{Fore.LIGHTGREEN_EX})\n")
        self.questions_number_user_input = input("> ")

    def _get_chart_input(self):
        title = 'Please choose the preferred action: '

        option = pick(self.chart_select_options, title, indicator='=>', default_index=0)
        self.chart_input_option = option[0][1]
        print(f"{Fore.LIGHTGREEN_EX}\nAction: {Fore.LIGHTYELLOW_EX}{option[0][0]}\n")

    def _get_chart_render(self):
        spinner = Halo(text="Getting Data...", text_color="green", spinner='dots', color="grey")
        spinner.start()
        self.chart_option_to_show[self.chart_input_option]()
        spinner.stop()
        print(f"{Fore.LIGHTGREEN_EX}\033[A                             \033[A")
        get_continue_message()

    def start(self):
        colorama.init(autoreset=True)
        print(f"""
        {Fore.GREEN}**********************************************
        ***** {Fore.YELLOW}Welcome to Stack Overflow scrapper {Fore.GREEN}*****
        **********************************************
        ** {Fore.YELLOW}You will be asked now to enter a couple  {Fore.GREEN}**
        ** {Fore.YELLOW}of parameters, so we get the data needed {Fore.GREEN}**
        **********************************************
        """)
        get_continue_message()

        self._continue_process()

        while True:
            if self.option[0] == "Quit":
                break
            if self.option[0] == "Access some interesting insights":
                self._get_chart_input()
                self._get_chart_render()
            else:
                self._input_options()

            if self.option[0] == "Search by tag":
                if self.filter_user_input[0] == "Newest questions":
                    data = get_recent_questions(self.tag_user_input, int(self.questions_number_user_input))
                    print_formatted_results(data, self.filter_user_input[0])

                elif self.filter_user_input[0] == "Questions without answers":
                    data = get_questions_with_no_answers(self.tag_user_input, int(self.questions_number_user_input))
                    print_formatted_results(data, self.filter_user_input[0])

                elif self.filter_user_input[0] == "Most frequent questions":
                    data = get_frequent(self.tag_user_input, int(self.questions_number_user_input))
                    print_formatted_results(data)

                elif self.filter_user_input[0] == "Most voted questions":
                    data = get_most_voted_results(self.tag_user_input, self.questions_number_user_input)
                    print_formatted_results(data, self.filter_user_input[0])

            if self.option[0] == "Search by text":
                data = get_search_results(self.text_user_input, self.tag_user_input, int(self.questions_number_user_input))
                print_formatted_results(data)

            if self.option[0] == "Best hiring companies for a specific programming language":
                data = get_best_companies_hiring(self.tag_user_input)
                for i in data:
                    print(f"\n{Fore.LIGHTGREEN_EX}----------------------------\n")
                    print(Fore.LIGHTBLUE_EX + link(i["Link"], i["Title"]))
                get_continue_message()

            self._continue_process()

        print("\nOk, call upon me when I'm needed")
        return


if __name__ == "__main__":  # pragma: no cover
    app = AppManager()
    app.start()
