from flask import Flask, request
from dynamo_get import dynamo_get
from dynamo_put import dynamo_put
from datetime import datetime

app = Flask(__name__)
app.config["DEBUG"] = True
@app.route("/", methods=["GET", "POST"])

def runDynamo():
    d = datetime.now()
    errors = ""
    if request.method =="POST":
        if request.form['submit_button']=='Get Full Table':

            result = dynamo_get()
            f=open("audit.txt", "a+")
            f.write(str(d) + " - Full Table Get:" + result + "\n")

            return '''
            <html>
            <body>
            <p>DynamoDB Get Full Table:</p>
            <p>Table: </p>
            <p>======================</p>
            <h1>  {result}   </h1>
            <p>======================</p>
            <p><a href="/">Click here to return</p>
            </body>
            </html>
            '''.format(result=result)  #, question=question)
        put_request = request.form.get('put_request')
        if request.form['submit_button']=='Add Element':
            if put_request is not None:
                result = dynamo_put(put_request)
                f=open("audit.txt","a+")
                f.write(str(d) + " - " + put_request + "\n")
                print(put_request)
                return '''
            <html>
            <body>
            <p> You requested to add: {put_request} </p>
            <p>Table has been successfully updated</p>
            <p><a href="/">Click here to return</p>
            </body>
            </html>
            '''.format(result=result, put_request=put_request)

    return '''
    <html>
    <body>
    
    <h3>Click here to retrieve full table</h3>
    <form method="post" action=".">
    <p><input type="submit" name="submit_button" value="Get Full Table" /></p>

    <p>Enter below:</p>
    <form method="post" action=".">
    <p><input name="put_request" /></p>
    <p><input type="submit" name="submit_button" value="Add Element" /></p>
    </form>
    </body>
    </html>
    '''.format(errors=errors)
    
if __name__ == '__main__':
    app.run(debug=True, port=8080, host = '0.0.0.0')
