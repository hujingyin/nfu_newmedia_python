pick_a_schedule_4web.py

# 简介 
我们用pandas读xls文档，把读好的整个资料筛选出，然后把想要的资料写入和读入一个新的tsv文档，把tsv文档供webapp使用，其中我们也用到了把tsv转化为csv。
		

## 输入：
用户输入变数1:课程内容（型态：下拉）
## 输出：
用户得到输出结果为：上限人数
## 从输入到输出，本组作品使用了：
### 模块
* [tsv](http://www.52ij.com/jishu/python/12449.html)
* [csv](http://www.cnblogs.com/nisen/p/6155492.html)
*[pandas](http://www.jb51.net/article/63216.htm)
*[pandas读xls](http://www.cnblogs.com/lhj588/archive/2012/01/06/2314181.html)
### 数据
* 老师提供的xls文档课程表
### API
## Web App动作描述

以下按web 请求（web request） - web 响应 时序说明

1. 後端伺服器启动：执行 pick_a_schedule_4web.py 启动後端伺服器，等待web 请求。启动成功应出现：  * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

2. 前端浏览器web 请求：访问 http://127.0.0.1:5000/ 启动前端web 请求

3. 後端伺服器web 响应：[pick_a_ schedule_4web.py]( pick_a_ schedule_4web.py) 中 执行 了@app.route('/') 下的 entry_page()函数，以HTML模版[templates/entry.html](templates/entry.html)产出的产生《欢迎来到网上查文学与传媒系与艺创系课程表！》的HTML页面

4. 前端浏览器收到web 响应：出现HTML页面有HTML表单的输入 input 类型(type) 为"select"，变数名称(name)为user_yuanxi 'user_subject 'user_class”,详见HTML模版[templates/entry.html](templates/entry.html)

5. 前端浏览器web 请求：用户选取指标後按了提交钮「搞吧」，则产生新的web 请求，按照form元素中定义的method='POST' action='/pick_a_schedule '，以POST为方法，动作为/pick_a_schedule的web 请求

6. 後端服务器收到用户web 请求，匹配到@app.route('/pick_a_schedule', methods=['POST'])的函数 pick_a_schedule() 

7. [pick_a_schedule_4web.py.form[user_yuanxi 'user_subject 'user_class]	取到Web 请求中，HTML表单变数名称user_yuanxi 'user_subject 'user_class的值，存放在user_yuanxi 'user_subject 'user_class这Python变数下，再使用flask模块render_template 函数以[templates/results.html](templates/results.html)模版为基础（输出）

8. 前端浏览器收到web 响应：模版中[templates/results.html](templates/results.html) 的变数值正确的产生的话，前端浏览器会收到正确响应，看到指标的相关元数据。




## 作者成员：
见[_team_.tsv](https://github.com/hujingyin/nfu_newmedia_python/blob/master/%E4%BA%8CC%E7%BB%84/_team_/_team_.tsv)
