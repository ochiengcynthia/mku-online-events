from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_migrate import Migrate
from models import db, User, Event, Participant
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///events.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

CORS(app)
db.init_app(app)
migrate = Migrate(app, db)

@app.route('/')
def index():
    return 'Welcome to the Event API!'

# GET all Users
@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    user_list = [user.to_dict() for user in users]
    return jsonify(user_list)

#GET user by id
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get(user_id)
    if user:
        return jsonify(user.to_dict()), 200
    else:
        return jsonify({'error': 'User not found'}), 404

#create new user
@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    user = User(username=data['username'], email=data['email'])
    db.session.add(user)
    db.session.commit()
    return jsonify(user.to_dict()), 201

#update user details
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    user = User.query.get(user_id)
    if user:
        user.username = data.get('username', user.username)
        user.email = data.get('email', user.email)
        db.session.commit()
        return jsonify(user.to_dict()), 200
    else:
        return jsonify({'error': 'User not found'}), 404

#delete user
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.get(user_id)
    if user:
        db.session.delete(user)
        db.session.commit()
        return jsonify({'message': 'User deleted'}), 200
    else:
        return jsonify({'error': 'User not found'}), 404

# Event routes
@app.route('/events', methods=['GET'])
def get_events():
    events = Event.query.all()
    event_list = [event.__dict__ for event in events]
    for event in event_list:
        del event['_sa_instance_state']
    return jsonify(event_list)

#GET event by id
@app.route('/events/<int:event_id>', methods=['GET'])
def get_event(event_id):
    event = Event.query.get(event_id)
    if event:
        return jsonify(event.__dict__), 200
    else:
        return jsonify({'error': 'Event not found'}), 404

#create event
@app.route('/events', methods=['POST'])
def create_event():
    data = request.get_json()
    event = Event(
        name=data['name'],
        description=data['description'],
        date=datetime.strptime(data['date'], '%Y-%m-%d %H:%M:%S'),
        location=data['location'],
        organizer_id=data['organizer_id']
    )
    db.session.add(event)
    db.session.commit()
    return jsonify(event.__dict__), 201

#UPDATE event
@app.route('/events/<int:event_id>', methods=['PUT'])
def update_event(event_id):
    data = request.get_json()
    event = Event.query.get(event_id)
    if event:
        event.name = data.get('name', event.name)
        event.description = data.get('description', event.description)
        event.date = datetime.strptime(data.get('date', event.date.strftime('%Y-%m-%d %H:%M:%S')), '%Y-%m-%d %H:%M:%S')
        event.location = data.get('location', event.location)
        db.session.commit()
        return jsonify(event.__dict__), 200
    else:
        return jsonify({'error': 'Event not found'}), 404

#DELETE event
@app.route('/events/<int:event_id>', methods=['DELETE'])
def delete_event(event_id):
    event = Event.query.get(event_id)
    if event:
        db.session.delete(event)
        db.session.commit()
        return jsonify({'message': 'Event deleted'}), 200
    else:
        return jsonify({'error': 'Event not found'}), 404

# Participant routes
@app.route('/participants', methods=['GET'])
def get_participants():
    participants = Participant.query.all()
    participant_list = [participant.__dict__ for participant in participants]
    for participant in participant_list:
        del participant['_sa_instance_state']
    return jsonify(participant_list)

#GET participants by id
@app.route('/participants/<int:participant_id>', methods=['GET'])
def get_participant(participant_id):
    participant = Participant.query.get(participant_id)
    if participant:
        return jsonify(participant.__dict__), 200
    else:
        return jsonify({'error': 'Participant not found'}), 404

#CREATE participant
@app.route('/participants', methods=['POST'])
def create_participant():
    data = request.get_json()
    participant = Participant(
        user_id=data['user_id'],
        event_id=data['event_id']
    )
    db.session.add(participant)
    db.session.commit()
    return jsonify(participant.__dict__), 201

#DELETE participants
@app.route('/participants/<int:participant_id>', methods=['DELETE'])
def delete_participant(participant_id):
    participant = Participant.query.get(participant_id)
    if participant:
        db.session.delete(participant)
        db.session.commit()
        return jsonify({'message': 'Participant deleted'}), 200
    else:
        return jsonify({'error': 'Participant not found'}), 404

if __name__ == '__main__':
    app.run(port=5555)
