# Git 提交作业操作指引（学生版）

> 给同学：每天学完 Python，就照着这份步骤把当天的代码和日志提交到 GitHub。
> 全程只有 6 步，做熟之后 2 分钟搞定。

---

## 第一部分：第一次使用（只需做一次）

### 1. 克隆仓库到电脑

打开 **VS Code 的终端**（菜单「终端」→「新建终端」），输入：

```bash
git clone https://github.com/WangChuanRiverGhost/ywq_project.git
```

然后进入仓库目录：

```bash
cd ywq_project
```

### 2. 配置你的身份（第一次用 git 才需要）

```bash
git config --global user.name "你的名字"
git config --global user.email "你的邮箱@qq.com"
```

> 把邮箱换成你自己的。这一步让 git 知道每次提交是谁做的。

### 3. 验证是否成功

```bash
git status
```

看到 `On branch main` 就说明成功了。

---

## 第二部分：每天提交的标准流程（核心，记住这 6 步）

> 顺序固定：**先 pull → 放文件 → 看状态 → 加文件 → 提交 → 推送**

### 第 1 步：先拉取最新（防止和别人冲突）

```bash
cd ywq_project
git pull
```

> 如果提示 `Already up to date.` 说明远程没有新东西，直接继续。

### 第 2 步：把当天代码 / 日志放进对应目录

按规范放到对应位置，例如：

```
作业代码/第1周_Python核心基础/day3_exceptions.py   ← 今天的代码
作业代码/第1周_Python核心基础/面试题自测.md        ← 面试题答案（追加到文档末尾）
学习日志/第1周/2026-10-14_周三.md                  ← 今天的日志
```

> 目录要自己先建好：右键「新建文件夹」，周目录命名要带主题（如 `作业代码/第1周_Python核心基础`），主题名查《仓库规范》第三节的 16 周对照表。

### 第 3 步：查看改了哪些文件

```bash
git status
```

红色字的是「还没加入提交」的文件，确认是不是你要交的那些。

### 第 4 步：把文件加入提交

```bash
git add 作业代码/第1周_Python核心基础/day3_exceptions.py
git add 学习日志/第1周/2026-10-14_周三.md
```

> 想一次加当天所有改动，也可以 `git add .`，但**不推荐**（容易误加 venv 等大文件）。

### 第 5 步：提交（写清楚这次做了什么）

```bash
git commit -m "feat: 第1周 day3 异常处理练习"
```

日志再单独提交一次：

```bash
git commit -m "log: 第1周 周三学习日志"
```

### 第 6 步：推送到 GitHub

```bash
git push
```

看到 `main -> main` 就说明推送成功了。

---

## 第三部分：commit 规范速查（写错会被老师提醒）

格式：`类型: 第N周 内容简述`

| 类型 | 用在什么时候 | 例子 |
|---|---|---|
| `feat` | 交了新代码 / 新作业 | `feat: 第1周 day5 SQLite 练习` |
| `log` | 交了学习日志 | `log: 第1周 周五学习日志` |
| `plan` | 传了学习计划 | `plan: 第1周 学习计划归档` |
| `fix` | 改了之前交的代码 | `fix: 第1周 day2 修正 BMI 计算` |
| `docs` | 改 README 等文档 | `docs: 更新 README` |

**三条红线**：
1. 不要写 `2`、`update`、`123` 这种没意义的话。
2. 类型用小写英文，后面跟中文简述。
3. 一天一交，别攒到周末。

---

## 第四部分：学习日志怎么写（每天 5 分钟）

日志文件命名 `2026-10-14_周三.md`，内容按下面三小段写即可：

```markdown
# 2026-10-14 周三学习日志

## 今天学了什么
（用 2-3 句话概括：异常处理的 try/except 结构）

## 遇到的问题
（写出报错信息 + 你是怎么想的）

## 怎么解决的
（查了哪个资料、问了老师、还是自己试出来的）
```

---

## 第五部分：常见报错怎么办

| 报错提示 | 原因 | 解决办法 |
|---|---|---|
| `fatal: not a git repository` | 不在仓库目录里 | 先 `cd ywq_project` |
| `error: failed to push some refs` | 远程有新提交，本地落后了 | 先 `git pull` 再 `git push` |
| `nothing to commit` | 没东西可提交 | 检查文件是否已 add，或是否已提交过 |
| `Please tell me who you are` | 没配置身份 | 按第一部分第 2 步配置 name/email |
| 输入 commit 后进入奇怪界面 | 忘记写 `-m "..."` | 按 `Esc`，输入 `:wq` 回车退出 |
| 提交了才发现忘改文件 | 文件还没保存 | 保存文件后，重新 `git add` + `git commit` |
| `fatal: unable to access ...` | 网络/加速没开 | 打开 Watt Toolkit 的 GitHub 加速，再重试 |

---

## 第六部分：本周（第1周）完整提交清单

对照第 1 周计划，本周你要交这些，逐项打勾：

> 放哪里：代码和测试清单进 `作业代码/第1周_Python核心基础/`，日志进 `学习日志/第1周/`。

| 天 | 代码 | 日志 | 是否已提交 |
|---|---|---|---|
| 周一 | `day1_basics.py` | `2026-10-12_周一.md` | □ |
| 周二 | `day2_functions.py` | `2026-10-13_周二.md` | □ |
| 周三 | `day3_exceptions.py` | `2026-10-14_周三.md` | □ |
| 周四 | `day4_modules.py` + `day4_math_tools.py` + `day4_main.py` | `2026-10-15_周四.md` | □ |
| 周五 | `day5_builtins_sqlite.py` | `2026-10-16_周五.md` | □ |
| 周六 | `todo_project/` 整个文件夹 + `todo_test_checklist.txt`（都放代码目录） | `2026-10-17_周六.md` | □ |

> 记得：`venv/` 和 `*.db` 不提交（已在 .gitignore 里）。
