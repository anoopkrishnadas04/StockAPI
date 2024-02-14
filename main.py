
import json
import requests
from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route('/?stock', methods=['GET'])
def get_info(number):
    return "Incremented number is " + str(number+1)

'''
@app.route('/<string:ticker>/<string:section>/')
def get_stock(ticker, section):
    #section: graph, table, news, short-tick (graph + table), all
    #"https://query1.finance.yahoo.com/v8/finance/chart/{}?region=US&lang=en-US&includePrePost=false&interval=2m&useYfid=true&range=1d&corsDomain=finance.yahoo.com&.tsrc=finance"

    return {"ticker":ticker, str(section):section}
'''

# allow both GET and POST requests
@app.route('/form-example', methods=['GET', 'POST'])
def form_example():
    # handle the POST request
    if request.method == 'POST':
        language = request.form.get('language')
        framework = request.form.get('framework')
        return '''
                  <h1>The language value is: {}</h1>
                  <h1>The framework value is: {}</h1>'''.format(language, framework)

    # otherwise handle the GET request
    return '''
           <form method="POST">
               <div><label>Language: <input type="text" name="language"></label></div>
               <div><label>Framework: <input type="text" name="framework"></label></div>
               <input type="submit" value="Submit">
           </form>
           '''

if __name__ == '__main__':
   app.run(port=5000)
