from manager import TaskManager
from todo_error import MatterNumError,MatterNameError,MatterCheckError
from db_helper import DBHelper
import logging

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

logger = logging.getLogger("2026-11-04_day16_logging.py")  # 创建记录器对象
sys_handler =  logging.StreamHandler()  # 创建写入控制台的处理器对象
file_handler =  logging.FileHandler(filename="第四周/app.log",mode="a",encoding="utf-8",delay=False)  # 创建输出到文件的处理器
formatter = logging.Formatter(
    fmt="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y/%m/%d %H:%M:%S"
)  # 创建格式器

def yes_debug(record):  # 创建过滤器防止高级别的日志显示在控制台
    if record.levelno < 20:
        return True
    return False

logger.setLevel(logging.DEBUG)  # 配置记录器筛选级别
logger.addHandler(sys_handler)
logger.addHandler(file_handler)  # 绑定处理器

sys_handler.addFilter(yes_debug)

file_handler.setLevel(logging.INFO)  # 配置处理器筛选级别，高于INFO记录到log文件中
file_handler.setFormatter(formatter)  # 绑定格式器


def main():
    """初始化：创建用户表实例-连接数据库与创建游标"""
    user_task = TaskManager("第四周/todo.db","tasks")
    """创建表"""
    user_task.create_table("""
        CREATE TABLE IF NOT EXISTS tasks(
            id INTEGER PRIMARY KEY NOT NULL,
            title TEXT NOT NULL,
            status TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    """程序主循环"""
    while True:

        """收集用户选择的事项"""
        show_menu()
        choice = input("请选择：").strip() 
        logger.info("用户进行了选项输入")
        """异常检查1：检测用户输入是否为数字"""
        try:
            choice = int(choice)

            """异常检查2：检测用户输入是否超出选项范围"""
            if choice not in range(0, 6):
                raise MatterNumError
            
        except ValueError:   # 异常处理1：处理用户输入不符合数字要求的情况
            logger.debug("输入错误，请重新输入（输入需要为纯数字，不能包含字母、小数点或空格）")
            logger.warning("用户输入了非数字")
            continue

        except MatterNumError:   # 异常处理2：处理用户输入超出选项范围的情况
            logger.debug("输入超出范围，请输入选项内的数字")
            logger.warning("用户输入了超出选项范围的数字")
            continue

        """程序运行逻辑"""
        if choice == 1:   # 添加任务
            logger.info("用户选择了添加日程")
            """异常检查3：检测用户输入的标题是否为空"""
            try:
                user_title = input("请输入您要添加的待办事项：").strip() 
                if user_title == "":
                    raise MatterNameError("名称不能为空")
            except MatterNameError:
                logger.warning("用户输入了空字符")
                logger.debug("名称不能为空，请重新操作。")
                continue

            if user_task.add_task(user_title):
                logger.debug("代办添加成功！请继续操作。")
                logger.info("用户添加了一个代办。")
                continue
            else:
                logger.debug("代办添加失败，请重新操作")
                continue

        elif choice == 2:   # 查看所有任务
            logger.info("用户想查看任务")
            rows = user_task.get_all_tasks()
            
            if not rows:
                logger.debug("当前没有待办事项")
                logger.info("没有代办事项给ta查。")
                continue

            for row in rows:
                data_str = f"事项id：{row[0]} 事项内容：{row[1]} 事项状态：{row[2]} 创建时间：{row[3]}\n"
                print(data_str)
            logger.info("用户成功查到了待办事项。")    

        elif choice == 3:   # 查看未完成任务
            rows = user_task.get_tasks_by_status("未完成")
            logger.info("用户想查看未完成任务")

            if not rows:
                logger.debug("当前没有未完成事项")
                logger.info("没有未完成事项给ta查，")
                continue

            for row in rows:
                data_str = f"事项id：{row[0]} 事项内容：{row[1]} 事项状态：{row[2]} 创建时间：{row[3]}\n"
                print(data_str)     
            logger.info("用户成功查到了未完成事项。")
        elif choice == 4:   # 修改任务完成状态
            logger.info("用户想要修改任务完成状态")
            try:
                """异常检测5：检测库中是否有内容"""
                if not user_task.get_all_tasks():
                    raise MatterCheckError("库中没有内容，请添加后再删除")
                
                done_id = input("请输入要修改状态事项的编号：")
                """异常检测1：检测用户输入是否为数字"""
                done_id = int(done_id)
                
                """异常检测4：检测用户输入是否为已存在的事项"""
                if user_task.check_error(done_id):
                    raise MatterCheckError("选择的事项不存在，请重新选择")
            
            except ValueError:   # 异常处理1：处理用户输入非数字的情况
                logger.debug("输入错误，请重新输入（输入需要为纯数字，不能包含字母、小数点或空格）")
                logger.warning("用户输入了非数字")
                continue
            
            except MatterCheckError as e:   # 异常处理4&5：处理空库或用户输入不存在事项的情况
                
                if str(e) == "库中没有内容，请添加后再删除":
                    logger.debug("库中没有内容，请添加后再修改")
                    logger.warning("用户对空库进行了修改待办状态操作")
                else:
                    logger.debug("选择的事项不存在，请重新选择")
                    logger.warning("用户选择了不存在的事项")
                continue
            
            if user_task.complete_task(done_id):
                logger.debug("状态修改成功！请继续操作。")
                logger.info(f"用户成功修改了待办事项：{done_id}")
                continue
            
            else:
                logger.debug("状态修改失败，请重新操作")
                continue
        
        elif choice == 5:   # 删除任务
            logger.info("用户选择了删除任务选项")
            try:

                """异常检测5：检测库中是否有内容"""
                if not user_task.get_all_tasks():
                    raise MatterCheckError("库中没有内容，请添加后再删除")
                
                del_id = input("请输入要删除事项的编号：")
                """异常检测1：检测用户输入是否为数字"""
                del_id = int(del_id)
                
                """异常检测4：检测用户输入是否为已存在的事项"""
                if user_task.check_error(del_id):
                    raise MatterCheckError("选择的事项不存在，请重新选择")
            
            except ValueError:   # 异常处理1：处理用户输入非数字的情况
                logger.debug("输入错误，请重新输入（输入需要为纯数字，不能包含字母、小数点或空格）")
                logger.warning("用户输入了非数字")
                continue
            
            except MatterCheckError as e:   # 异常处理4&5：处理空库或用户输入不存在事项的情况
                
                if str(e) == "库中没有内容，请添加后再删除":
                    logger.debug("库中没有内容，请添加后再删除")
                    logger.warning("用户对空库进行了删除待办操作")
                else:
                    logger.debug("选择的事项不存在，请重新选择")
                    logger.warning("用户选择了不存在的待办事项")
                continue
            
            if user_task.delete_task(del_id):
                logger.debug("代办删除成功！请继续操作。")
                logger.info("用户成功删除了代办。")
                continue
            
            else:
                logger.debug("代办删除失败，请重新操作")
                continue
        
        else:   # 退出
            logger.info("用户退出了程序。")
            user_task.db_close()
            break

if __name__ == '__main__':
    main()