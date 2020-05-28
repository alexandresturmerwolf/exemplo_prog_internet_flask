from flask import Flask, render_template, session

app = Flask(__name__)
app.secret_key = 'sdafasjfsfksafsdafsad23583094'


@app.route("/pagina")
def pagina():
    session['nome'] = 'Juca'
    return render_template('base.html')
# enddef


@app.route('/')
def hello_world():
    variavel = " a vaca " + 'asdas'
    i = 0;
    while(i < 10 ):
        variavel = variavel + "ola"
        i = i + 1
    # endef

    return 'Hello da vaca!' + variavel * 5
# enddef


@app.route('/pega')
def pega():
    b = []

    a = {}
    a['chave'] = '123'
    a['nome'] = 'Juca'
    a['fone'] = '213213'

    b.append(a)

    a['chave'] = '456'
    a['nome'] = 'Marieta'
    a['fone'] = '2343'

    b.append(a)

    return str(b)


@app.route('/dados')
def dados():
    return '<html>' \
           '   <head>' \
           '      <title> minh apagina </title' \
           '   </head>' \
           '   <body>' \
           '        A vaca morreu <b> ontem </b>' \
           '   </body>' \
           '</html>'
# enddef


if __name__ == '__main__':
    app.run()
# endif