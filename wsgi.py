import eventlet
eventlet.monkey_patch()  # ⚡ doit être tout en haut !

from main import app, socketio

# Expose une variable "app" pour gunicorn
app = app  

if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=8000)
