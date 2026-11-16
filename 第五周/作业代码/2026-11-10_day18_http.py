# 导入 requests 库。它是第三方 HTTP 客户端，用来发 GET、POST 等请求。
# 使用前需要先安装：pip install requests
import requests

# 向 JSONPlaceholder 的公开测试接口发一个 GET 请求，获取 id 为 1 的待办事项。
# requests.get() 会阻塞等待服务器响应，然后返回一个 Response 对象，赋给变量 r。
r = requests.get("https://jsonplaceholder.typicode.com/todos/1")

# 打印 HTTP 状态码。这条资源存在，正常情况下是 200（成功）。
# r.status_code 是整数，例如 200、404、500。
print("状态码：", r.status_code)

# r.json() 把响应体按 JSON 解析成 Python 字典（或列表）。
# 这条接口返回的大致是：{"userId": 1, "id": 1, "title": "...", "completed": false}
# 如果响应体不是合法 JSON，这里会抛出异常。
print("响应体：", r.json())

# 再发一次 GET，这次请求 id 为 999999 的待办事项。该 id 在测试数据里不存在。
# 写法与上面相同，只是 URL 末尾的数字不同。
r2 = requests.get("https://jsonplaceholder.typicode.com/todos/999999")

# 打印第二次请求的状态码。资源不存在时，服务器通常返回 404（Not Found）。
# 请求本身是成功发出并收到响应的；404 表示“没找到这条数据”，不是网络错误。
print("状态码：", r2.status_code)