#Flask Application - Set and display response attributes
from flask import Flask,request,make_response
app=Flask(__name__)
@app.route("/status")
def status():
    response=make_response("Status Code and Headers")
    response.status_code=200
    response.headers['Custom_Header']='Custom Value'
    return response
@app.route("/setcookie")
def set_cookie():
    username = request.cookies.get('username')
    response=make_response("Cookie set!!")
    response.set_cookie('username','abc')
    response_content=f'username from cookie is {username}'
    response.set_data(response_content)
    return response
@app.route("/showcookie")
def showcookie():
    username = request.cookies.get('username')
    '''username = request.cookies.get('username')
    if username:
        return f'Cookie {username} has been set'
    else:
        return 'Cookie not found' '''
    return f'Cookie {username} has been set'
@app.route("/deletecookie")
def delete_cookie():
    response=make_response("Cookie deleted")
    response.delete_cookie('username')
    return response
@app.route("/content")
def content():
    response=make_response("Content with custom length and type")
    response.content_length=len(response.get_data())
    response.content_type='text/plain'
    response_content=f'Content is {response.content_length},\
                     Content type is {response.content_type}'
    response.set_data(response_content)
    return response
@app.route("/data",methods=['POST','GET'])
def data():
    if request.method=='POST':
        data=request.form['data']
        response=make_response("Data received")
        response.set_data(data.encode('utf-8'))
        return response
    else:
        data=request.get_data(as_text=True)
        return f'Recieved data is {data}'

@app.route("/display")
def display():
    username=request.cookies.get('username')
    #con_len= response.content_length
    #con_type= response.content_type
    status_code=200
    response=make_response('Displaying attributes of requests')
    if hasattr(response,'status_code'):
        status_code=response.status_code
    response_content=(f'Username from cookie is {username},\
                      Status code is{status_code},'
                      ) #Content length {con_len},\
                      #Content type {con_type}
    response.set_data(response_content)
app.run(port=5005)
