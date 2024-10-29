from flask import Flask, Response
import json

app = Flask(__name__)
count = 0  # Лічильник запитів

@app.get("/count-requests")
def count_requests():
    global count
    count += 1
    return Response(json.dumps({"count": count}), content_type='application/json')

@app.post("/reset-counter")
def reset_requests():
    global count
    count = 0
    return Response(json.dumps({"count": count}), content_type='application/json')

if __name__ == '__main__':
    app.run(debug=True)