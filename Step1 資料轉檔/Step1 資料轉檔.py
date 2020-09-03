import xlrd
import json
import operator
import time
import datetime
#針對excel時間做轉換
def datetrans(xldate, datemode):
    return (
        datetime.datetime(1899, 12, 30)
        + datetime.timedelta(days=xldate + 1462 * datemode)
        )
def read_xlsx(filename):
    # 開啟excel檔案
    data1 = xlrd.open_workbook(filename)
    # 讀取第一個工作表
    table = data1.sheets()[0]
    # 統計行數
    n_rows = table.nrows
 
    data = []
 
    for v in range(1, n_rows-1):
        # 每一行資料形成一個列表
        values = table.row_values(v)
        # 列表形成字典
        data.append({"Id": values[0],
                     "NewsId":   values[1],
                     "NewsUrl":       values[2],
                     "NewsTitle":    values[3],
                     "NewsContent":         values[4],
                     "NewsTime": datetrans(values[5],0).strftime('%y-%m-%d'),
                     "NewsSite":        values[6],
                     "NewsChannel":        values[7],
                     "NewsAuthor":      values[8],
                     "Sentiment":      values[9],
                     "CtyName":      values[10],
                     "LocName":      values[11],
                     "PplName":      values[12],
                     "ComName":      values[13],
                     "AMLKeyword":      values[14],
                     "CreatedTime":  datetrans(values[15],0).strftime('%y-%m-%d'),
                     })
    return data

#寫入json檔
Data = read_xlsx("Data.xlsx")
with open('Output.json','w', encoding = 'utf8' ) as f:
    json.dump(Data,f,indent=4,ensure_ascii=False)
print("載入入檔案完成...")

