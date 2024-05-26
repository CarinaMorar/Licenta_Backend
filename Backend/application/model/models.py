from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Enum

db = SQLAlchemy()

class FoodScheduleModel(db.Model):
    __tablename__ = "food_schedule"

    id = db.Column(db.Integer, primary_key= True)
    schedule_name = db.Column(db.String(), nullable= False)
    number_meals = db.Column(db.Integer, nullable= False)
    meal_1 = db.Column(db.Time, nullable= True)
    meal_2 = db.Column(db.Time, nullable= True)
    meal_3 = db.Column(db.Time, nullable= True)
    meal_4 = db.Column(db.Time, nullable= True)
    meal_5 = db.Column(db.Time, nullable= True)
    meal_6 = db.Column(db.Time, nullable= True)
    stepper_rotations = db.Column(db.Integer, nullable= False)

    def repr(self):
        return {
            "id": self.id,
            "schedule_name": self.schedule_name,
            "number_meals": self.number_meals,
            "meal_1": self.meal_1,
            "meal_2": self.meal_2,
            "meal_3": self.meal_3,
            "meal_4": self.meal_4,
            "meal_5": self.meal_5,
            "meal_6": self.meal_6,
            "stepper_rotations": self.stepper_rotations
        }


class WeightStatisticsModel(db.Model):
    __tablename__ = "weight_statistics"
    id = db.Column(db.Integer, primary_key= True)
    value = db.Column(db.Float, nullable= False)
    date = db.Column(db.Date, nullable= False)
    time = db.Column(db.Time, nullable= False)

    def repr(self):
        return {
            "id": self.id,
            "value": self.value,
            "date": self.date,
            "time": self.time
        }


