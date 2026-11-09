import logging

TRACE_LEVEL = 5 # 级别值
logging.addLevelName(TRACE_LEVEL, "TRACE") # 新增级别，值和名称

logger = logging.getLogger("aaa")
logging.basicConfig(level=TRACE_LEVEL)

logger.log(TRACE_LEVEL,"新增级别日志") # 根据级别值生成该级别的日志

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("aaa")

try:
    result = 1/0
except:
    logger.exception("出现了错误")
    

