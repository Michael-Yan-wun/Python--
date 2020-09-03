# Python : 新聞文本分類
### <本專案目的為利用監督式機器學習(K-means)來判斷文本分群>
#### Step 1. 資料轉檔
####         首先，將原先爬蟲完的資料檔案(預設為Excel檔案格式)，轉為json檔案方便後續無論是資料呈現或網站開發都較方便。
####         轉檔案的過程中，因為資料型態有「時間」這個因子，然而Excel與Python的日期計算起始點不同，所以需要創立日期轉換的function。(範例如下)
            
             def datetrans(xldate, datemode):
                return (
                datetime.datetime(1899, 12, 30)
                + datetime.timedelta(days=xldate + 1462 * datemode)
                )
####
####
####
####
