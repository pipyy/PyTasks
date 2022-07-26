import gspread
import pandas as pd
import gspread as gs


GOOGLESHEET_ID = "11iCvHhbNJH2q6viSHgg4LlzAIqp4d564dBlBBEqJPzs"


# sheet = gc.open_by_key(GOOGLESHEET_ID)

class Sheetsconnector:

    def __init__(self, googlesheet_id):
        self.GOOGLESHEET_ID = googlesheet_id

    def open_googlesheet(self, worksheet_name):
        gc = gs.service_account(filename="gcloud-credentials.json")
        spreadsheet = gc.open_by_key(self.GOOGLESHEET_ID)
        worksheet = spreadsheet.worksheet(worksheet_name)
        return worksheet

    def read_worksheet_as_dataframe(self, worksheet_name):
        return pd.DataFrame.from_dict(self.open_googlesheet(worksheet_name).get_all_records())

    def read_worksheet_as_lod(self, worksheet_name):
        return self.open_googlesheet(worksheet_name).get_all_records()

    def read_worksheet_as_lol(self, worksheet_name):
        return self.open_googlesheet(worksheet_name).get_all_values()