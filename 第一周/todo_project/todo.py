from db_helper import *

class MatterNameError(Exception):
    pass

class MatterNumError(Exception):
    pass

class MatterCheckError(Exception):
    pass

def show_menu():   # 显示菜单
    """显示菜单"""
    print("""
    ===== 待办事项管理 =====
    1. 添加任务
    2. 查看所有任务
    3. 查看未完成任务
    4. 修改任务完成状态
    5. 删除任务
    0. 退出
    ========================
    """)

def main():
    """初始化：连接数据库与创建游标"""
    init_db()

    """程序主循环"""
    while True:

        """收集用户选择的事项"""
        show_menu()
        choice = input("请选择：").strip() 

        """异常检查1：检测用户输入是否为数字"""
        try:
            choice = int(choice)

            """异常检查2：检测用户输入是否超出选项范围"""
            if choice not in range(0, 6):
                raise MatterNumError
            
        except ValueError:   # 异常处理1：处理用户输入不符合数字要求的情况
            print("输入错误，请重新输入（输入需要为纯数字，不能包含字母、小数点或空格）")
            continue

        except MatterNumError:   # 异常处理2：处理用户输入超出选项范围的情况
            print("输入超出范围，请输入选项内的数字")
            continue

        """程序运行逻辑"""
        if choice == 1:   # 添加任务

            """异常检查3：检测用户输入的标题是否为空"""
            try:
                user_title = input("请输入您要添加的待办事项：").strip() 
                if user_title == "":
                    raise MatterNameError("名称不能为空")
            except MatterNameError:
                print("名称不能为空，请重新操作。")
                continue

            if add_task(user_title):
                print("代办添加成功！请继续操作。")
                continue
            else:
                print("代办添加失败，请重新操作")
                continue

        elif choice == 2:   # 查看所有任务
            rows = get_all_tasks()

            if not rows:
                print("当前没有待办事项")
                continue

            for row in rows:
                data_str = f"事项id：{row[0]} 事项内容：{row[1]} 事项状态：{row[2]} 创建时间：{row[3]}\n"
                print(data_str)

        elif choice == 3:   # 查看未完成任务
            rows = get_tasks_by_status("未完成")

            if not rows:
                print("当前没有未完成事项")
                continue

            for row in rows:
                data_str = f"事项id：{row[0]} 事项内容：{row[1]} 事项状态：{row[2]}\n"
                print(data_str)     

        elif choice == 4:   # 修改任务完成状态
            done_id = input("请输入要修改状态事项的编号：")

            """异常检测1：检测用户输入是否为数字"""
            try:
                done_id = int(done_id)
                """异常检测4：检测用户输入是否为已存在的事项"""
                if check_error(done_id):
                    raise MatterCheckError("选择的事项不存在，请重新选择")
            except ValueError:   # 异常处理1：处理用户输入非数字的情况
                print("输入错误，请重新输入（输入需要为纯数字，不能包含字母、小数点或空格）")
                continue
            except MatterCheckError:   # 异常处理4：处理用户输入不存在事项的情况
                print("选择的事项不存在，请重新选择")
                continue
            if complete_task(done_id):
                print("状态修改成功！请继续操作。")
                continue
            else:
                print("状态修改失败，请重新操作")
                continue
        
        elif choice == 5:   # 删除任务
            del_id = input("请输入要删除事项的编号：")

            """异常检测1：检测用户输入是否为已存在的事项"""
            try:
                del_id = int(del_id)
                """异常检测4：检测用户输入是否为已存在的事项"""
                if check_error(del_id):
                    raise MatterCheckError("选择的事项不存在，请重新选择")
            except ValueError:   # 异常处理1：处理用户输入非数字的情况
                print("输入错误，请重新输入（输入需要为纯数字，不能包含字母、小数点或空格）")
                continue
            except MatterCheckError:   # 异常处理4：处理用户输入不存在事项的情况
                print("选择的事项不存在，请重新选择")
                continue
            
            if delete_task(del_id):
                print("代办删除成功！请继续操作。")
                continue
            else:
                print("代办删除失败，请重新操作")
                continue
        
        else:   # 退出
            break

if __name__ == '__main__':
    main()