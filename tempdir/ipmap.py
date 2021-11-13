import ipapi 
from flask import Flask, request, render_template

app = Flask(__name__)

#IP address information for which the user has searched
@app.route('/', methods = ['GET', 'POST'])
def Index():
    search = request.form.get('search') 
    data = ipapi.location(ip=search, output='json')
    return render_template('index.html', data=data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)