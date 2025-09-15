import sys,os
from importlib import metadata

JQCODE_PATH = fr"/data/projects/JqChatV2/JqChat"
sys.path.append(str(JQCODE_PATH))
from jqcode.jq_utils.logger import jqkj_logger
logger = jqkj_logger(__file__).get_logger()
logger.warning(f"已在R2R/py/r2r/__init__.py文件中直接将{JQCODE_PATH}添加到sys.path中")
try:
    from jqcode.jq_agent.c0_init_env_models import env_models_instance
    # from jqcode.jq_readers.jqkj_readers import JqkjDocxReader
    # from jqcode.jq_splitters.jq_docx_tree_text_splitter import JqkjDocTreeTokenTextSplitter
    # from jqcode.jq_splitters.backend_splitter_utils.jq_chinese_recursive_text_splitter import JqkjChineseRecursiveTextSplitter
    logger.warning(f"已成功导入Jqcode包中的相关模块，如env_models_instance")
except ImportError as e:
    logger.error(f"无法导入Jqcode包中的相关模块，如env_models_instance: {e}")


from sdk.async_client import R2RAsyncClient
from sdk.sync_client import R2RClient
from shared import *
from shared import __all__ as shared_all

# HATCHET_CLIENT_TOKEN可以在Hatchet-Dashboard界面的Settings面板中获取 https://docs.hatchet.run/home/setup
os.environ['HATCHET_CLIENT_TOKEN']="eyJhbGciOiJFUzI1NiIsImtpZCI6InQ3ZF81ZyJ9.eyJhdWQiOiJodHRwOi8vaG9zdC5kb2NrZXIuaW50ZXJuYWw6NzI3NCIsImV4cCI6NDkxMTUwMTQzOSwiZ3JwY19icm9hZGNhc3RfYWRkcmVzcyI6ImhhdGNoZXQtZW5naW5lOjcwNzciLCJpYXQiOjE3NTc5MDE0MzksImlzcyI6Imh0dHA6Ly9ob3N0LmRvY2tlci5pbnRlcm5hbDo3Mjc0Iiwic2VydmVyX3VybCI6Imh0dHA6Ly9ob3N0LmRvY2tlci5pbnRlcm5hbDo3Mjc0Iiwic3ViIjoiNzA3ZDA4NTUtODBhYi00ZTFmLWExNTYtZjFjNDU0NmNiZjUyIiwidG9rZW5faWQiOiIxMWEwNTk3ZS1hZGYwLTRkMjItYTM5ZS03YTA2Y2U1ODk1NzkifQ.L5OrXPbWZs8S6TWkrgfRZGTNLH3nzL87F4ouZQWdE1UlhPkQE13Pk-ybNWvfR7BI6FNcf9hAvWMqFZZ4MJXksw"
__version__ = metadata.version("r2r")  # type: ignore


__all__ = [
    "R2RAsyncClient",
    "R2RClient",
    "__version__",
    "R2RException",
] + shared_all


def get_version():
    return __version__
