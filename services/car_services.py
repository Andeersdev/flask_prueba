from models.car import Car
from utils.db import db


def list_car():
    cars = Car.query.all()
    return cars


def create_car(brand, model, year, doors, is_favorite, photo, color, cylinder_capacity, velocity):
    car = Car(brand=brand,
              model=model,
              year=year,
              doors=doors,
              is_favorite=is_favorite,
              photo=photo,
              color=color,
              cylinder_capacity=cylinder_capacity,
              velocity=velocity)
    db.session.add(car)
    db.session.commit()


def show_car(id):
    car = Car.query.get(id)
    if not car:
        return 'Car not found'
    return car


def update_car(id, brand, model, year, doors, is_favorite, photo, color, cylinder_capacity, velocity):
    car = Car.query.get(id)
    if not car:
        return 'Car not found'
    car.brand = brand
    car.model = model
    car.year = year
    car.doors = doors
    car.is_favorite = is_favorite
    if photo is not None:
        car.photo = photo
    car.color = color
    car.cylinder_capacity = cylinder_capacity
    car.velocity = velocity
    db.session.commit()


def delete_car(id):
    try:
        car = Car.query.get(id)
        if not car:
            return 'Car not found'
        db.session.delete(car)
        db.session.commit()
        return car.photo
    except Exception as e:
        return str(e)


def found_image(id):
    car = Car.query.get(id)
    if not car:
        return 'Car not found'
    return car.photo
