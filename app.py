from flask import Flask, render_template

app = Flask(__name__)

@app.route('/email/<template_name>')
def render_email_template(template_name):
    return render_template(f'{template_name}.html')

if __name__ == '__main__':
    app.run(debug=True, port=8000)
