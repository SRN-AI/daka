# daka
2
我在校园自动打卡（河北工程大学）
3
## 一、抓包获取token和session值
如：
Host: student.wozaixiaoyuan.com
Connection: keep-alive
Content-Length: 307
content-type: application/x-www-form-urlencoded
Cookie: [object Null]
### token: 9aaff489-523e-4001-b447-c7535c56c147
### JWSESSION: 15efddbfc4f245a9a40818847c8264bb
Accept-Encoding: gzip,compress,br,deflate
User-Agent: Mozilla/5.0 (iPhone; CPU iPhone OS 14_4_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.7(0x18000731) NetType/4G Language/zh_CN
Referer: https://servicewechat.com/wxce6d08f781975d91/173/page-

### 安卓可以用Httpcanary来抓，ios可以用stream
### win参考文章：https://www.cnblogs.com/liulinghua90/p/9109282.html 
## 二、修改app.json中的参数为你自己的参数
### 其中“token_p”为pushplus的token,注册后会生成，打卡成功后会推送消息
参考文章
https://blog.csdn.net/King_why_love/article/details/110860778?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522162587803916780261981685%2522%252C%2522scm%2522%253A%252220140713.130102334..%2522%257D&request_id=162587803916780261981685&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~top_click~default-2-110860778.first_rank_v2_pc_rank_v29&utm_term=%E6%88%91%E5%9C%A8%E6%A0%A1%E5%9B%AD&spm=1018.2226.3001.4187
## 三、执行
`python daka.py app.json`
更新token session
`python3 update.py app.json 你的token 你的session`

upd.sh和sigh.sh分别为更新token、session和执行打卡程序的shell脚本
