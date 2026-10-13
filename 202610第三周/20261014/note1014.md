周三（10月14日）：异常处理

一、异常的结构
    try-except-else-finally
    当认为本段代码会出错时，可以使用异常处理这段代码，使整个程序即使中间有错误也可以继续走；
    当一段代码中同时存在try|except|finally时，
    优先执行try，当try出现错误时，交给except进行处理；
    如果try没有错误，将执行else中的代码；
    无论程序有没有出错，都会执行finally中的代码。
二、主动抛出异常与自定义异常
    class 异常名(Exception):  # 定义一个异常类，必须继承于Exception类
        pass
    reise 异常名(异常信息)
    当代码出现的问题无法被python识别并处理时（如bmi值为负数，程序运行不会出错，但常识来讲有问题）可以使用raise主动抛出一个自定义异常并交给except处理；
    当然，也可以不处理让程序崩溃退出；