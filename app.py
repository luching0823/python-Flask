from flask import Flask # 載入Flask
from flask import request # 載入request
from flask import redirect # 載入redirect
from flask import render_template # 載入render_template
import json

app = Flask( # 建立application，設定靜態檔案路徑
    __name__,
    static_folder="static", # 靜態檔案資料夾名稱
    static_url_path="/static"
    ) # 靜態檔案對應的網址路徑(可以只打 / ，就變成像在根目錄底下)

#路由設定：建立路徑 / 對應的處理函式
@app.route("/") # 1.路由裝飾器（首頁）
def index(): #2.回應的函式
    return render_template("index", name="Pulin") #從templates往下看檔案路徑
    # return redirect("https://www.google.com.tw") # 導向至google
#     print("請求方法：", request.method)
#     print("通訊協定：", request.scheme)
#     print("瀏覽器與作業系統：", request.headers.get("user-agent"))
#     print("語言偏好：", request.headers.get("accept-language"))
#     lang = request.headers.get("accept-language")
#     if lang.startswith("en"):
#         return redirect("/en/")
#     else:
#         return redirect("/zh/")
#     # return "Hello Flask" # 回應的內容
# #路由設定結束

# @app.route("/en/")
# def index_English():
#     return json.dumps({ # 回應json格式字串
#             "status": "ok",
#             "text": "Hello World"
#         })

# @app.route("/zh/")
# def index_Chinese():
#     return json.dumps({
#             "status": "ok",
#             "text": "您好"
#         }, ensure_ascii=False) # 不要用ASCII編碼處理中文

# @app.route("/data")
# def handleData():
#     return "myData"

# #動態路由：支援擁有相同字首的路由設定
# @app.route("/user/<userName>")
# def handleUser(userName):
#     return "Hi " + userName

# # 擷取要求字串(Query String) -> max
# @app.route("/getSum") #1+2+3+...+max
# def getSum():
#     min = request.args.get("min", 1) # 擷取min的值，預設1
#     max = request.args.get("max", 100) # 擷取max的值，預設100
#     min = int(min)
#     max = int(max) #String to Int
#     print("最小值：", max)
#     print("最大值：", max)
#     result = 0
#     for n in range(min,max+1):
#         result += n
#     return "結果：" + str(result)

# 啟動網站伺服器，可以透過port指定阜號
app.run(port = 3000)

