from faker import Faker
from models import db, User, Event, Participant
from main import app
import random
from datetime import datetime, timedelta

fake = Faker()

def seed_data():
    with app.app_context():
        db.drop_all()  # Drop existing tables
        db.create_all()  # Create new tables

        users = []
        for _ in range(10):
            user = User(
                username=fake.user_name(),
                email=fake.email()
            )
            users.append(user)
            db.session.add(user)

        db.session.commit()

        events = []
        for _ in range(10):
            event = Event(
                name=fake.catch_phrase(),
                description=fake.text(),
                date=fake.date_time_between(start_date='-1y', end_date='+1y'),
                location=fake.address(),
                organizer_id=random.choice(users).id
            )
            events.append(event)
            db.session.add(event)

        db.session.commit()

        participants = []
        for _ in range(30):
            participant = Participant(
                user_id=random.choice(users).id,
                event_id=random.choice(events).id
            )
            participants.append(participant)
            db.session.add(participant)

        db.session.commit()

        print("Database seeded!")

if __name__ == '__main__':
    seed_data()
