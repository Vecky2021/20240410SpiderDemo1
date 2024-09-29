stuList = [] # 保存学生信息的列表

def input_stu(): # 录入函数
    stuName = input("录入姓名：")
    yuwen = int(input("输入语文成绩："))
    shuxue = int(input("输入数学成绩："))
    yingyu = int(input("输入英语成绩："))
    stu = {} # 创建空字典，用于保存一条学生信息
    stu['name'] = stuName
    stu['yuwen'] = yuwen
    stu['shuxue'] = shuxue
    stu['yingyu'] = yingyu
    stuList.append(stu) # 把当前字典添加到学生信息列表中

def show_stu(): # 查看函数
    for l in stuList:
        print('姓名:',l['name'],'语文:',l['yuwen'],'数学:',l['shuxue'],'英语:',l['yingyu'])

def search_stu(): # 搜索函数
    search_name = input("输入搜索的姓名：")
    for l in stuList:
        if search_name == l['name']:
            print('姓名:', l['name'], '语文:', l['yuwen'], '数学:', l['shuxue'], '英语:', l['yingyu'])

def change_stu(): # 修改函数
    search_name = input("输入搜索的姓名：")
    for l in stuList:
        if search_name == l['name']:
            l['yuwen'] = int(input("输入新的语文成绩："))
            l['shuxue'] = int(input("输入新的数学成绩："))
            l['yingyu'] = int(input("输入新的英语成绩："))

while True: # 程序主循环
    print("1. 录入成绩")
    print("2. 查看成绩")
    print("3. 搜索信息")
    print("4. 修改成绩")
    opt = int(input("输入1-4"))
    if opt == 1:
        input_stu()
    elif opt == 2:
        show_stu()
    elif opt == 3:
        search_stu()
    elif opt == 4:
        change_stu()
