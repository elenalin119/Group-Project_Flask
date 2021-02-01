from flask import Flask, request, jsonify
import test as t
import pprint

app = Flask(__name__, static_url_path='/static', static_folder='./static')

@app.route('/test', methods=['GET', 'POST'])
def shopping_cart():
    outStr = """
    <html>
        <head>
            <link rel="icon" href="/static/images/wurenicon.ico" type="image/x-icon"/>      
            <title>Member_ID</title>
            <style>  
            .title{
                text-align:center;
                margin-top:50px;
                color:#FFFFFF;
            }
            .subtitle{
                color:#FFFFFF;
                font-size:18px;
            }
            .button{
              background-color: #921AFF;
              border: none;
              color: white;
              padding: 5px 10px;
              text-align: center;
              text-decoration: none;
              display: inline-block;
              font-size: 16px;
              margin: 3px 1px;
              cursor: pointer;
            }
            .input{
                padding:5px 15px; 
                border:2px #aaaaaa solid;
                cursor:pointer;
                -webkit-border-radius: 5px;
                border-radius: 5px; 
            }
            </style>
        </head>
        
        <body background='./static/images/1.jpg' style=" background-repeat:no-repeat;
                background-size:100% 100%;
                background-attachment: fixed;">
        
        <section>  
            <h1 class="title">請輸入會員ID號碼<p class="subtitle">( 號碼 1~2500 )</p></h1>
            <form style="text-align:center;margin-top:20px" action="/test" method="post">
                <input class="input" type="textbox" name="recommendation">
                <button class="button" type="submit">Submit</button>
            </form>
        </section>   
    """
    if request.method == 'GET':
        outStr += """
        </body>
    </html>
        """
    elif request.method == 'POST':
        tmp_output1 = ""
        user_input1 = request.form.get('recommendation')
        output1 = t.recommend_you(user_input1)
        for i in output1:
            tmp_output1 += '<p>'+str(i)+'</p>'
        outStr += """
        <div style="border:1px #aaa solid;padding:10px;margin:20px;text-align:center;color:#FFFFFF">
            %s
        </div>
        """%(tmp_output1)
        outStr += """
             </body>
        </html>       
         """
    return outStr

@app.route('/test2', methods=['GET','POST'])
def shopping_cart2():
    outStr = """
    <html>
        <head>
            <link rel="icon" href="/static/images/wurenicon.ico" type="image/x-icon" />
            <title>AI_Recommendation</title>
            <style>
            .title{
                text-align:center;
                margin-top:50px;
                color:#FFFFFF; 
            }
            .subtitle{
                color:#FFFFFF;
                font-size:18px;
            }
            .button{
              background-color: #921AFF;
              border: none;
              color: white;
              padding: 5px 10px;
              text-align: center;
              text-decoration: none;
              display: inline-block;
              font-size: 16px;
              margin: 3px 1px;
              cursor: pointer;
            }
            .input{
                padding:5px 15px; 
                border:2px #aaaaaa solid;
                cursor:pointer;
                -webkit-border-radius: 5px;
                border-radius: 5px; 
            }
            </style>
        </head>
        
        <body background='./static/images/4.jpg' style=" background-repeat:no-repeat;
                background-size:100% 100%;
                background-attachment: fixed;">
        
        <section>
            <h1 class="title">輸入商品子類別名稱</h1>
            <form style="text-align:center;margin-top:20px" action="/test2" method="post">
                <input class="input" type="textbox" name="recommendation">
                <button class="button" type="submit">Submit</button>
            </form>
        </section>
    """
    if request.method == 'GET':
        outStr += """
        </body>
    </html>
        """
    elif request.method == 'POST':
        tmp_output2 = ""
        ms = request.form.get('recommendation')
        a = t.others_also_like_by_product(ms)
        for j in a:
            tmp_output2 += '<p>'+str(j) + '</p>'
        outStr += """
          <div style="border:1px #aaa solid;padding:10px;margin:20px;text-align:center; color:#FFFFFF">
            %s
        </div>
        """%(tmp_output2)

        outStr += """
        </body>
    </html>
        """
    return outStr


if __name__ == '__main__':
    app.run(debug=True, port=5000)