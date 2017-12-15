# 两个脚本实现修改md5和文件名
- rename.py 去除文件名内的空格，并在每个字符间添加符号，实现防止关键字搜索
- change_md5.sh 在文件末尾追加字节，修改md5，同时不影响文件的正常打开。

## 使用方法
1. 在命令行界面输入`python3 rename.py /Users/test`，/Users/test是目标文件目录，将自己的目录换上去；
2. 在命令行界面输入`sh change_md5.sh ` ，/Users/test是目标文件目录，将自己的目录换上去。


## 注意
请先执行rename.py，然后执行change_md5.sh



