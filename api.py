from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <title>TikTok Downloader API 🚀</title>
        <style>
            body {
                background: #0f172a;
                color: #f8fafc;
                font-family: monospace;
                padding: 20px;
            }
            pre {
                background: #1e293b;
                padding: 15px;
                border-radius: 8px;
                overflow-x: auto;
                box-shadow: 0 2px 8px rgba(0,0,0,0.5);
            }
            .key { color: #38bdf8; }
            .string { color: #f472b6; }
        </style>
    </head>
    <body>
        <h2>TikTok Downloader API 🚀</h2>
        <p>Base URL: <code>/api/tiktok?url=TIKTOK_URL</code></p>
        <h3>Example Response:</h3>
        <pre>{
  <span class="key">"message"</span>: <span class="string">"TikTok Downloader API 🚀"</span>,
  <span class="key">"status"</span>: <span class="string">"online"</span>,
  <span class="key">"usage"</span>: <span class="string">"/api/tiktok?url=TIKTOK_URL"</span>,
  <span class="key">"author"</span>: <span class="string">"Always Zycho"</span>
}</pre>
    </body>
    </html>
    """

@app.route('/api/tiktok')
def tiktok_dl():
    url = request.args.get("url")
    if not url:
        return jsonify({"error": "URL is required"})
    return jsonify({
        "status": "success",
        "url": url,
        "download": {
            "mp4": "https://example.com/video.mp4",
            "mp3": "https://example.com/audio.mp3"
        }
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
