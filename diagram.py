import flask
from flask import Flask, request
from werkzeug.wrappers import Request, response

app = Flask(__name__)

@app.route("/")
def render_mermaid_chart():
        html_content = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>API Flow Chart</title>
            <script type="module">
                import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid/dist/mermaid.esm.min.mjs';
                mermaid.initialize({{'theme': 'default'}});
            </script>
        </head>
        <body>
            <div class="mermaid">
                flowchart LR
                weather_api --> geocode_api --> openweather_api
            </div>
        </body>
        </html>
        """
        return html_content
    


if __name__ == "__main__":
  app.run(host='localhost', port=8100, debug=True)