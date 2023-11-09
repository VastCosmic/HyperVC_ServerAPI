# 获取文件目录，并启动Server
import os 
# 获取当前文件目录
path = os.path.abspath(os.path.dirname(__file__))
print(path)
# 启动Server
os.system("python " + path + "\Server\StartServer.py")
# 等待输入
input("Press Enter to continue...")
