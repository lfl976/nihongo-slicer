from flask import Flask, request, Response, jsonify
import MeCab

app = Flask(__name__)
mecab = MeCab.Tagger()


@app.route('/tokenize', methods=['GET'])
def tokenize():
    text = request.args.get('text')
    if not text:
        return jsonify({"error": "No text provided"}), 400
    result = mecab.parse(text)

    result = {
        "data": result
    }
    print(result)
    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)
