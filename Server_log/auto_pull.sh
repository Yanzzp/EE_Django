cd /home/ubuntu/MyCodeProject/EE_Django

# 打印当前的日期并追加到日志文件
echo "---------- Pulling on $(date) ----------" >> /home/ubuntu/MyCodeProject/EE_Django/Server_log/pull_log.txt

# 执行git fetch命令，并将输出重定向到日志文件
git fetch >> /home/ubuntu/MyCodeProject/EE_Django/Server_log/pull_log.txt 2>&1

# 硬重置到远程主分支，并将输出重定向到日志文件
git reset --hard origin/main >> /home/ubuntu/MyCodeProject/EE_Django/Server_log/pull_log.txt 2>&1

