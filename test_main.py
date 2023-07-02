import pytest
import main


def test_get_today_birthdays(monkeypatch):

    def mock_get_today_date():
        return "2023-02-19"

    monkeypatch.setattr(main, "get_today_date", mock_get_today_date)

    employees = [
        ["Kamiński Adrian", "1993-02-19"],
        ["Messi Lionel", "1989-07-20"],
        ["Ronladingho Gaucho", "1983-10-12"],
        ["Peszko Sławomir", "1987-02-19"]
    ]

    assert main.get_today_birthdays(employees) == [["Kamiński Adrian", "1993-02-19"],
                                              ["Peszko Sławomir", "1987-02-19"]]


def test_get_list_of_birthdays(monkeypatch):

    def mock_get_list_of_employees(sheet_name, range):
        return [["ID", "Name", "agreement type", "start_date", "end_date", "status", "position", "based in", "email", "address", "Date of birth"],
                ["u-12345", "Adrian Kamiński", "B2B", "1831-01-01", "Nieokreślony", "NEW", "C++", "Remote", "adrian@adrian.com", "blabla", "2023-04-01"],
                ["u-12346", "Roman Giertych", "UoP", "2022-01-01", "2023-04-01", "NEW", "C++", "Remote", "adrian@adrian.com", "blabla", "1993-05-21"],
                ["u-12347", "Kazimierz Marcinkiewicz", "B2B", "1831-01-01", "Nieokreślony", "ACTIVE", "C++", "Remote", "adrian@adrian.com", "blabla", "1988-09-28"],
                ["u-12348", "Tadeusz Mazowiecki", "UoP", "1831-01-01", "Nieokreślony", "FORMER", "C++", "Remote", "adrian@adrian.com", "blabla", "1990-02-15"],
                ["u-12349", "Jerzy Buzek", "UoP", "1831-01-01", "Nieokreślony", "FORMER", "C++", "Remote", "adrian@adrian.com", "blabla", "1995-06-30"],
                ["u-12345", "Donald Tusk", "B2B", "1831-01-01", "Nieokreślony", "ACTIVE", "C++", "Remote", "adrian@adrian.com", "blabla", "1960-03-19"]]

    monkeypatch.setattr(main, "get_list_of_employees", mock_get_list_of_employees)

    assert main.get_list_of_birthdays("LIST OF EMPLOYEES", "A1:S") == [["ID", "Date of birth"],
                ["u-12345", "2023-04-01"],
                ["u-12346", "1993-05-21"],
                ["u-12347", "1988-09-28"],
                ["u-12345", "1960-03-19"]]


def test_get_list_of_birthdays_check_status(monkeypatch):

    def mock_get_list_of_employees(sheet_name, range):
        return [["ID", "Name", "agreement type", "start_date",  "status", "end_date","position", "based in", "email", "address", "Date of birth"],
                ["u-12345", "Adrian Kamiński", "B2B", "1831-01-01",  "NEW", "Nieokreślony","C++", "Remote", "adrian@adrian.com", "blabla", "2023-04-01"],
                ["u-12346", "Roman Giertych", "UoP", "2022-01-01",  "NEW", "2023-04-01", "C++", "Remote", "adrian@adrian.com", "blabla", "1993-05-21"],
                ["u-12347", "Kazimierz Marcinkiewicz", "B2B", "1831-01-01",  "ACTIVE", "Nieokreślony","C++", "Remote", "adrian@adrian.com", "blabla", "1988-09-28"],
                ["u-12348", "Tadeusz Mazowiecki", "UoP", "1831-01-01",  "FORMER", "Nieokreślony","C++", "Remote", "adrian@adrian.com", "blabla", "1990-02-15"],
                ["u-12349", "Jerzy Buzek", "UoP", "1831-01-01",  "FORMER", "Nieokreślony","C++", "Remote", "adrian@adrian.com", "blabla", "1995-06-30"],
                ["u-12345", "Donald Tusk", "B2B", "1831-01-01",  "ACTIVE","Nieokreślony", "C++", "Remote", "adrian@adrian.com", "blabla", "1960-03-19"]]

    def mock_inform_admin():
        print("admin informed")

    monkeypatch.setattr(main, "get_list_of_employees", mock_get_list_of_employees)
    monkeypatch.setattr(main, "inform_admin", mock_inform_admin)

    with pytest.raises(Exception):
        main.get_list_of_birthdays("LIST OF EMPLOYEES", "A1:S")



