# ---------------------- Assignment Web Caesar ------------------------

from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
                }}

            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
                font-size: 20px;
            }}
        </style>
    </head>
    <body>
      <form method='POST'>
        <label for='rot'>Rotate by</label>
        <input id='rot' type='text' name='rot' value='0' />
        <textarea name='text'>{0}</textarea>
        <input type='submit' />

      </form>
    </body>
</html>
"""

# display form when first opening.
@app.route("/")
def index():

    return form.format("")


# handle the info from the form
@app.route("/", methods=['POST'])
def encrypt():
    
    # get the values from the form. use syntax like you would to get a Dictionary value.
    rotate = int(request.form['rot'])  # use int() to convert string to integer.
    message = request.form['text']

    encrypt_message = rotate_string(message,rotate)

    return form.format(encrypt_message)   # places the encrypted message inside the placeholder inside the textarea field.

app.run()