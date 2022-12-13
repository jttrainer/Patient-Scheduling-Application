from datetime import datetime


class Patient:
    def __init__(self, first_name: str, last_name: str, dob: datetime, sex: str, phone: str = "none",
                 email: str = "none"):
        self._first_name = first_name.upper()
        self._last_name = last_name.upper()
        self._dob = dob
        self._sex = sex.upper()
        self._phone = phone
        self._email = email.lower()

    def __str__(self):
        return f"{self._last_name}, {self._first_name}"

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, first_name: str):
        self._first_name = first_name

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, last_name: str):
        self._last_name = last_name

    @property
    def dob(self):
        return f"{self._dob.month}/{self._dob.day}/{self._dob.year}"

    @dob.setter
    def dob(self, dob: datetime):
        self._dob = dob

    @property
    def sex(self):
        return self._sex

    @sex.setter
    def sex(self, sex: str):
        self._sex = sex

    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, phone: str):
        self._phone = phone

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email: str):
        self._email = email

