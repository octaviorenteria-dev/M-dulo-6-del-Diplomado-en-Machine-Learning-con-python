from flask import Flask, render_template, request
from transformers import pipeline

from queue import Queue
from time import sleep
import threading

from pathlib import Path



def process():
    global in_queue, out_queue

    model = pipeline("image-classification", model="microsoft/resnet-50")
    while True:
        url = in_queue.get()
        results = model(url)
        out_queue.put(results[0])
        sleep(1)

thread = threading.Thread(target=process)
thread.start()
in_queue = Queue()
out_queue = Queue()

app = Flask(__name__)

@app.route("/")
def root():
    
    root_path = Path(__file__).absolute().parent
    img_path = Path(f'{root_path}/static/images')
    images = sorted([f'<option value="{p.name}">{p.name}</option>' for p in img_path.rglob('*.jpg')])
    images = "\n".join(images)

    src = render_template('template.html')

    listbox = F'''<label for="images">Choose an option:</label>
            <select id="images" onchange="updateImage();">
            {images}
            </select>'''
    return src.replace('<body>','<body>'+listbox)

@app.route('/inference', methods=['POST'])
def inference():
    global in_queue, out_queue
    data = request.get_json()

    in_queue.put(data['image'])
    result = out_queue.get()    
    return result
