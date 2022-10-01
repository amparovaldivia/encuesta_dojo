from encuesta import app
from encuesta.controlers import controlador

app.secret_key="secreto"
if __name__=='__main__':
    app.run(debug=True)
    app.secret_key="nadie_sabe"