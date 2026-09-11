from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from datetime import datetime

db = SQLAlchemy()


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)

    username = db.Column(
        db.String(100),
        unique=True,
        nullable=False
    )

    email = db.Column(
        db.String(150),
        unique=True,
        nullable=False
    )

    password = db.Column(
        db.String(255),
        nullable=False
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )


class Machine(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    machine_id = db.Column(
        db.String(50),
        unique=True,
        nullable=False
    )

    machine_type = db.Column(
        db.String(100),
        nullable=False
    )

    purchase_year = db.Column(
        db.Integer
    )

    machine_age_years = db.Column(
        db.Float
    )

    operating_hours = db.Column(
        db.Float
    )

    production_type = db.Column(
        db.String(150)
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )


class SensorReading(db.Model):
    id = db.Column(
        db.Integer,
        primary_key=True
    )

    machine_id = db.Column(
        db.String(50),
        nullable=False
    )

    timestamp = db.Column(
        db.DateTime
    )

    temperature = db.Column(
        db.Float
    )

    vibration = db.Column(
        db.Float
    )

    pressure = db.Column(
        db.Float
    )

    current = db.Column(
        db.Float
    )

    voltage = db.Column(
        db.Float
    )

    rpm = db.Column(
        db.Float
    )

    lubrication_level = db.Column(
        db.Float
    )

    production_rate = db.Column(
        db.Float
    )


class Analysis(db.Model):
    id = db.Column(
        db.Integer,
        primary_key=True
    )

    machine_id = db.Column(
        db.String(50),
        nullable=False
    )

    status = db.Column(
        db.String(50)
    )

    failure_probability = db.Column(
        db.Float
    )

    failure_type = db.Column(
        db.String(100)
    )

    faulty_component = db.Column(
        db.String(150)
    )

    root_cause = db.Column(
        db.String(150)
    )

    confidence = db.Column(
        db.Float
    )

    recommendation = db.Column(
        db.Text
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )


class MaintenanceHistory(db.Model):
    id = db.Column(
        db.Integer,
        primary_key=True
    )

    machine_id = db.Column(
        db.String(50),
        nullable=False
    )

    maintenance_date = db.Column(
        db.DateTime
    )

    maintenance_type = db.Column(
        db.String(150)
    )

    description = db.Column(
        db.Text
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )
