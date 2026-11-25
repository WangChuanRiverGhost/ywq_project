# 用户管理系统

一个基于 FastAPI 的用户管理 + 待办事项管理系统，支持用户注册/登录、待办事项增删改查。

## 技术栈

- Python 3.14 + FastAPI
- Pydantic v2（数据校验）
- APIRouter（路由分层）
- 内存存储（第 7 周将切换为 MySQL）
- Postman / Apifox（接口测试）

## 快速开始

### 1. 克隆仓库
```bash
git clone https://github.com/WangChuanRiverGhost/ywq_project.git
cd 第六周/用户管理项目
```

### 2. 安装依赖
```bash
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
```

### 3. 启动项目
```bash
uvicorn main:app --reload
```
访问/docs。

### 4. 打开接口文档
浏览器访问 http://127.0.0.1:8000/docs 就能看到 Swagger 文档，所有接口都能在线测试。

## 项目结构

```
用户管理项目/
├── main.py           # 应用入口
├── routers/          # 路由层（按模块分文件）
│   ├── users.py      # 用户模块
│   └── todos.py      # 待办模块
├── schemas/          # Pydantic 模型层
├── models/           # 数据库模型（第 7 周使用）
├── database.py       # 数据库连接（第 7 周使用）
├── requirements.txt  # 依赖清单
└── README.md         # 本文件
```

## 接口清单

### 用户模块
- `POST /users/register` — 用户注册
- `POST /users/login` — 用户登录（明天完成）

### 待办模块
- `POST /todos/` — 新增待办
- `GET /todos/` — 查所有待办
- `GET /todos/{todo_id}` — 查某一条待办
- `PUT /todos/{todo_id}` — 修改某一条待办
- `DELETE /todos/{todo_id}` — 删除某一条待办

## 接口测试
项目启动后，可通过 Swagger UI、Postman 或 Apifox 测试接口。推荐先用 /docs 确认接口定义，再用 Postman / Apifox 做完整流程测试。  
### 1、启动服务
```
uvicorn main:app --reload
```
启动后访问：http://127.0.0.1:8000/docs
### 2、用postman测试
#### 步骤一：注册用户
方法：POST  
url：http://127.0.0.1:8000/users/users
body：
```
{
  "username": "aaa",
  "password": "12345678",
  "email": "aaa@outlook.com"
}
```
预期响应：200 OK
用户名重复/密码长度不符合要求：400 Bad Request
#### 步骤二：登录并获取token
方法：POST  
url：http://127.0.0.1:8000/users/users/login
body：
```
{
  "username": "aaa",
  "password": "12345678"
}
```
预期响应：200 OK
用户名不存在/密码错误：401 Unauthorized
#### 步骤三：用token访问接口
方法：GET
url：http://127.0.0.1:8000/users/my-account
body：
```
{
  "user_id": 1
}
```
预期响应：200 OK
## 未来计划
下周切换 MySQL、加爬虫模块、加部署