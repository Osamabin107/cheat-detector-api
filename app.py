from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Cheat Detector API is running."

@app.route('/analyze', methods=['POST'])
def analyze_video():
    # In a real app, you'd run AI video analysis here
    # For now, just mock response
    video = request.files.get('video')
    if not video:
        return jsonify({"error": "No video uploaded"}), 400
    return jsonify({
        "cheats_detected": True,
        "cheat_types": ["aimbot", "wallhack"]
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
