from flask import Flask, request, redirect, url_for

app = Flask(__name__)

# Define a dictionary of valid users and passwords
users = {
    "admin": "admin@123"    
}

# Define the first page that takes username and password
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username] == password:
            return redirect(url_for('input'))
        else:
            return "Invalid username or password"
    return '''
        <form method="post">
            <p>Username: <input type="text" name="username"></p>
            <p>Password: <input type="password" name="password"></p>
            <p><input type="submit" value="Login"></p>
        </form>
    '''

# Define the second page that takes user inputs
@app.route('/input', methods=['GET', 'POST'])
def input():
    if request.method == 'POST':
        input1 = request.form['region']
        input2 = request.form['ipcount']
        #input3 = request.form['input3']
        # Call a Python script with the user inputs
        # Replace this with your own script
        output = my_python_script(input1, input2)
        return "Output: {}".format(output)
    return '''
        <form method="post">
            <p>
            <label for="region" name="optns"><b>Choose any one region : </b></label>
            <select name="region" id="opts">
                <option value="none" name="na">None</option>
                <option value="central india" name="ci">Central India</option>
                <option value="south india" name="si">South India</option> 
            </select>
            </p>    
            <p>Number of IPs required ? : <input type="text" name="ipcount"></p>
            <p><input type="submit" value="Submit"></p>
        </form>
    '''

# Replace this function with your own Python script
def my_python_script(region, ipcount):
    #op = region + " | " + input2 + " | " + input3
    output = "You selected " + region + " region and " + ipcount + " ips!!!" 
    return output

if __name__ == '__main__':
    app.run(debug=True)
