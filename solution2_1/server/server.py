#!/usr/bin/python3

from flask import Flask, request
from mylib import solution


app = Flask(__name__)



@app.route('/', methods = ['GET'] )
def hello_world():
    return 'Hello, world!\n'

# this does not stop docker though
@app.route('/stop', methods = ['GET'] )
def stopping():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()
    return 'Goodbye, world!\n'

# route /calculate to this function
@app.route('/calculate', methods = ['GET', 'POST'])
def handle():
    ''' 
    A single connection handler
    '''
    # handling one request
    try:
        if request.method == 'GET':
            return '''
              <form method="POST">
                  <div><label>Data: <input type="text" name="data"></label></div>
                  <input type="submit" value="Submit">
              </form>'''
        if request.method == 'POST':
            try:
                data = request.form.get('data')
                if data is None:
                    raise KeyError
            except KeyError:
                print("Error: No data provided")
                return 'Error: No data provided'
        print("Calculation request: {}".format(data))
    
            
        # data should be a string with a problem, encoded in utf-8
        # client removes '&' symbols
        ans = solution.calculate(data)
        if (not isinstance(ans, str)):
            ans = str(ans)
            print("Server answer: " + ans)

            # send result back with a request for next problem
            return "Server answer: {}\n".format(ans)
        else:
            print("Calculation failed:\n{}".format(ans))
            return "Calculation failed:\n{}".format(ans)
            
    except Exception:
        raise

def main():
    print("server starting")
    app.run(debug=True, port=5000)

if __name__ == "__main__":
    main()