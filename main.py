from functions.newest_questions import get_recent_questions
from functions.no_accepted_answers import get_questions_with_no_accepted_answers
from functions.new_duplicate_question import new_duplicate_question


def main():
    print("""
    **********************************************
    ***** Welcome to Stack Overflow scrapper *****
    **********************************************
    *** You will be asked now to enter a couple***
    ** of parameters, so we get the data needed **
    ********************************************** 
    """)
    print("Enter a tag name: \n(ex: python, javascript, c#, etc...)")
    tag_user_input = input("> ")
    print("Enter one of the following filters: \nNewest (n), No answers (na)")
    no_answers_filter_user_input = input("> ")
    print("Enter the number of questions to return: \n(max is 50 questions)")
    questions_number_user_input = input("> ")

    if no_answers_filter_user_input.lower() == "newest" or no_answers_filter_user_input.lower() == "n":
        data = get_recent_questions(tag_user_input, int(questions_number_user_input))
        for i in data:
            # print(new_duplicate_question(i))
            if new_duplicate_question(i) is not None:
                data_with_dup = new_duplicate_question(i)
                i["originalData"] = {"Title": data_with_dup["Title"], "Link": data_with_dup["Link"]}

        print(data)


if __name__ == "__main__":
    main()
