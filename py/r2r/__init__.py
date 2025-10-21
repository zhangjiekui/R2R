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


# R2R_CONFIG_PATH
os.environ['R2R_CONFIG_PATH']="/data/jqr2r/R2R/docker/user_configs/full_jq.toml"
# HATCHET_CLIENT_TOKEN可以在Hatchet-Dashboard界面的Settings面板中获取 https://docs.hatchet.run/home/setup
# 也可以在R2R容器hatchet.api_key/api_key.txt文件中获取
os.environ['HATCHET_CLIENT_TOKEN']="eyJhbGciOiJFUzI1NiIsImtpZCI6InQ3ZF81ZyJ9.eyJhdWQiOiJodHRwOi8vaG9zdC5kb2NrZXIuaW50ZXJuYWw6NzI3NCIsImV4cCI6NDkxMTUwMTQzOSwiZ3JwY19icm9hZGNhc3RfYWRkcmVzcyI6ImhhdGNoZXQtZW5naW5lOjcwNzciLCJpYXQiOjE3NTc5MDE0MzksImlzcyI6Imh0dHA6Ly9ob3N0LmRvY2tlci5pbnRlcm5hbDo3Mjc0Iiwic2VydmVyX3VybCI6Imh0dHA6Ly9ob3N0LmRvY2tlci5pbnRlcm5hbDo3Mjc0Iiwic3ViIjoiNzA3ZDA4NTUtODBhYi00ZTFmLWExNTYtZjFjNDU0NmNiZjUyIiwidG9rZW5faWQiOiIxMWEwNTk3ZS1hZGYwLTRkMjItYTM5ZS03YTA2Y2U1ODk1NzkifQ.L5OrXPbWZs8S6TWkrgfRZGTNLH3nzL87F4ouZQWdE1UlhPkQE13Pk-ybNWvfR7BI6FNcf9hAvWMqFZZ4MJXksw"
os.environ['HATCHET_CLIENT_HOST_PORT'] = "10.1.150.105:7077"
os.environ['HATCHET_CLIENT_TLS_STRATEGY']="none"
# 生成SSL证书和私钥的命令（在Linux或Mac终端中运行）：
# 步骤1：生成 Root CA 私钥
# openssl genrsa -out root_ca.key 2048
# 步骤2：生成自签名 Root CA 证书（这就是 root_ca.crt）
# openssl req -x509 -new -key root_ca.key -out root_ca.crt -days 3650 -subj "/CN=My Internal Root CA"
# 步骤3：生成客户端私钥和证书签名请求（CSR）
# openssl genrsa -out client.key 2048
# openssl req -new -key client.key -out client.csr
# 步骤4：用你自己的 CA 签发（假设有 root_ca.crt 和 root_ca.key）
# openssl x509 -req -in client.csr -CA root_ca.crt -CAkey root_ca.key -CAcreateserial -out client.crt -days 365

# 配置环境变量
# os.environ['HATCHET_CLIENT_TLS_CERT_FILE'] = "/data/jqr2r/sslkeyfile/client.crt"
# os.environ['HATCHET_CLIENT_TLS_KEY_FILE'] = "/data/jqr2r/sslkeyfile/client.key"
# os.environ['HATCHET_CLIENT_TLS_ROOT_CA_FILE'] = "/data/jqr2r/sslkeyfile/root_ca.crt"
# os.environ['HATCHET_CLIENT_TLS_STRATEGY']="tls"
    ### 但经测试，服务端并没有启用SSL：docker/env/hatchet.env中SERVER_GRPC_INSECURE=t 
    ### 如果启用，需做如下配置，但未实际测试
    #### SERVER_GRPC_INSECURE=f  # 关闭 insecure 模式 → 启用 TLS
    #### SERVER_TLS_CERT_FILE=/path/to/server.crt
    #### SERVER_TLS_KEY_FILE=/path/to/server.key
    #### SERVER_TLS_CLIENT_CA_FILE=/path/to/root_ca.crt  # 如果启用 mTLS（客户端证书验证）
    ###
# 所以此处不使用TLS加密连接，设置为"none"
os.environ['HATCHET_CLIENT_TLS_STRATEGY']="none"
# 验证的代码逻辑：/root/.virtualenvs/test/lib/python3.10/site-packages/hatchet_sdk/connection.py

__version__ = metadata.version("r2r")  # type: ignore


__all__ = [
    "R2RAsyncClient",
    "R2RClient",
    "env_models_instance",
    "__version__",
    "R2RException",
] + shared_all


def get_version():
    return __version__
