import flask
import qrcode

app = flask.Flask(__name__)

@app.route("/")
def home():
    

    return flask.render_template('qr_tool.html') 
    '''
    <!DOCTYPE html>

    '''
@app.route("/qr", methods=['POST'])
def qr():
# # 第一步，获取生成二维码的数据
    data = flask.request.args.get("data")

    # # 第二步，生成二维码图像
    img = qrcode.make(data)
    img.save(r"C:\Users\17161\Desktop\python代码\qr_tool_online\static\qr.png")

    # #第三步，在页面上显示二维码图片
    
    return '<img src="/static/qr.png"/>'


if __name__ == '__main__':
    app.run(debug=True)