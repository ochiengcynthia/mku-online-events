from faker import Faker
from models import db, User, Event, Staff, ServiceProvider, Sponsor
import random
from datetime import datetime, timedelta
from main import app

# Initialize Faker
faker = Faker()

# Create the app context
with app.app_context():
    # Drop all tables and recreate them
    db.drop_all()
    db.create_all()

    # Seed Users
    for _ in range(10):
        user = User(
            username=faker.user_name(),
            email=faker.email(),
            password=faker.password()
        )
        db.session.add(user)
    
    # Seed Events
    for _ in range(10):
        event = Event(
            eventname=faker.sentence(nb_words=3),
            description=faker.text(max_nb_chars=200),
            date=faker.date_between(start_date='-1y', end_date='today'),
            venue=faker.address(),
            clientname=faker.name()
        )
        db.session.add(event)
    
    # Seed Staff
    for _ in range(10):
        staff = Staff(
            staffname=faker.name(),
            image=faker.image_url()
        )
        db.session.add(staff)

    # Seed Service Providers
    for _ in range(10):
        service_provider = ServiceProvider(
            service_type=faker.job(),
            products=faker.text(max_nb_chars=200)
        )
        db.session.add(service_provider)
    
    # Seed Sponsors
    for _ in range(10):
        sponsor = Sponsor(
            sponsorname=faker.company(),
            amount=random.uniform(1000, 10000)
        )
        db.session.add(sponsor)

    # Commit the changes
    db.session.commit()

print("Database seeded successfully.")
