# Standard library imports
import os
import datetime
import time
from typing import List
import logging

# Third party  imports
from dotenv import load_dotenv

# Local app imports
import msg_generator
import slack_client
import birthday_calendar

load_dotenv()

SRC_SPREADSHEET_ID = os.getenv("src_spreadsheet_id")
SHEET_NAME = os.getenv("sheet_name")
RANGE = os.getenv("range")
NAME_COL_NUMBER = os.getenv("name_col_number")
BIRTHDATE_COL_NUMBER = os.getenv("birthdate_col_number")
SLACK_CHANNEL_NAME = os.getenv("slack_channel_name")


def get_list_of_birthdays(sheet_name: str, range: str) -> List[List[str]]:
    sheet = birthday_calendar.Gsheets(SRC_SPREADSHEET_ID)
    list_of_employees = sheet.get_data_from_sheet(sheet_name, range)

    list_of_birthdays = []
    if list_of_employees[0][int(BIRTHDATE_COL_NUMBER)] == "Date of birth":
        for employee in list_of_employees:
            try:
                list_of_birthdays.append([employee[int(NAME_COL_NUMBER)], employee[int(BIRTHDATE_COL_NUMBER)]])
            except IndexError as e:
                logging.debug(e)

    return list_of_birthdays


def get_today_birthdays(list_of_birthdays: [[str, str, str]]) -> [[str, str, str]]:
    today = datetime.date.today().strftime("%Y-%m-%d")
    logging.debug(today)
    return list(filter(lambda x: x[1][4:] == today[4:], list_of_birthdays))


def get_birthday_wishes() -> str:
    return msg_generator.get_bday_wishes()


def process_birthday_wishes(birthday_user: str, birthday_wishes: str, placeholder: str = "@jan.kowalski"):
    return birthday_wishes.replace(placeholder, birthday_user)


def main():
    list_of_birthdays = get_list_of_birthdays(SHEET_NAME, RANGE)
    logging.debug(list_of_birthdays)

    today_birthdays = get_today_birthdays(list_of_birthdays)
    logging.debug(today_birthdays)

    for today_birthday in today_birthdays:
        user = today_birthday[0]
        logging.debug(f"User Birthday {user}")

        birthday_wishes = get_birthday_wishes()

        processed_wishes = process_birthday_wishes(user, birthday_wishes)

        slack_client.post_message(SLACK_CHANNEL_NAME, processed_wishes)

        time.sleep(5)


if __name__ == "__main__":
    main()
