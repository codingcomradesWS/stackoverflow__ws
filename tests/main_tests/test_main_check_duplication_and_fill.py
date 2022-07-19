import pytest
from main import check_duplication_and_fill


def test_that_original_question_details_are_returned(duplication_data_directed_case,
                                                     duplication_data_undirected_case,
                                                     non_duplicate_data):
    assert duplication_data_directed_case["originalData"]["Title"] is not None
    assert duplication_data_directed_case["originalData"]["Link"] is not None
    assert duplication_data_directed_case["originalData"]["Link"] == \
           "https://stackoverflow.com/questions/8312459/iterate-through-object-properties"

    assert duplication_data_undirected_case["originalData"]["Title"] is not None
    assert duplication_data_undirected_case["originalData"]["Link"] is not None
    assert duplication_data_undirected_case["originalData"]["Link"] == \
           "https://stackoverflow.com/questions/7961363/removing-duplicates-in-lists"

    assert check_duplication_and_fill(non_duplicate_data) is None


def test_retuning_data_type(duplication_data_directed_case, duplication_data_undirected_case):
    assert type(duplication_data_directed_case["originalData"]) == type({})
    assert type(duplication_data_undirected_case["originalData"]) == type({})


@pytest.fixture
def duplication_data_directed_case():
    duplication_data_directed_case = \
        {"Title": "Is grid something defined on the JavaScript language? [duplicate]",
         "Link": "https://stackoverflow.com/questions/8312459/iterate-through-object-properties"}
    check_duplication_and_fill(duplication_data_directed_case)
    return duplication_data_directed_case


@pytest.fixture
def duplication_data_undirected_case():
    duplication_data_undirected_case = \
        {"Title": "What is wrong with my code of deleting duplicates from a list? [duplicate]",
         "Link": "https://stackoverflow.com/questions/72906092/what-is-wrong-with-my-code-of-deleting-duplicates-from-a-list"}
    check_duplication_and_fill(duplication_data_undirected_case)
    return duplication_data_undirected_case


@pytest.fixture
def non_duplicate_data():
    non_duplicate_data = \
        {"Title": "Efficient reuse of previous hashmap entries (insert or modify if key exists)",
         "Link": "https://stackoverflow.com/questions/72904866/efficient-reuse-of-previous-hashmap-entries-insert-or-modify-if-key-exists"}
    return non_duplicate_data
