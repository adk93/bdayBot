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
