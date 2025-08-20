from flask import Flask, jsonify
import random

app = Flask(__name__)

@app.route('/points')
def get_points():
    num_points = random.randint(5, 10)
    points = [
        {'x': random.randint(50, 450), 'y': random.randint(50, 450)}
        for _ in range(num_points)
    ]
    centroid = {
        'x': sum(p['x'] for p in points) / num_points,
        'y': sum(p['y'] for p in points) / num_points
    }
    return jsonify({'points': points, 'centroid': centroid})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
