from db_helper import *

def show_menu():   # 显示菜单
    """显示菜单"""
    print("""
    ===== 待办事项管理 =====
    1. 添加任务
    2. 查看所有任务
    3. 查看未完成任务
    4. 完成任务
    5. 删除任务
    0. 退出
    ========================
    """)

def main():
    init_db()
    while True:

        show_menu()
        choice = input("请选择：")

        try:
            choice = int(choice)
        except ValueError:
            print("输入错误，请重新输入（输入需要为纯数字，不能包含字母、小数点或空格）")
            continue
        if choice == 1:
            user_title = input("请输入您要添加的待办事项：")
            if add_task(user_title):
                print("代办添加成功！请继续操作。")
                continue
            else:
                print("代办添加失败，请重新操作")
                continue
        elif choice == 2:
            rows = get_all_tasks()
            for row in rows:
                data_str = f"事项id：{row[0]} 事项内容：{row[1]} 事项状态：{row[2]} 创建时间：{row[3]}\n"
                print(data_str)
        elif choice == 3:
            rows = get_tasks_by_status("未完成")
            for row in rows:
                data_str = f"事项id：{row[0]} 事项内容：{row[1]} 事项状态：{row[2]}\n"
                print(data_str)            
        elif choice == 4:
            done_id = input("请输入已完成事项的编号：")
            try:
                done_id = int(done_id)
            except ValueError:
                print("输入错误，请重新输入（输入需要为纯数字，不能包含字母、小数点或空格）")
                continue
            if complete_task(done_id):
                print("状态修改成功！请继续操作。")
                continue
            else:
                print("状态修改失败，请重新操作")
                continue
        elif choice == 5:
            del_id = input("请输入已完成事项的编号：")
            try:
                del_id = int(del_id)
            except ValueError:
                print("输入错误，请重新输入（输入需要为纯数字，不能包含字母、小数点或空格）")
                continue
            if delete_task(del_id):
                print("代办删除成功！请继续操作。")
                continue
            else:
                print("代办删除失败，请重新操作")
                continue
        elif choice == 0:
            break
        else:
            print("请输入选项内的数字。")

if __name__ == '__main__':
    main()