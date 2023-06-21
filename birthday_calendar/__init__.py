from datetime import datetime
import ast
import os
from typing import List

# Third party imports
import gspread
from dotenv import load_dotenv


load_dotenv()
CREDENTIALS = ast.literal_eval(os.getenv("service_account_json"))


class Gsheets:
    """Connects to a google spreadsheet, reads and writes data"""
    def __init__(self, spreadsheet_id: str):
        self.spreadsheet_id = spreadsheet_id
        self.client = self.authenticate_gsheets()

    def authenticate_gsheets(self) -> gspread.client:
        scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
                 "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

        return gspread.service_account_from_dict(CREDENTIALS)

    def get_data_from_sheet(self, sheet_name: str, range: str = None) -> List[List]:
        """Grabs data from a specified sheet. Uses given range. If range is not given returns all data in a sheet"""
        sheet = self.client.open_by_key(self.spreadsheet_id).worksheet(sheet_name)
        data = sheet.get_all_values() if range is None else sheet.get(range)
        return data