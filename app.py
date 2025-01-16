from flask import Flask,request
import json
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World! nice to meet you. good bye.see you again..."

@app.route("/let")
def play():
    return "Let's Go!! shall we dance?"

@app.route('/_api')
def get():
     d = request.args.get("d")
     list = d.split("_")
     u = request.args.get("user")
     di = {}
     di["timeMachine"] = {}
     di["today"] = {}
     di["timeMachine"]["recent"] = {}
     di["timeMachine"]["past"] = {}
     di["timeMachine"]["future"] = {}
     with open(f"./data/user/{u}.json") as f:
        str = json.load(f)
        for i in range(len(str)):
            if str[i] == f"user/{u}/メモ_{d}.md":
                if i != 0:
                    di["timeMachine"]["recent"]["prev"] = str[i-1]
                if i != len(str)-1:
                    di["timeMachine"]["recent"]["next"] = str[i+1]
        for j in range(1,4):
            for i in range(len(str)-1,-1,-1):
                if int(str[i].split("/")[2].split("_")[1]) == int(list[0])-j and int(str[i].split("/")[2].split("_")[3].split(".")[0]) <= int(list[2]) and int(str[i].split("/")[2].split("_")[2]) == int(list[1]):
                    di["timeMachine"]["past"][f"{j}"] = str[i]
                    break
                elif int(str[i].split("/")[2].split("_")[1]) == int(list[0])-j and int(str[i].split("/")[2].split("_")[2]) < int(list[1]):
                    di["timeMachine"]["past"][f"{j}"] = str[i]
                    break
                elif int(str[i].split("/")[2].split("_")[1]) < int(list[0])-j:
                    di["timeMachine"]["past"][f"{j}"] = str[i]
                    break
        for j in range(1,4):
            for i in range(len(str)):
                if int(str[i].split("/")[2].split("_")[1]) == int(list[0])+j and int(str[i].split("/")[2].split("_")[3].split(".")[0]) >= int(list[2]) and int(str[i].split("/")[2].split("_")[2]) == int(list[1]):
                    di["timeMachine"]["future"][f"{j}"] = str[i]
                    break
                elif int(str[i].split("/")[2].split("_")[1]) == int(list[0])+j and int(str[i].split("/")[2].split("_")[2]) > int(list[1]):
                    di["timeMachine"]["future"][f"{j}"] = str[i]
                    break
                elif int(str[i].split("/")[2].split("_")[1]) > int(list[0])+j:
                    di["timeMachine"]["future"][f"{j}"] = str[i]
                    break
 
     with open(f"./data/all.json") as f:
         str = json.load(f)
         userdata = str[f"{d}"]
         for d in userdata:
             name = d.split("/")[1]
             di["today"][name] = d
         return json.dumps(di)

@app.route('/time')
def time():
    d = request.args.get("d")
    list = d.split("_")
    u = request.args.get("user")
    di = {}
    di["timeMachine"] = {}
    di["timeMachine"]["recent"] = {}
    di["timeMachine"]["past"] = {}
    di["timeMachine"]["future"] = {}
    with open(f"./data/user/{u}.json") as f:
        str = json.load(f)
        for i in range(len(str)):
            if str[i] == f"user/{u}/メモ_{d}.md":
                if i != 0:
                    di["timeMachine"]["recent"]["prev"] = str[i-1]
                if i != len(str)-1:
                    di["timeMachine"]["recent"]["next"] = str[i+1]
        for j in range(1,4):
            for i in range(len(str)-1,-1,-1):
                if int(str[i].split("/")[2].split("_")[1]) == int(list[0])-j and int(str[i].split("/")[2].split("_")[3].split(".")[0]) <= int(list[2]) and int(str[i].split("/")[2].split("_")[2]) == int(list[1]):
                    di["timeMachine"]["past"][f"{j}"] = str[i]
                    break
                elif int(str[i].split("/")[2].split("_")[1]) == int(list[0])-j and int(str[i].split("/")[2].split("_")[2]) < int(list[1]):
                    di["timeMachine"]["past"][f"{j}"] = str[i]
                    break
                elif int(str[i].split("/")[2].split("_")[1]) < int(list[0])-j:
                    di["timeMachine"]["past"][f"{j}"] = str[i]
                    break
        for j in range(1,4):
            for i in range(len(str)):
                if int(str[i].split("/")[2].split("_")[1]) == int(list[0])+j and int(str[i].split("/")[2].split("_")[3].split(".")[0]) >= int(list[2]) and int(str[i].split("/")[2].split("_")[2]) == int(list[1]):
                    di["timeMachine"]["future"][f"{j}"] = str[i]
                    break
                elif int(str[i].split("/")[2].split("_")[1]) == int(list[0])+j and int(str[i].split("/")[2].split("_")[2]) > int(list[1]):
                    di["timeMachine"]["future"][f"{j}"] = str[i]
                    break
                elif int(str[i].split("/")[2].split("_")[1]) > int(list[0])+j:
                    di["timeMachine"]["future"][f"{j}"] = str[i]
                    break
    return json.dumps(di)

@app.route('/today')
def today():
    d = request.args.get("d")
    list = d.split("_")
    u = request.args.get("user")
    di = {}
    di["today"] = {}
    with open(f"./data/all.json") as f:
        str = json.load(f)
        userdata = str[f"{d}"]
        for d in userdata:
            name = d.split("/")[1]
            di["today"][name] = d
    return json.dumps(di)

if __name__ == '__main__':
    port = os.environ.get('FLASK_PORT') or 8080
    port = int(port)

    app.run(port=port,host='0.0.0.0')
