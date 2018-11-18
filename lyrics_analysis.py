import codecs
from konlpy.tag import Okt
okt = Okt()
import pandas as pd
from openpyxl.utils.dataframe import dataframe_to_rows
from openpyxl import Workbook
wb = Workbook()
ws = wb.create_sheet(title = "analysis")

data = codecs.open("d:/python/study/lyrics/data/ikon_goodbyeroad.txt", "r", encoding="utf-8")
tae_be_li = []
pum_be_li = []
tae_af_li = []
pum_af_li = []
for line in data :
    wd_be = okt.pos(line)
    for tae_be, pum_be in wd_be :
        tae_be_li.append(tae_be)
        pum_be_li.append(pum_be)
    wd_af = okt.pos(line, norm=True, stem=True)
    for tae_af, pum_af in wd_af :
        tae_af_li.append(tae_af)
        pum_af_li.append(pum_af)

raw_data = {"형태소(전)" : tae_be_li,
            "품사" : pum_be_li,
            "형태소(후)" : tae_af_li}
df = pd.DataFrame(raw_data, columns = ["형태소(전)","품사","형태소(후)"])
for row in dataframe_to_rows(df, index=True, header=True):
    if len(row) > 1:
        ws.append(row)
wb.save("D:/python/study/lyrics/ikon_goodbyeroad.xlsx") #저장
