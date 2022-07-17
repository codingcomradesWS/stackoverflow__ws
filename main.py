from functions.newest_questions import get_recent_questions
from functions.no_answers import get_questions_with_no_accepted_answers
from functions.new_duplicate_question import new_duplicate_question


def check_duplication_and_fill(data):
    if new_duplicate_question(data) is not None:
        data_with_dup = new_duplicate_question(data)
        data["originalData"] = {"Title": data_with_dup["Title"], "Link": data_with_dup["Link"]}
    else:
        return


class AppManager:

    def __init__(self):
        self.is_on = False
        self.tag_user_input = ""
        self.no_answers_filter_user_input = ""
        self.questions_number_user_input = ""

    def _continue_process(self):
        print("\nContinue? (y / any others key)")
        start_input = input("> ")

        if start_input.lower() == "y":
            self.is_on = True
        else:
            self.is_on = False

    def _input_options(self):
        print("Enter a tag name: \n(ex: python, javascript, c#, etc...)")
        self.tag_user_input = input("> ")
        print("Enter one of the following filters: \nNewest (n), No answers (na)")
        self.no_answers_filter_user_input = input("> ")
        print("Enter the number of questions to return: \n(max is 50 questions)")
        self.questions_number_user_input = input("> ")

    def _get_filter_again(self):
        print("Enter one of the following filters: \nNewest (n), No answers (na)")
        self.no_answers_filter_user_input = input("> ")

    def start(self):
        print("""
        **********************************************
        ***** Welcome to Stack Overflow scrapper *****
        **********************************************
        ** You will be asked now to enter a couple  **
        ** of parameters, so we get the data needed **
        ********************************************** 
        """)
        self._continue_process()

        while self.is_on is True:
            self._input_options()
            if self.no_answers_filter_user_input.lower() == "newest" or self.no_answers_filter_user_input.lower() == "n":
                data = get_recent_questions(self.tag_user_input, int(self.questions_number_user_input))
                for i in data:
                    check_duplication_and_fill(i)

                print(data)

            elif self.no_answers_filter_user_input.lower() == "no answers" or self.no_answers_filter_user_input.lower() == "na":
                data = get_questions_with_no_accepted_answers(self.tag_user_input,
                                                              int(self.questions_number_user_input))
                for i in data:
                    check_duplication_and_fill(i)

                print(data)

            else:
                print("Only the above filtering options are allowed, please try again")
                self._get_filter_again()
                continue

            self._continue_process()

        print("\nOk, call upon me when I'm needed")
        return


if __name__ == "__main__":
    app = AppManager()
    app.start()
