cd /home/ubuntu/MyCodeProject/EE_Django

# 执行git pull命令，并将输出重定向到一个日志文件
echo "---------- Pulling on $(date) ----------" >> /home/ubuntu/MyCodeProject/EE_Django/Server_log/pull_log.txt
git pull >> /home/ubuntu/MyCodeProject/EE_Django/Server_log/pull_log.txt 2>&1
