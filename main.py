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

    print(f'Client 2 - Value from Memcached: {result}')

    # HTML-formatted text
    html_text = f"<h1>Hello, Feature flag 1! Is there a key here {result}</h1><p>This is a sample HTML-formatted text.</p>"
    html_text2 = "<h1>Hello, Feature flag 2!</h1><p>This is a sample HTML-formatted text.</p>"

    # Render the HTML template
    # if feature_flag:
    #     return render_template('index.html', html_text=html_text1)
    # else:
    #     return html_text2
    return html_text


if __name__ == '__main__':
    app.run(debug=True)
