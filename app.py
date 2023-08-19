from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

openai.api_key = "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"

@app.route('/get_response', methods=['POST'])
def get_response():
    data = request.get_json()
    user_message = data['user_message']

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": user_message}
        ]
    )

    response = completion.choices[0].message['content']
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
