import os
from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/dat', methods=['POST'])
def dat():
    checklist = {
        'color': 'green',
        'message': (
            '''
Have we met the acceptance criteria of the user story?
Is the code easy enough to read (naming, comments, ...)?
Are there any potential security issues?
Are we logging or storing any sensitive data? If so, how are we protecting it?
Are there any race conditions? If so, they are:
Are there any potential performance issues?
Does the code adhere to our style guide?
Is the code/architecture consistent with the rest of the code?
Have all code review comments been addressed?
Does the code adhere to accessibility best practices?'''
        ),
        'notify': False,
        'message_format': 'text'
    }

    return jsonify(**checklist)


@app.route('/')
def hello():
    return 'Hello World!'


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
