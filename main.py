from flask import Flask, render_template

app = Flask(__name__)

feature_flag = False


@app.route('/')
def index():
    from pymemcache.client import base

    client = base.Client(('localhost', 11211))  # Replace with your Memcached server address

    key = 'feature_flag'

    # Retrieve the value set by Client 1
    result = client.get(key)

    data_string = result.decode('utf-8')

    print(f'Client 2 - Value from Memcached: {data_string}')

    html_text = ""

    # HTML-formatted text

    if data_string == "flag1":
        html_text = f"<h1>Hello, Feature flag 1! Is there a key here {data_string}</h1>"
    elif data_string == "flag2":
        html_text = f"<h1>Hello, Feature flag 2! Look at this {data_string}</h1>"
    else:
        html_text = f"<h1>Hello, uh-oh! No or wrong flags have been set</h1>"

    # Render the HTML template
    # if feature_flag:
    #     return render_template('index.html', html_text=html_text1)
    # else:
    #     return html_text2
    return html_text


if __name__ == '__main__':
    app.run(debug=True)
