# 本教程只为了帮助那些因特殊原因（除流动）无法打卡，仅做学习交流使用，请勿传播谢谢
#
#
# daka
我在校园自动打卡（河北工程大学）河北工程大学我在校园自动打卡

## 工具
1. PC台式机一台
2. 微信
3. 任一浏览器
4. 如果使用云函数：腾讯云账号(实名认证)
## 一、获取session
session.exe输入我在校园的账号密码（账号为手机号，密码忘记了自行去修改，点重新登录然后左滑便可看见账号密码登录选项）获取session
如果改完显示密码错误，请确认我在校园用新密码登录成功
## 二、修改app.json中的参数为你自己的参数
纬度和经度百度可查，最好精度高一些，一般没事，位置不限制，但是有注释的部分一定要填
其中“token_p”为pushplus的token,注册后会生成，打卡成功后会推送消息
pushplus网址：http://www.pushplus.plus 进去后点一对一推送，微信扫码后可获取token
## 三、执行
#### 一.win：直接执行win.exe文件，可给电脑设置定时任务来完成每天的打开任务，具体百度。

#### 二：云函数（推荐，比较方便）：详细教程见链接http://www.gtr50.top/?p=1783
#### 三：linux
`python daka.py app.json`<br/>
更新token session<br/>
`python3 update.py app.json 你的token 你的session`<br/>

##### upd.sh和sigh.sh分别为更新token、session和执行打卡程序的shell脚本，可以通过crontab设置定时任务来完成打卡<br/>
`./upd.sh 你的token session`<br/

