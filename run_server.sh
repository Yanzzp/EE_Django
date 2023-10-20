PROJECT_DIR="/home/ubuntu/MyCodeProject/EE_Django"

# 虚拟环境路径
VENV_DIR="$PROJECT_DIR/venv"

# 日志文件位置
LOGFILE="$PROJECT_DIR/Server_log/logfile.log"

# 激活虚拟环境
source $VENV_DIR/bin/activate

# 切换到项目目录
cd $PROJECT_DIR

# 启动Django服务器
nohup python3 manage.py runserver 0.0.0.0:8002 > $LOGFILE 2>&1 &

# 打印服务器启动消息
echo "Django server started and listening on 0.0.0.0:8002!"
