import sheetsconnector
import config

GOOGLESHEET_ID = "11iCvHhbNJH2q6viSHgg4LlzAIqp4d564dBlBBEqJPzs"


test = sheetsconnector.Sheetsconnector.open_googlesheet(sheetsconnector.Sheetsconnector(GOOGLESHEET_ID), "Settings")
# table = config.Config()
lod = sheetsconnector.Sheetsconnector.read_worksheet_as_lod(sheetsconnector.Sheetsconnector(GOOGLESHEET_ID), "Settings")
print(lod)

# print(lod[2]["Descriptions"])
# print(lod[2]["Answers"])

# perc = config.Config.str2perc(lod[4]["Answers"])
# print(type(lod[0]["Answers"]))
# print(type(lod[1]["Answers"]))
# print(type(lod[2]["Answers"]))
# print(type(lod[3]["Answers"]))
#
# perc = config.Config.str2num(lod[3]["Answers"])
#
# print(type(lod[3]["Answers"]))
# print(type(lod[4]["Answers"]))


for row in lod:
    print(row["Answers"])


for row in lod:
    n = row["Answers"]
    config.Config.convert_type(n)
    print(type(n))
#
# for row_num, row in enumerate(lod):
#     # n = config.Config.convert_type(lod[0:]["Answers"])
#     print(row_num)
#     print(type(row["Answers"]))
#
# for row in lod:
#     print(row["Answers"])




# stuff = "80%"
#
# percon = config.Config.convert_type(stuff)
# print(stuff)
# print(type(stuff))
# print(percon)
# print(type(percon))