from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "message": "Welcome to the symbolic blurp-vault daemon.",
        "tags": ["modular", "poetic", "resilient"],
        "mood": "🌀 balanced"
    })

@app.route('/blurps/<fragment>')
def blurp(fragment):
    return jsonify({
        "fragment": fragment,
        "meaning": "symbolic resonance"
    })

@app.route('/mood')
def mood():
    return jsonify({
        "mood": "🌞 radiant",
        "message": "The daemon hums with clarity."
    })

if __name__ == '__main__':
    app.run()
