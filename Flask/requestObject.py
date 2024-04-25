# Flask Application - request Object

from flask import Flask,request

app= Flask(__name__)
@app.route("/info")
def info():
    methods = request.method
    url = request.url
    headers = dict(request.headers)
    args = dict(request.args)
    form = dict(request.form)
    cookies = request.cookies
    is_json = request.is_json
    data = request.get_data(as_text=True)
    response_html = f'''
    <h1>Requested Data</h1>
    <p><strong>Methods : </strong> {methods}</p>
    <p><strong>URL : </strong> {url}</p>
    <p><strong>Headers : </strong> {headers}</p>
    <p><strong>Args : </strong> {args}</p>
    <p><strong>Form : </strong> {form}</p>
    <p><strong>Cookies : </strong> {cookies}</p>
    <p><strong>Is it json : </strong> {is_json}</p>
    <p><strong>Data : </strong> {data}</p>
    '''

    return response_html

app.run(port=5001)



