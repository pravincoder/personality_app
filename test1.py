import base64
from io import BytesIO
from flask import Flask
from matplotlib.figure import Figure

app = Flask(__name__)

@app.route("/submit")
def Output_graph():
    # Generate the figure **without using pyplot**.
    fig = Figure()
    ax = fig.subplots()
    ax.plot([1, 2])
    ax.set_title("A simple plot")
    ax.set_xlabel("X-axis")
    ax.set_ylabel("Y-axis") 
    # Save it to a temporary buffer.
    buf = BytesIO()
    fig.savefig(buf, format="png")
    # Embed the result in the html output.
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    return f"<img src='data:image/png;base64,{data}'/>"
