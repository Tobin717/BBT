from app import app
from flask import request, session
from database import findUser, createUser, userLogin

@app.route('/rzt/regist', methods=['POST'])
def register():
    data = request.get_json()
    username = data['username']
    password = data['password']

    result = findUser(username)
    if result:
        return {
            'errcode': 400,
            'errmsg': '该用户名已被注册'
        }, 400
    
    rowcount = createUser(username, password)
    if rowcount > 0:
        return {
            'errcode': 0,
            'errmsg': '注册成功'
        }, 200
    
    return {
        'errcode': 400,
        'errmsg': '出现错误~请重试'
    }, 400

@app.route('/rzt/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data['username']
    password = data['password']

    result = userLogin(username, password)
    
    if result:
        session['user_id'] = result[0]
        return {
            'errcode': 0,
            'errmsg': '登陆成功'
        }, 200
    
    return {
        'errcode': 401,
        'errmsg': '用户不存在或密码错误'
    }, 401
