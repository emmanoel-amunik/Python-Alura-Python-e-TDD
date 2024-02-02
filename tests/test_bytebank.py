from codigo.bytebank import Employer


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

    def test_when_salary_is_100k_decrease_10percent(self):

        employer_name_input = "Paulo Bragança"
        employer_salary_input = 100000
        expected = 90000

        employer_test = Employer(employer_name_input, 11/11/2000,
                                 employer_salary_input)
        result = employer_test.salary_decrease()

        assert result == expected
