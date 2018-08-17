import sys
import telepot
from flask import Flask, request

try:
    from Queue import Queue
except ImportError:
    from queue import Queue

TOKEN = sys.argv[1]
CHANNEL = sys.argv[2]
app = Flask(__name__)
update_queue = Queue()
bot = telepot.Bot(TOKEN)
CHANNEL = sys.argv[2]


def on_chat_message(msg):
	content_type, chat_type, chat_id = telepot.glance(msg)
	if content_type == "document":
		file_id = msg['document']['file_id']
		bot.sendDocument(CHANNEL,file_id)

	elif content_type == "text":
		text = msg["text"].lower()
		if text.startswith("/start"):
			bot.sendMessage("Buongiorno.")
		elif text.startswith("/ping"):
			bot.sendMessage("Pong.")

@app.route('/', methods=['GET', 'POST'])
def pass_update():
	update_queue.put(request.data)
	return 'OK [200] HTTP CODE!!'


if __name__ == '__main__':
	app.run()
