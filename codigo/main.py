from codigo.bytebank import Employer


# lucas = Employer("Lucas Carvalho", "13/03/2000", 1000)
# print(lucas.idade())

def test_age():

    employer_test = Employer("Test", '13/03/2000', 1111)
    print(f"Test = {employer_test.age()}")


test_age()
