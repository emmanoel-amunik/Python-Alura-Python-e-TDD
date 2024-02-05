import pytest
from codigo.bytebank import Employer
from pytest import mark


class TestClass:

    @staticmethod
    def test_when_age_is_13_03_2000_must_return_24():
        # Given
        employer_birth_date_input = "12/03/2000"
        expected = 24

        # When
        employer_test = Employer("Teste", employer_birth_date_input, 1111)
        result = employer_test.age()

        # Then
        assert result == expected

    @staticmethod
    def test_when_last_name_is_lucas_carvalho_return_carvalho():

        employer_name_input = " Lucas Carvalho "
        expected = "Carvalho"

        employer_test = Employer(employer_name_input, "11/11/2000", 1111)
        result = employer_test.last_name()

        assert result == expected

    @mark.skip
    def test_when_salary_is_100k_decrease_10percent(self):

        employer_name_input = "Paulo Bragança"
        employer_salary_input = 100000
        expected = 90000

        employer_test = Employer(employer_name_input, "11/11/2000",
                                 employer_salary_input)
        result = employer_test.salary_decrease()

        assert result == expected

    @mark.calculate_bonus
    def test_when_bonus_calculate_is_1000_return_100(self):

        employer_salary_input = 1000
        expected = 100

        employer_test = Employer("Test", "11/11/2000", employer_salary_input)
        result = employer_test.calculate_bonus()

        assert result == expected

    @mark.calculate_bonus
    def test_when_calculate_bonus_receive_1kk_return_exception(self):

        with pytest.raises(Exception):

            employer_salary_input = 100000000
            # expected = None

            employer_test = Employer("Test", "11/12/2000",
                                     employer_salary_input)
            result = employer_test.calculate_bonus()

            assert result
