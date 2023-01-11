from flask import Flask
from flask import send_file

app = Flask(__name__)

sampleFile = "Financial Sample.xlsx"


@app.route('/')
def hello():
    return 'Ok!', 200, {'Content-type': 'text/plain; charset=utf-8'}

@app.route('/download-1', methods = ['POST'])
def download_1():
  return send_file("./"+sampleFile, mimetype=None, as_attachment=False, etag=False), 200, {'Content-Disposition': 'attachment;filename="' + sampleFile +'"', 'Content-Type': 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet;;charset=ISO 8859-9'}


@app.route('/download-2', methods = ['POST'])
def download_2():
  return send_file("./"+sampleFile, mimetype=None, as_attachment=False, etag=False), 200, {'Content-disposition': 'attachment;filename="' + sampleFile +'"', 'Content-Type': 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet;;charset=ISO 8859-9'}


@app.route('/download-3', methods = ['POST'])
def download_3():
  return send_file("./"+sampleFile, mimetype=None, as_attachment=False, etag=False), 200, {'Content-disposition': 'attachment;filename="Vestas Wind System A-S TR Maliyet Raporu 31.10.2022.xlsx"', 'Content-Type': 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet;;charset=ISO 8859-9'}


@app.route('/download-4', methods = ['POST'])
def download_4():
  return send_file("./"+sampleFile, mimetype=None, as_attachment=False, etag=False), 200, {'Content-disposition': 'attachment;filename="Vestas Wind System A-S  TR Maliyet Raporu 31.10.2022.xlsx"', 'Content-Type': 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet;;charset=ISO 8859-9'}



if __name__ == "__main__":
    app.run(debug=False)