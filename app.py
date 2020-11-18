from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient  # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)

app = Flask(__name__)

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta  # 'dbsparta'라는 이름의 db를 만들거나 사용합니다.


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/tools', methods=['GET'])
def showArticles():
    # 1. db에서 tools 목록 전체를 검색합니다.
    tools = list(db.tools.find({}, {'_id':False}).sort('likes', -1))

    for tool in tools:
        tool_id = tool['id']
        likes_list = db.tools_comment.find({ 'like': 'true', 'tool_id': str(tool_id) })
        likes_list = list(likes_list)
        likes = len(likes_list)
        tool['likes'] = likes
    tools = sorted(tools, key=lambda x: -x['likes'])

        # 2. 성공하면 success 메시지와 함께 tools 목록을 클라이언트에 전달합니다.

    return  jsonify({'result': 'success', 'tools': tools})

@app.route('/evaluation', methods=['GET'])
def onclickShowEvaluation():
    id = request.args.get('id')
    tools_comment = list(db.tools_comment.find({'tool_id': id}, {'_id': False}))
    return jsonify({'result': 'success', 'tools_comment': tools_comment})


@app.route('/tools', methods=['POST'])
def postArticles():
    # 1. 클라이언트로부터 데이터를 받기
    grade_receive = request.form['grade_give']
    comment_receive = request.form['comment_give']
    tool_id_receive = request.form['tool_id_give']
    like_receive = request.form['like_give']

    # 2. mongoDB에 데이터 넣기
    doc = {
        'tool_id': tool_id_receive,
        'grade' : grade_receive,
        'comment' : comment_receive,
        'like' : like_receive
    }
    db.tools_comment.insert_one(doc)

    return jsonify({'result': 'success', 'msg': '저장이 완료되었습니다!'})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)