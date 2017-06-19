### 进程线程协程

数据库操作与Paramiko模块

paramiko主要用于远程ssh连接服务器进行批量管理操作

SSH 有scp命令可以传文件 scp是基于ssh的sftp协议

`scp -rp -P22 temp.txt root@10.0.0.41:/tmp/` r为如果是目录拷贝目录 p为permission拷贝权限至远程机器

top, vim 不能返回, top -bn


#### ssh 密钥
> 不通过明文用户名密码 使用RSA非对称密钥加密 自动连接远程机器

公钥 public key
私钥 private key
A: 10.0.0.31(持有A公钥) ---> B: 10.0.0.41 (持有A私钥)

生成密钥对 `ssh -keygen`



