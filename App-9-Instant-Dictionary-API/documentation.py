from flask import Flask, render_template_string

app = Flask(__name__)


class Doc:
    path = "/about"

    @classmethod
    def serve(cls):
        return render_template_string("""
        <!DOCTYPE html>
        <html>
        <head>
            <title>About</title>
            <style>
                body {
                    background-color: #e5e7eb;
                    font-family: Arial, sans-serif;
                    padding: 30px;
                }
                h1 {
                    font-size: 40px;
                    margin-bottom: 10px;
                }
                p {
                    font-size: 20px;
                }
                hr {
                    margin: 20px 0;
                }
                pre {
                    background: white;
                    padding: 15px;
                    border-radius: 5px;
                    font-size: 16px;
                    overflow-x: auto;
                }
            </style>
        </head>
        <body>

            <h1>Instant Dictionary API</h1>

            <p>Get definitions of words:</p>

            <hr>

            <p>www.example.com/api?w=moon</p>

            <hr>

            <pre>{
                "word": "moon",
                "definition": [
                    "A natural satellite of a planet.",
                    "A month, particularly a lunar month (approximately 28 days).",
                    "To fuss over adoringly or with great affection.",
                    "Deliberately show one's bare ass.",
                    "To be lost in fantasies or be carried away by some internal vision."
                ]
            }</pre>

        </body>
        </html>
        """)

