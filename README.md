# daka
我在校园自动打卡（河北工程大学）
## 一、抓包获取token和session值
如：<br/>
Host: student.wozaixiaoyuan.com<br/>
Connection: keep-alive<br/>
Content-Length: 307<br/>
content-type: application/x-www-form-urlencoded<br/>
Cookie: [object Null]<br/>
token: 9aaff489-523e-4001-b447-c7535c56c14<br/>
JWSESSION: 15efddbfc4f245a9a40818847c8264bb<br/>
Accept-Encoding: gzip,compress,br,deflate<br/>
User-Agent: Mozilla/5.0 (iPhone; CPU iPhone OS 14_4_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.7(0x18000731) NetType/4G Language/zh_CN<br/>
Referer: https://servicewechat.com/wxce6d08f781975d91/173/page-13<br/>

### 安卓可以用Httpcanary来抓，ios可以用stream
### win参考文章：https://www.cnblogs.com/liulinghua90/p/9109282.html 
## 二、修改app.json中的参数为你自己的参数
### 其中“token_p”为pushplus的token,注册后会生成，打卡成功后会推送消息
pushplus网址：http://www.pushplus.plus/

参考文章
## 三、执行
`python daka.py app.json`<br/>
更新token session<br/>
`python3 update.py app.json 你的token 你的session`<br/>

### upd.sh和sigh.sh分别为更新token、session和执行打卡程序的shell脚本，可以通过crontab设置定时任务来完成打卡<br/>
`./upd.sh 你的token session`<br/>

