from flask import Flask, request, jsonify
from flask_cors import CORS
from models import db
from models import User, Event, Staff, ServiceProvider, Sponsor


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///events.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
CORS(app)

# User CRUD
@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([user.to_dict() for user in users])

@app.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    user = User.query.get_or_404(id)
    return jsonify(user.to_dict())

@app.route('/users', methods=['POST'])
def create_user():
    data = request.json
    new_user = User(username=data['username'], email=data['email'], password=data['password'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify(new_user.to_dict()), 201

@app.route('/users/<int:id>', methods=['PUT'])
def update_user(id):
    data = request.json
    user = User.query.get_or_404(id)
    user.username = data.get('username', user.username)
    user.email = data.get('email', user.email)
    user.password = data.get('password', user.password)
    db.session.commit()
    return jsonify(user.to_dict())

@app.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    user = User.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()
    return '', 204

# Event CRUD
@app.route('/events', methods=['GET'])
def get_events():
    events = Event.query.all()
    return jsonify([event.to_dict() for event in events])

@app.route('/events/<int:id>', methods=['GET'])
def get_event(id):
    event = Event.query.get_or_404(id)
    return jsonify(event.to_dict())

@app.route('/events', methods=['POST'])
def create_event():
    data = request.json
    new_event = Event(
        eventname=data['eventname'],
        description=data['description'],
        date=data['date'],
        venue=data['venue'],
        clientname=data['clientname']
    )
    db.session.add(new_event)
    db.session.commit()
    return jsonify(new_event.to_dict()), 201

@app.route('/events/<int:id>', methods=['PUT'])
def update_event(id):
    data = request.json
    event = Event.query.get_or_404(id)
    event.eventname = data.get('eventname', event.eventname)
    event.description = data.get('description', event.description)
    event.date = data.get('date', event.date)
    event.venue = data.get('venue', event.venue)
    event.clientname = data.get('clientname', event.clientname)
    db.session.commit()
    return jsonify(event.to_dict())

@app.route('/events/<int:id>', methods=['DELETE'])
def delete_event(id):
    event = Event.query.get_or_404(id)
    db.session.delete(event)
    db.session.commit()
    return '', 204

# Staff CRUD
@app.route('/staff', methods=['GET'])
def get_staff():
    staff = Staff.query.all()
    return jsonify([s.to_dict() for s in staff])

@app.route('/staff/<int:id>', methods=['GET'])
def get_staff_member(id):
    staff_member = Staff.query.get_or_404(id)
    return jsonify(staff_member.to_dict())

@app.route('/staff', methods=['POST'])
def create_staff():
    data = request.json
    new_staff = Staff(staffname=data['staffname'], image=data['image'])
    db.session.add(new_staff)
    db.session.commit()
    return jsonify(new_staff.to_dict()), 201

@app.route('/staff/<int:id>', methods=['PUT'])
def update_staff(id):
    data = request.json
    staff_member = Staff.query.get_or_404(id)
    staff_member.staffname = data.get('staffname', staff_member.staffname)
    staff_member.image = data.get('image', staff_member.image)
    db.session.commit()
    return jsonify(staff_member.to_dict())

@app.route('/staff/<int:id>', methods=['DELETE'])
def delete_staff(id):
    staff_member = Staff.query.get_or_404(id)
    db.session.delete(staff_member)
    db.session.commit()
    return '', 204

# ServiceProvider CRUD
@app.route('/serviceproviders', methods=['GET'])
def get_service_providers():
    service_providers = ServiceProvider.query.all()
    return jsonify([sp.to_dict() for sp in service_providers])

@app.route('/serviceproviders/<int:id>', methods=['GET'])
def get_service_provider(id):
    service_provider = ServiceProvider.query.get_or_404(id)
    return jsonify(service_provider.to_dict())

@app.route('/serviceproviders', methods=['POST'])
def create_service_provider():
    data = request.json
    new_service_provider = ServiceProvider(service_type=data['service_type'], products=data['products'])
    db.session.add(new_service_provider)
    db.session.commit()
    return jsonify(new_service_provider.to_dict()), 201

@app.route('/serviceproviders/<int:id>', methods=['PUT'])
def update_service_provider(id):
    data = request.json
    service_provider = ServiceProvider.query.get_or_404(id)
    service_provider.service_type = data.get('service_type', service_provider.service_type)
    service_provider.products = data.get('products', service_provider.products)
    db.session.commit()
    return jsonify(service_provider.to_dict())

@app.route('/serviceproviders/<int:id>', methods=['DELETE'])
def delete_service_provider(id):
    service_provider = ServiceProvider.query.get_or_404(id)
    db.session.delete(service_provider)
    db.session.commit()
    return '', 204

# Sponsor CRUD
@app.route('/sponsors', methods=['GET'])
def get_sponsors():
    sponsors = Sponsor.query.all()
    return jsonify([s.to_dict() for s in sponsors])

@app.route('/sponsors/<int:id>', methods=['GET'])
def get_sponsor(id):
    sponsor = Sponsor.query.get_or_404(id)
    return jsonify(sponsor.to_dict())

@app.route('/sponsors', methods=['POST'])
def create_sponsor():
    data = request.json
    new_sponsor = Sponsor(sponsorname=data['sponsorname'], amount=data['amount'])
    db.session.add(new_sponsor)
    db.session.commit()
    return jsonify(new_sponsor.to_dict()), 201

@app.route('/sponsors/<int:id>', methods=['PUT'])
def update_sponsor(id):
    data = request.json
    sponsor = Sponsor.query.get_or_404(id)
    sponsor.sponsorname = data.get('sponsorname', sponsor.sponsorname)
    sponsor.amount = data.get('amount', sponsor.amount)
    db.session.commit()
    return jsonify(sponsor.to_dict())

@app.route('/sponsors/<int:id>', methods=['DELETE'])
def delete_sponsor(id):
    sponsor = Sponsor.query.get_or_404(id)
    db.session.delete(sponsor)
    db.session.commit()
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)
