# Python : 新聞文本分類
### <本專案目的為利用機器學習(K-means)來判斷文本分群>
### Step 1. 資料轉檔
####        首先，將原先爬蟲完的資料檔案(預設為Excel檔案格式)，轉為json檔案方便後續無論是資料呈現或網站開發都較方便。
####        轉檔案的過程中，因為資料型態有「時間」這個因子，然而Excel與Python的日期計算起始點不同，所以需要創立日期轉換的function。
####        範例如下：
            #自定義fucntion轉換
            def datetrans(xldate, datemode):
               return (
               datetime.datetime(1899, 12, 30)
               + datetime.timedelta(days=xldate + 1462 * datemode)
               )
####        [第一步完整範例在此](https://github.com/Michael-Yan-wun/Python-News-Content/blob/master/Step1%20%E8%B3%87%E6%96%99%E8%BD%89%E6%AA%94/Step1%20%E8%B3%87%E6%96%99%E8%BD%89%E6%AA%94.py "Step one") 
####
### Step 2. 資料前處理
####        接著，將資料引入後需要將資料作前處理，也就是所謂資料預處理，需要將資料整理成後續機器學習的測試集。
####        在這步驟中我們需要導入Jieba套件，並且匯入停字庫讓新聞文章切除不必要的語助詞，例如：妳、我、他、的、是嗎......
####        除此之外，同時將非必要的特殊文字或者標點符號刪去。
####        範例如下：
            #去除繁體中文以外的英文、數字、符號
            #NewsContent為新聞內文的list
            rule = re.compile(r"[^\u4e00-\u9fa5]")
            NewsContent = [list(jieba.cut(rule.sub('', content))) for content in NewsContent]      
####        [第二步完整範例在此](https://github.com/Michael-Yan-wun/Python-News-Content/blob/master/Step2%20%E8%B3%87%E6%96%99%E5%89%8D%E8%99%95%E7%90%86/Step2%20%E8%B3%87%E6%96%99%E5%89%8D%E8%99%95%E7%90%86.py "Step two")
### Step 3. K-means++
####        在第三步中套入K-means++。
####        所謂K-means是集群分析(又稱c-means Clustering，中文又稱k-平均演算法)，且K-means為非監督機器學習，用白話來說就是將性質相近的資料放置再一起，不斷經過計算點與點之見的距離，讓越相近的點分類為同意群的過程。
####        然而因為k-means不會有重新尋找中心點的計算過程，導致訓練模型在新的點進來時會有些偏離，因此誕生的不斷重新尋找中心點的k-means++。
####        k-means++的過程首先產生一個隨機的中心點，然後再計算每個點與這個中心點的距離，然而離中心點越近的點就會被歸類為同一群，最遠的點則會變成新的中心點。
####        不斷重複計算1000次(此專案設立1000次迭代)後，達到每次計算都拿最遠的點當作新的中心點，達成每次更新中心點。
####        最後將每個點藉由新的中心點將每個點分成n群，進而完成分類任務。
####        [第三步完整範例在此](https://github.com/Michael-Yan-wun/Python-News-Content/blob/master/Step3%20K-means%2B%2B%E5%BB%BA%E7%AB%8B/Step3%20K-means%2B%2B%E5%BB%BA%E7%AB%8B.py "Step two")

### Step 4. 訓練並輸出結果為json檔
####        最後將訓練結果輸出成json檔，使前後端都方便使用此次分群的結果。
