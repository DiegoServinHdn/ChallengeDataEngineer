import pytest
from src.main import connect, number_of_answers, answer_with_less_views, oldest_and_latest_answers, owner_with_best_reputation

CONNECTION_URL = "https://api.stackexchange.com/2.2/search?order=desc&sort=activity&intitle=perl&site=stackoverflow"


class TestConnect(object):
    def test_connection_status(self):
        expected_status = 200
        actual_status = connect(CONNECTION_URL).status_code
        assert actual_status == expected_status, f"Connection status to {CONNECTION_URL} is not 200\nconnection status: {actual_status}"


    def test_connection_json(self):
        expected_type = dict
        actual_type = type(connect(CONNECTION_URL).json())
        assert expected_type == actual_type, "Data isn't a dictionary"
    

class TestNumberOfAnswers(object):
    def test_answers_keys(self):
        test_data = {'items': [
            {'is_answered': True},
            {'is_answered': False},
            {'is_answered': True},
            ]}
        expected_keys = ['answered', 'not answered']
        actual_keys = list(number_of_answers(test_data).keys())
        assert expected_keys == actual_keys, f"Expected keys: {expected_keys} don't match with actual keys: {actual_keys}"

    def test_with_two_answered_two_not_answered(self):
        test_data = {'items': [
            {'is_answered': True},
            {'is_answered': False},
            {'is_answered': True},
            {'is_answered': False},
            ]}
        expected_number_of_answers = {'answered': 2, 'not answered': 2}
        actual_number_of_answers = number_of_answers(test_data)
        assert expected_number_of_answers == actual_number_of_answers, f"Expected number of answer: {number_of_answers} \
         don't match with actual number of answers: {actual_number_of_answers}"

    def test_without_is_answered_key(self):
        test_data = {'items': [
            {'is_answered': True},
            {'is_answered': False},
            {'is_answered': True},
            {},
            ]}
        expected_number_of_answers = {'answered': 2, 'not answered': 1}
        actual_number_of_answers = number_of_answers(test_data)
        assert expected_number_of_answers == actual_number_of_answers


class TestAnswerWithLessViews(object):
    def test_with_ordered_view_count(self):
        test_data = {'items': [
            {'view_count': 1},
            {'view_count': 2},
            {'view_count': 3},
            {'view_count': 4}
        ]}

        expected_value = {'view_count': 1}
        actual_value = answer_with_less_views(test_data)
        assert expected_value == actual_value

    def test_with_unordered_view_count(self):
        test_data = {'items': [
            {'view_count': 3},
            {'view_count': 2},
            {'view_count': 1},
            {'view_count': 4}
        ]}

        expected_value = {'view_count': 1}
        actual_value = answer_with_less_views(test_data)
        assert expected_value == actual_value

    def test_with_two_less_view_count(self):
        test_data = {'items': [
            {'view_count': 3},
            {'view_count': 1},
            {'view_count': 1},
            {'view_count': 4}
        ]}

        expected_value = {'view_count': 1}
        actual_value = answer_with_less_views(test_data)
        assert expected_value == actual_value

    def test_without_view_count_key(self):
        test_data = {'items': [
            {'view_count': 3},
            {},
            {'view_count': 1},
            {'view_count': 4}
        ]}

        expected_value = {'view_count': 1}
        actual_value = answer_with_less_views(test_data)
        assert expected_value == actual_value


class TestOldestAndLatestAnswers(object):
    def test_with_ordered_creation_date(self):
        test_data = {'items': [
            {'creation_date': 1},
            {'creation_date': 3},
            {'creation_date': 4},
            {'creation_date': 6}
        ]}

        expected_value = {
            'oldest': {'creation_date': 1},
            'latest': {'creation_date': 6}
            }

        actual_value = oldest_and_latest_answers(test_data)
        assert expected_value == actual_value

    def test_with_unordered_creation_date(self):
        test_data = {'items': [
            {'creation_date': 3},
            {'creation_date': 6},
            {'creation_date': 1},
            {'creation_date': 4}
        ]}

        expected_value = {
            'oldest': {'creation_date': 1},
            'latest': {'creation_date': 6}
        }

        actual_value = oldest_and_latest_answers(test_data)
        assert expected_value == actual_value

    def test_without_creation_date_key(self):
        test_data = {'items': [
            {'creation_date': 3},
            {'creation_date': 6},
            {},
            {'creation_date': 4}
        ]}

        expected_value = {
            'oldest': {'creation_date': 3},
            'latest': {'creation_date': 6}
        }

        actual_value = oldest_and_latest_answers(test_data)
        assert expected_value == actual_value

class TestOwnerWithBestReputation(object):
    def test_with_ordered_reputation(self):
        test_data = {'items': [
            {'owner': 
                {
                    'reputation': 2
                }
            },
            {'owner': 
                {
                    'reputation': 10
                }
            },
            {'owner': 
                {
                    'reputation': 20
                }
            },
            {'owner': 
                {
                    'reputation': 30
                }
            },
        ]}

        expected_value = {'owner': {'reputation': 30}}

        actual_value = owner_with_best_reputation(test_data)
        assert expected_value == actual_value

    def test_with_unordered_reputation(self):
        test_data = {'items': [
            {'owner': 
                {
                    'reputation': 59
                }
            },
            {'owner': 
                {
                    'reputation': 70
                }
            },
            {'owner': 
                {
                    'reputation': 20
                }
            },
            {'owner': 
                {
                    'reputation': 30
                }
            },
        ]}

        expected_value = {'owner': {'reputation': 70}}
        
        actual_value = owner_with_best_reputation(test_data)
        assert expected_value == actual_value

    def test_without_owner_key(self):
        test_data = {'items': [
            {'owner': 
                {
                    'reputation': 2
                }
            },
            {
            },
            {'owner': 
                {
                    'reputation': 20
                }
            },
            {'owner': 
                {
                    'reputation': 10
                }
            },
        ]}

        expected_value = {'owner': {'reputation': 20}}
        
        actual_value = owner_with_best_reputation(test_data)
        assert expected_value == actual_value






    

