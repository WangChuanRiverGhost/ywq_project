# README 模板与 .gitignore

> 本文件包含三份模板：① 仓库根 README ② 项目 README ③ .gitignore。
> 使用时复制对应段落，替换掉尖括号占位内容即可。

---

## ① 仓库根 README.md 模板

```markdown
# ywq_project — Python 实训仓库

> 一句话说明：16 周技术岗就业冲刺的学习轨迹仓库。

## 目录结构

按周归档，每周一个目录；主线项目独立在根级 `项目/`。

```text
ywq_project/
├── docs/          # 规范文档
├── 第N周/          # 第N周学习计划_学生版.md + 学习日志/ + 作业代码/
└── 项目/          # 主线项目，唯一位置
    └── 用户管理系统/
```

> 详细命名规则见 docs/05_命名与目录规范.md。

## 16 周学习轨迹

| 周次 | 主题 | 核心产出 | 状态 |
|---|---|---|---|
| 第1周 | <主题> | <产出> | ✅ / 🔄 / 计划中 |

## 提交规范

格式：`类型: 第N周 内容简述`（feat / log / plan / fix / docs）

## 每日提交节奏

git pull → 放文件 → git add . → git commit -m "..." → git push

## 文档索引

| 文件 | 用途 |
|---|---|
| docs/01_新人入门指引.md | 环境安装 + 仓库使用 |
| docs/05_命名与目录规范.md | 命名规则 |
```

---

## ② 项目 README.md 模板（放在 `项目/用户管理系统/`）

> 注意事项：文件名必须是 **README.md**（全大写）。写成 REMADE.md / Readme.md 等，GitHub 不会在首页渲染。

```markdown
# 用户管理系统

一个基于 FastAPI + MySQL 的用户管理 + 待办事项管理系统。

## 技术栈

- Python 3.10+ / FastAPI
- Pydantic v2（数据校验）
- APIRouter（路由分层）
- SQLAlchemy + MySQL（数据持久化）
- Postman / Apifox（接口测试）

## 快速开始

```bash
git clone https://github.com/WangChuanRiverGhost/ywq_project.git
cd ywq_project/项目/用户管理系统
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
uvicorn main:app --reload
```

浏览器打开 http://127.0.0.1:8000/docs

## 项目结构

```text
用户管理系统/
├── main.py          # 应用入口
├── routers/         # 路由层
├── schemas/         # Pydantic 模型层
├── models/          # 数据库模型层
├── database.py      # 数据库连接
├── requirements.txt
└── README.md
```

## 接口清单

> 必须与实际路由完全一致。`APIRouter(prefix="/users")` 配 `@router.post("/register")`，实际路径是 `/users/register`，不是 `/users/users/register`。

| 方法 | 路径 | 说明 |
|---|---|---|
| POST | /users/register | 用户注册 |
| POST | /users/login | 用户登录 |

## 接口测试

见 Postman Collection `项目/用户管理系统/postman/`。
```

---

## ③ .gitignore（仓库根目录）

```gitignore
# 虚拟环境（体积大，本地用即可，不提交）
venv/
.venv/

# Python 缓存
__pycache__/
*.pyc

# 数据库文件（运行时自动生成）
*.db

# 环境变量（含密钥，绝不提交）
.env

# 编辑器配置
.vscode/
.idea/
```
