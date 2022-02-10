from typing import List

class employee:

    def __init__(self, firstname: str, lastname: str, salary: int):
        self.firstname = firstname
        self.lastname = lastname
        self.salary = salary
        self.email =  self.firstname + '.' + self.lastname + '@rict.com'

    def giveRaise(self, salary: int) -> None:

        self.salary = salary

class developer(employee):

    def __init__(
            self,
            firstname: str,
            lastname: str,
            salary: int,
            programming_languages: List[str]):
        super().__init__(firstname, lastname, salary)
        self.prog_langs = programming_languages

    def addLanguage(self, lang: str) -> None:
        self.prog_langs.append(lang)

class PythonDeveloper(developer):

    def __init__(self, firstname: str, lastname: str, salary: int):
        super().__init__(firstname, lastname, salary, ['Python'])

employee1 = employee('Jon', 'Smith', 8000)

print(employee1.salary)

dev1 = developer('Joe', 'Montana', 10_000, ['Python', 'C'])

print(dev1.salary)

dev1.addLanguage('Java')

print(dev1.prog_langs)
