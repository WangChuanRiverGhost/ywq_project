# 周四：列表、字典、模块、虚拟环境

# 练习一：列表与字典操作
num_list = [3, 1, 4, 1, 5, 9, 2, 6, 5]
print(set(num_list))
num_list.sort()  # 升序
print(sorted(num_list))
num_list.sort(reverse=True)  # 降序
print(sorted(num_list,reverse=True))
print(sorted(num_list,reverse=True)[:3])  # 取前三
print(sum(num_list))
print(sum(num_list)/len(num_list))

mes = {"name": "小明", "age": 18, "scores": [80, 90, 85]}
print(f"姓名：{mes["name"]}")
print(f"年龄：{mes['age']}")
print(sum(mes["scores"])/len(mes["scores"]))
mes["grade"] = "B"
mes.pop("age")
print(mes)