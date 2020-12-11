from flask import Flask, render_template, request
from flaskwebgui import FlaskUI
app = Flask(__name__)
ui = FlaskUI(app)

def str_to_binary(text):
    binary = ""
    for char in text:
        binary += format(ord(char), '08b')
    return binary
        
def binary_to_str(binary):
    #number of characters in text
    num = len(binary)/8 
    bit = ""
    for x in range(int(num)):
        start = x*8
        end = (x+1)*8
        bit += chr(int(str(binary[start:end]),2))
    return bit

@app.route("/", methods=["GET", "POST"])
def main():
    if request.method == "POST":
        myDict = request.form
        textarea = myDict["textarea"]
        userGiven = myDict["type"]
        if userGiven == "Text":
            result = str_to_binary(textarea)
        elif userGiven == "Binary":
            result = binary_to_str(textarea)
        return render_template("show.html", converterResult=result)
    return render_template("base.html")



if __name__ == "__main__":
    ui.run()