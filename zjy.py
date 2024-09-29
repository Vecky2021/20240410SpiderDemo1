from tkinter import Tk, Label, Button, Entry, END
# 创建主窗口
root = Tk()
# 设置窗口标题
root.title("学生成绩管理系统")

# 创建标签，显示学生姓名
label_name = Label(root, text="学生姓名：")
label_name.pack()

# 创建输入框，用于输入学生姓名
entry_name = Entry(root)
entry_name.pack()

# 创建标签，显示学科 1
label_subject1 = Label(root, text="学科 1：")
label_subject1.pack()

# 创建输入框，用于输入学科 1 的成绩
entry_subject1 = Entry(root)
entry_subject1.pack()

# 创建标签，显示学科 2
label_subject2 = Label(root, text="学科 2：")
label_subject2.pack()

# 创建输入框，用于输入学科 2 的成绩
entry_subject2 = Entry(root)
entry_subject2.pack()

# 创建标签，显示学科 3
label_subject3 = Label(root, text="学科 3：")
label_subject3.pack()

# 创建输入框，用于输入学科 3 的成绩
entry_subject3 = Entry(root)
entry_subject3.pack()

# 创建保存按钮
button_save = Button(root, text="保存", command=lambda: save_student_info())
button_save.pack()

def save_student_info():
    # 在这里获取输入的学生信息并进行处理，例如保存到数据库或其他地方
    student_name = entry_name.get()
    subject1_score = float(entry_subject1.get())
    subject2_score = float(entry_subject2.get())
    subject3_score = float(entry_subject3.get())
    print(f"学生 {student_name} 的成绩：学科 1 {subject1_score}，学科 2 {subject2_score}，学科 3 {subject3_score}")