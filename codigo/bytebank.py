from datetime import date


class Employer:

    def __init__(self, name, birth_date, wage):
        self._name = name
        self._birth_date = birth_date
        self._wage = wage

    @property
    def name(self):
        return self._name

    def last_name(self):

        full_name = self._name.strip()
        broken_name = full_name.split(' ')

        return broken_name[-1]

    @property
    def wage(self):
        return self._wage

    def age(self):

        birth_date_broken = self._birth_date.split('/')
        birth_year = birth_date_broken[-1]
        current_year = date.today().year

        return current_year - int(birth_year)

    def calculate_bonus(self):

        value = self._wage * 0.1
        if value > 1000:
            value = 0

        return value

    def __str__(self):
        return f'Employer({self._name}, {self._birth_date}, {self._wage})'
