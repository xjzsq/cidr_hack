# 基于Fiddler的cdr辅助  
### 使用教程
0. 安装python3
1. 配置fiddler，导入脚本并保存
2. 解压answer.7z(把answer.txt和python脚本放在一个目录下)
3. 运行cdr.py脚本
4. 开心地背单词吧

### 详细配置步骤
0. 安装python3  
下载页：https://www.python.org/downloads/  
1. 配置fiddler
下载地址：http://s.xjzsq.ren/x/fd.zip  
下载后点右上位置的FiddlerScript按钮，然后把所有脚本删掉，替换为fiddler_script.js的内容，之后**点击Save Script按钮**保存脚本
参考这篇文章：https://blog.csdn.net/gld824125233/article/details/52588275  
注意事项：
- 一定注意用管理员身份运行fiddler  
- 默认监听端口建议改为558，改了之后手机安装证书的地址也要改为ip:558  
- 一定要让你的手机和电脑在一个网络下
- ip查询步骤：  
	- win+r  
	- 输入cmd并回车  
	- 弹出的窗口中输入ipconfig并回车
	- 有线就是以太网，无线就是无线局域网适配器，找到IPv4 地址一项，如果有多个就一个一个试，再不行私信我
	- 替换好fiddler_script之后一定要记得点击Save Script保存
2. 解压answer.7z到当前文件夹，和python脚本放一起，不要放在子文件夹内  
3. 打开词达人，然后运行cdr.py脚本  
4. 开心地背单词吧~	 