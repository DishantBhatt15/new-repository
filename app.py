from flask import Flask, render_template, request
from text_summary import summarizer

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    summary = None
    len_orig_txt = None
    len_summary = None
    if request.method == 'POST':
        rawtext = request.form['rawtext']
        summary, _, len_orig_txt, len_summary = summarizer(rawtext)
    return render_template('index.html', summary=summary, len_orig_txt=len_orig_txt, len_summary=len_summary)

if __name__ == "__main__":
    app.run(debug=True)
