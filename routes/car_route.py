import os
from datetime import datetime
from flask import Blueprint, render_template, request, jsonify
from werkzeug.utils import secure_filename
from services.car_services import create_car, list_car, delete_car, show_car, update_car, found_image

cars = Blueprint('cars', __name__)


@cars.route('/')
def index():
    cars = list_car()
    return render_template('car/index.html', cars=cars)


@cars.route('/add', methods=['POST'])
def create():
    if request.method == 'POST':
        brand = request.form['brand']
        model = request.form['model']
        color = request.form['color']
        year = request.form['year']
        doors = request.form['doors']
        favorite = request.form['favorite'] == '1'
        cylinder_capacity = request.form['cylinder_capacity']
        velocity = request.form['velocity']
        photo = request.files['photo']

        if photo == None:
            return 'Please, enter image'
        else:
            original_filename = secure_filename(photo.filename)
            filename = set_image(original_filename)
            
            create_car(brand, model, year, doors, favorite,
                       filename, color, cylinder_capacity, velocity)
            save_image(filename, photo)
            return jsonify({'message': 'Car Created!'})


@cars.route('/edit/<int:id>')
def show(id):
    car = show_car(id)
    return jsonify(car.to_json())


@cars.route('/update/<int:id>', methods=['POST'])
def update(id):
    if request.method == 'POST':
        brand = request.form['brand']
        model = request.form['model']
        color = request.form['color']
        year = request.form['year']
        doors = request.form['doors']
        favorite = request.form['favorite'] == '1'
        cylinder_capacity = request.form['cylinder_capacity']
        velocity = request.form['velocity']
        photo = request.files['photo']

        if photo.filename == '':
            update_car(id, brand, model, year, doors, favorite,
                       None, color, cylinder_capacity, velocity)
            return jsonify({'message': 'Car Updated!'})
        else:
            original_filename = secure_filename(photo.filename)
            filename = set_image(original_filename)
            old_image = found_image(id)
            update_car(id, brand, model, year, doors, favorite,
                       filename, color, cylinder_capacity, velocity)
            save_image(filename, photo)
            delete_image(old_image)
            return jsonify({'message': 'Car Updated!'})


@cars.route('/delete/<int:id>', methods=['DELETE'])
def delete(id):
    response = delete_car(id)
    if response:
        delete_image(response)
        return jsonify({'message': 'Car deleted!'})

def set_image(original_filename):
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    return f"{timestamp}_{original_filename}"

def save_image(filename, photo):
    photo.save(os.path.join('static/images/', filename))


def delete_image(filename):
    # Ruta completa a la imagen
    image_path = os.path.join('static/images', filename)
    # Verificar si el archivo de la imagen existe y eliminarlo
    if os.path.exists(image_path):
        os.remove(image_path)
