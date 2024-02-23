from flask import Flask, request, render_template ,url_for ,json, jsonify,send_from_directory
import os ,datetime
import imageTest as iT

app = Flask(__name__)
dataFileName = f'json_files/UserImageAfter.json'

@app.route('/myImg')
def index():
  return render_template('mytest5.html')

@app.route('/histogram1')
def index2():
  return render_template('mytest6.html')

# @app.route('/login')
@app.route('/')
def index3():
  return render_template('mytest5_login.html')

@app.route('/signup')
def index4():
  return render_template('mytest5_signup.html')

@app.route('/myeventList')
def index5():
  return render_template('mytest5_eventlist.html')

@app.route('/myeventList_addNew')
def index6():
  return render_template('mytest5_Create.html')

@app.route('/myeventList_Edit')
def index7():
  return render_template('mytest5_Edit.html')

@app.route('/saveImage', methods=['POST'])
def save_image():
    try:
        data = request.get_json()
        # check =  int('data' in data)*10 
        # check =  int('width' in data)*10 
        # check =  int('height' in data)*10 
        # check2 = 0
        # print(type(data))
        # print(list(data.key()))
        if 'width' in data and 'height' in data and 'data' in data:
            # check2 = 1
           
            width = data['width']
            height = data['height']
            image_data = data['data']
            # print(image_data)
            # Create a directory to save the JSON files (if it doesn't exist)
            if not os.path.exists('json_files'):
                os.makedirs('json_files')

            # Generate a unique filename or use a specific naming convention
            # filename = f'json_files/canvas_image_{width}x{height}.json'
            filename = f'json_files/UserImage.json'

            with open(filename, 'w') as file:
                # file.write(jsonify(data))
                file.write(json.dumps(data, separators=(',', ':')))

            return 'JSON file saved successfully', 200
        else:
            return 'Invalid JSON data', 400
    except Exception as e:
        print(str(e))
        return 'Error saving JSON file',500

@app.route('/changeImageHistogram', methods=['get'])
def changeImageHistogram():
    iT.changeImageHistogram()

    with open(dataFileName) as f:
        data = json.load(f)

    return jsonify(data) 

@app.route('/HistData1', methods=['get'])
def getHistData1():
    with open("./Hist.json") as f:
        data = json.load(f)
    return jsonify(data)

@app.route('/signup_Savein', methods=['POST'])
def signup_Savein():
    filename = f'json_files/account.json'

    data = request.get_json()
    with open(filename) as f:
        SignUPdata = json.load(f)
    newSignUp = {
        "account":data["account"],
        "code "  :data["code"]
    }

    for i in range(len(SignUPdata)):
        if SignUPdata[i]["account"] == data["account"]:
            return "帳號已存在"
    SignUPdata.append(newSignUp)

    with open(filename, 'w') as file:
        # file.write(jsonify(data))
        file.write(json.dumps(SignUPdata, separators=(',',':')))

    return 'sign up success'

@app.route('/login1', methods=['POST'])
def login():
    filename = f'json_files/account.json'

    data = request.get_json()
    with open(filename) as f:
        LogIndata = json.load(f)
    # newLogIn = {
    #     "account":data["account"],
    #     "code "  :data["code"]
    # }

    for i in range(len(LogIndata)):
        if LogIndata[i]["account"] == data["account"]:
            if LogIndata[i]["code "] == data["code"]:
                return "登入成功"
            else:
                return "密碼錯誤"
    
    return "查無此帳號"

@app.route('/eventlist/list', methods=['get'])
def geteventlist_list():
    with open("./json_files/eventlist.json") as f:
        data = json.load(f)
    return jsonify(data)

@app.route('/eventlist/create', methods=['post'])
def eventlist_add():
    data = request.get_json()
    filename = f'json_files/eventlist.json'
    with open(filename) as f:
        MyList = json.load(f)
    List_new = {
        "todoTableId":datetime.datetime.now().strftime('%Y%m%d%H%M%S'),
        "title":data["title"],
        "isComplete":data["isComplete"]
    }

    if (List_new["isComplete"]):
        MyList.append(List_new)
    else:
        MyList.insert(0,List_new)

    with open(filename, 'w') as file:
        # file.write(jsonify(data))
        file.write(json.dumps(MyList, separators=(',', ':')))
    return "success"

@app.route('/eventlist/delete/<deleteid>', methods=['delete'])
def eventlist_delete(deleteid):
    
    filename = f'json_files/eventlist.json'
    with open(filename) as f:
        MyList = json.load(f)
    

    for i in range(len(MyList)):
        if MyList[i]["todoTableId"]==deleteid:
            MyList.pop(i)
            with open(filename, 'w') as file:
                # file.write(jsonify(data))
                file.write(json.dumps(MyList, separators=(',', ':')))
            return "success"
    return "not found"
    
@app.route('/eventlist/item/<itemid>', methods=['get'])
def eventlist_item(itemid):
    filename = f'json_files/eventlist.json'
    with open(filename) as f:
        MyList = json.load(f)
    for i in range(len(MyList)):
        if MyList[i]["todoTableId"]==itemid:
            return MyList[i]
    return "not found"

@app.route('/eventlist/item', methods=['put'])
def eventlist_item_edit():
    data = request.get_json()
    filename = f'json_files/eventlist.json'
    with open(filename) as f:
        MyList = json.load(f)
    for i in range(len(MyList)):
        if MyList[i]["todoTableId"]==data["todoTableId"]:
            MyList[i]["title"]=data["title"]
            MyList[i]["isComplete"]=data["isComplete"]
            if(data["isComplete"]):
                MyList.append(MyList[i])
                MyList.pop(i)
            else:
                MyList.insert(0,MyList[i])
                MyList.pop(i+1)
            with open(filename, 'w') as file:
                # file.write(jsonify(data))
                file.write(json.dumps(MyList, separators=(',', ':')))
            return "list update"
    return "not found"    

@app.route('/eventlist/item/clickComplete', methods=['put'])
def eventlist_item_ClickEdit():
    data = request.get_json()
    filename = f'json_files/eventlist.json'
    with open(filename) as f:
        MyList = json.load(f)
    for i in range(len(MyList)):
        if MyList[i]["todoTableId"]==data["todoTableId"]:
            MyList[i]["isComplete"] =1
            MyList.append(MyList[i])
            MyList.pop(i)
            with open(filename, 'w') as file:
                # file.write(jsonify(data))
                file.write(json.dumps(MyList, separators=(',', ':')))
            return "list update"
    return "not found"    




@app.route('/save_org_img_test', methods=['post'])
def save_org_img():
    # filename = f'json_files/saveTest.json'
    # data = request.get_json()

    # with open(filename, 'w') as file:
    #     # file.write(jsonify(data))
    #     file.write(json.dumps(data, separators=(',', ':')))
    # return "success"
    #-----------------------------------------------------------
     # 確認是否有上傳檔案
    if 'uploadMyFile' not in request.files:
        return 'No file part'

    file = request.files['uploadMyFile']

    # 確認檔案名稱不為空且檔案類型為PNG
    if file.filename == '' or not file.filename.endswith('.png'):
        return 'Invalid file'

    # 將檔案存儲到指定路徑
    file.save(os.path.join('./static/', 'uploaded.png'))

    return 'File uploaded successfully'

@app.route('/download_myImg')
def download():
    # 下載存儲的檔案
    return send_from_directory('./static/', 'after.png', as_attachment=True , download_name='image2.png')
    
# Python 內建的 json.dumps，可以將 Python 對象 (例如：字典 dict 或列表 list) 轉換成 JSON-formatted string，與 Flask jsonify 的差異在於 Http response 時，需自己手動加入 content-type = application/json
# https://www.maxlist.xyz/2020/05/15/flask-serializing/

if __name__ == '__main__':
    app.run(debug=True)