
from flask import Flask, render_template
import random

app = Flask(__name__)

# list of cat images
images = [
 "https://bayonline.co.nz/wp-content/uploads/2016/10/4-ways-cheer-up-depressed-cat.jpg",
 "https://media.giphy.com/media/SgZtvjwcfq0ww/giphy-downsized-large.gif",
 "https://media.giphy.com/media/SgZtvjwcfq0ww/giphy-downsized-large.gif",
 "https://media.giphy.com/media/lIgaClvpJdGwg/giphy.gif",
 "http://www.cutecatgifs.com/wp-content/uploads/2014/08/slpy.gif",
 "http://www.catgifpage.com/gifs/237.gif"
]

@app.route('/')
def index():
    url = random.choice(images)
    return render_template('index.html', url=url)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
