import sheetsconnector
from typing import Optional

class Config(sheetsconnector.Sheetsconnector):

    GOOGLESHEET_ID = "11iCvHhbNJH2q6viSHgg4LlzAIqp4d564dBlBBEqJPzs"
    SETTINGS_SHEET_NAME = "Settings"
    HEADER = ["Descriptions", "Answers"]

    def __init__(self):
        super().__init__(Config.GOOGLESHEET_ID)
        self.settings = self.read_settings()

    def read_settings(self):
        return self.read_worksheet_as_lod(self.SETTINGS_SHEET_NAME)


    @staticmethod
    def str2num(string: str):
        percent: bool = False
        result: Optional[float] = None

        # ~~ Corner case!!! ~~

        if string == 'onwards':
            return float('inf')
        string = string.replace('$', '')
        if string[-1] == '%':
            percent = True
            string = string.replace('%', '')
            # result = float(string.replace('%', '')) / 100
        if string.count('.') == 1 and string.count(',') >= 0:
            result = float(string.replace(',', ''))
        if string.count(',') == 1 and string.count('.') == 0:
            result = float(string.replace(',', '.'))
        if string.count(',') == 0 and string.count('.') == 0:
            result = int(string)
        if percent:
            result /= 100
        return result

    @staticmethod
    def convert_type(string: str):
        percent: bool = False
        result: Optional[float] = None
        # result: None

        if string[-1] == "%":
            percent = True
            string = string.replace("%", "")
        # if string.count(",") == 1 and string.count(".") == 0:
        #     result = float(string.replace(",", "."))
        # if string.count('.') == 1 and string.count(',') >= 0:
        #     result = float(string.replace(',', ''))
        if string.count(".") == 0 and string.count(",") == 0:
            result = int(string)
        if percent:
            result /= 100
        if string == "TRUE" or string == "FALSE":
            result = bool(string)
        return result