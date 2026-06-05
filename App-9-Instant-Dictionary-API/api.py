from urllib import response

from flask import Flask, request, jsonify
import definition
app = Flask(__name__)

class Api:

    @classmethod
    def serve(cls):
        """
        Handles requests at /api?w=word
        """
        word = request.args.get("w")
        defined = definition.Definition(word).get()

        response = {
            "word": word,
            "definition": defined
        }

        return jsonify(response)



if __name__ == "__main__":
    app.run(debug=True)