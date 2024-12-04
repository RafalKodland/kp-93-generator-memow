# Import
from flask import Flask, render_template, request, send_from_directory


app = Flask(__name__)

# Formularz z rezultatami
@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        # odczytywanie wybranego obrazka
        selected_image = request.form.get('image-selector')

        # Zadanie #2. Odczytywanie tekstu
        top_text = request.form.get('textTop')
        bottom_text = request.form.get('textBottom')

        # Zadanie #3. Odczytywanie pozycji tekstu
        selected_color = request.form.get('color-selector')

        # Zadanie #3. Odczytywanie koloru tekstu
        

        return render_template('index.html', 
                               # Wyświetlanie wybranego obrazka
                               selected_image = selected_image, 

                               # Zadanie #2. Wyświetlanie tekstu
                               top_text = top_text,
                               bottom_text = bottom_text,

                               # Zadanie #3. Wyświetlanie koloru
                               selected_color = selected_color
                               
                               # Zadanie #3. Wyświetlanie pozycji tekstu

                               )
    else:
        # Wyświetlanie pierwszego obrazka, jako grafika domyślna
        return render_template('index.html', selected_image='logo.svg')


@app.route('/static/img/<path:path>')
def serve_images(path):
    return send_from_directory('static/img', path)

app.run(debug=True)
