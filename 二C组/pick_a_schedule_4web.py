# -*- coding: utf-8 -*- 
# 使用模块moduld classtime


from flask import Flask, render_template, request, escape

app = Flask(__name__)

@app.route('/')
@app.route('/entry')

def entry_page() -> 'html':
    """Display this webapp's HTML form."""
    return render_template('entry.html',
                           the_title='欢迎来到网上查找中山大学南方学院艺创系与文传系课程情况！')


@app.route('/pick_a_schedule', methods=['POST'])
def pick_a_color() -> 'html':
	user_classtime_yuanxi= request.form['user_yuanxi']
	user_classtime_subject= request.form['user_subject']
	user_classtime_user_class= request.form['user_class']	
	with open('cleaned_data.tsv', 'r', encoding='utf8') as class_data:
		line = class_data.readlines()
	want_xy=[i for i in line if user_classtime_yuanxi in i]
	want_zy=[i for i in want_xy if user_classtime_subject in i]
	want_class=[i for i in want_zy if user_classtime_user_class in i]
	result_class=[]
	for i in range(len(set(want_class))):
		u=str(i+1)
		kechen=want_class[i].split('\t')[6]
		time_min=want_class[i].split('\t')[4]
		time_max=want_class[i].split('\t')[5]
		xuefen=want_class[i].split('\t')[8]
		zhoushi=want_class[i].split('\t')[9]
		qizhizhou=want_class[i].split('\t')[10]
		qizhizhou_divide=qizhizhou.split('-')
		qizhizhou_divide_1=qizhizhou_divide[0]
		qizhizhou_divide_2=qizhizhou_divide[1]
		jieguo='你筛选的课第'+u+'个有“'+kechen+'”，它从第'+qizhizhou_divide_1+'周开始到第'+qizhizhou_divide_2+'周结束，一周需要'+zhoushi+'个学时，共计'+xuefen+'个学分，人数下限为'+time_min+'人和上限为'+time_max+'人'
		result_class.append(jieguo)
		result_class=sorted(result_class)
		result_class_1=set(result_class)
		
	return render_template('results.html',
							the_title = '以下是您筛选后的课程：',
							the_classtime_code = result_class_1,
							the_classtime_yx_code =user_classtime_yuanxi,
							the_classtime_zy_code =user_classtime_subject,
							the_classtime_kc_code=user_classtime_user_class,
							)

if __name__ == '__main__':
    app.run(debug=True)
