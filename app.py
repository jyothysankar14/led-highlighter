import json
from flask import Flask, request, jsonify
import board
import neopixel

# Setup LED strip
NUM_LEDS = 30  # Set according to your setup
pixels = neopixel.NeoPixel(board.D18, NUM_LEDS, auto_write=False)

# Load database
with open('database.json') as f:
    book_db = json.load(f)

# Flask app
app = Flask(__name__)

# Define unique color codes
COLOR_CODES = {
    "signals": (255, 0, 0),
    "lic": (0, 255, 0),
    "control": (0, 0, 255),
    "microwaves": (255, 255, 0),
    "wireless": (255, 0, 255)
}

@app.route('/highlight', methods=['POST'])
def highlight():
    data = request.json
    book_name = data.get("book")
    
    if book_name in book_db:
        index = book_db[book_name]["led_index"]
        subject = book_db[book_name]["subject"]
        color = COLOR_CODES.get(subject, (255, 255, 255))

        # Clear and light specific LED
        pixels.fill((0, 0, 0))
        pixels[index] = color
        pixels.show()
        return jsonify({"status": "success", "message": f"LED {index} highlighted."}), 200
    else:
        return jsonify({"status": "error", "message": "Book not found."}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
