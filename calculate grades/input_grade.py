import json

name = str(input("請輸入名稱:"))
exam1, exam2, exam3 = map(eval, input("請輸入成績(使用空白間隔開):").split())

def get_info(): #打開json 檔案
    with open('Grades.json','r') as f:
        name = json.load(f)
    return name

def read_info(name): #讀取使用者資料
    names = get_info()
    if str(name) in names:
        return False

    if str(name) not in names:
        names[str(name)] = {}
        names[str(name)]["first"] = 0
        names[str(name)]["second"] = 0
        names[str(name)]["final"] = 0
    
    with open("Grades.json","w") as f: #打開json檔案，然後寫入
        names = json.dump(names,f, indent=4)
    return True

read_info(name)
name_id = get_info()

name_id[str(name)]['first'] = exam1
name_id[str(name)]['second'] = exam2
name_id[str(name)]['final'] = exam3

with open("Grades.json","w") as f:
    json.dump(name_id,f, indent=4)
