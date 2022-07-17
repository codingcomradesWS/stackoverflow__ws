from functions.newest_questions import get_recent_questions
from functions.no_answers import get_questions_with_no_answers
from functions.new_duplicate_question import new_duplicate_question
from functions.stack_api import get_search_results
from functions.most_frequent_answers import get_frequent
from pick import pick
from colorama import Fore, Back, Style
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


class AppManager:

    def __init__(self):
        # self.is_on = True
        self.option = ""
        self.text_user_input = ""
        self.tag_user_input = ""
        self.filter_user_input = ""
        self.questions_number_user_input = ""

    def _continue_process(self):
        """
        This function goes through the main program options, or quiting.
        :return: Nothing
        """
        title = 'Please choose the preferred action: '
        options = ['Search by tag', 'Search by text', "Quit"]

        option = pick(options, title, indicator='=>', default_index=0)
        self.option = option[0]
        print(f"{Fore.LIGHTGREEN_EX}\nAction: {Fore.LIGHTYELLOW_EX}{self.option[0]}\n")

    def _input_options(self):
        print(f"{Fore.LIGHTGREEN_EX}Enter a tag name: \n(ex: python, javascript, c#, etc...)\n")
        self.tag_user_input = input("> ")

        if self.option[0] == "Search by tag":
            self._get_filter()

        if self.option[0] == "Search by text":
            print(f"\n{Fore.LIGHTGREEN_EX}Search for:\n")
            self.tag_user_input = input("> ")

        print(f"\n{Fore.LIGHTGREEN_EX}Enter the number of questions to return: \n(max is 50 questions)\n")
        self.questions_number_user_input = input("> ")

    def _get_filter(self):
        title = 'Please choose the preferred filter: '
        options = ["Newest questions", "Questions without answers", "Most frequent questions"]

        option = pick(options, title, indicator='=>', default_index=0)

        self.filter_user_input = option[0]
        print(f"{Fore.LIGHTGREEN_EX}\nAction: {Fore.LIGHTYELLOW_EX}{self.filter_user_input[0]}\n")

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
        input(f"\nPress Enter to continue...")
        self._continue_process()

        while True:
            if self.option[0] == "Quit":
                break

            self._input_options()

            if self.option[0] == "Search by tag":
                if self.filter_user_input[0] == "Newest questions":
                    data = get_recent_questions(self.tag_user_input, int(self.questions_number_user_input))
                    for i in data:
                        print(f"{Fore.LIGHTGREEN_EX}----------------------------")
                        check_duplication_and_fill(i)
                        print(Fore.LIGHTBLUE_EX + link(i["Link"], i["Title"]))
                        if "originalData" in i:
                            print(f"{Fore.LIGHTGREEN_EX}This question is a duplicate, original link:"
                                  f"\n{Fore.LIGHTBLUE_EX}{link(i['originalData']['Link'], i['originalData']['Title'])}\n")
                    input("Press Enter to continue...")

                elif self.filter_user_input[0] == "Questions without answers":
                    data = get_questions_with_no_answers(self.tag_user_input, int(self.questions_number_user_input))
                    for i in data:
                        print(f"{Fore.LIGHTGREEN_EX}----------------------------")
                        check_duplication_and_fill(i)
                        print(Fore.LIGHTBLUE_EX + link(i["Link"], i["Title"]))
                        if "originalData" in i:
                            print(f"{Fore.LIGHTGREEN_EX}This question is a duplicate, original link:"
                                  f"\n{Fore.LIGHTBLUE_EX}{link(i['originalData']['Link'], i['originalData']['Title'])}\n")
                    # print(json.dumps(data, indent=4))
                    input("Press Enter to continue...")

                elif self.filter_user_input[0] == "Most frequent questions":
                    data = get_frequent(self.tag_user_input, int(self.questions_number_user_input))
                    for i in data:
                        print(f"{Fore.LIGHTGREEN_EX}----------------------------")
                        check_duplication_and_fill(i)
                        print(Fore.LIGHTBLUE_EX + link(i["Link"], i["Title"]))
                        if "originalData" in i:
                            print(f"{Fore.LIGHTGREEN_EX}This question is a duplicate, original link:"
                                  f"\n{Fore.LIGHTBLUE_EX}{link(i['originalData']['Link'], i['originalData']['Title'])}\n")
                    # print(json.dumps(data, indent=4))
                    input("Press Enter to continue...")

            if self.option[0] == "Search by text":
                data = get_search_results(self.text_user_input, self.tag_user_input, self.questions_number_user_input)

                for i in data:
                    print(f"\n{Fore.LIGHTGREEN_EX}----------------------------\n")
                    check_duplication_and_fill(i)
                    print(Fore.LIGHTBLUE_EX + link(i["Link"], i["Title"]))
                input("Press Enter to continue...")

            self._continue_process()

        print("\nOk, call upon me when I'm needed")
        return


if __name__ == "__main__":
    app = AppManager()
    app.start()
