import time
import hashlib

from app import db
from datetime import datetime, timedelta


# Generate 10 character long hash
def _createHash():
    now = str(time.time()).encode('utf-8')
    hash = hashlib.sha1(now)
    return hash.hexdigest()[:7]


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_key = db.Column(db.String(32), index=True, unique=True)
    join_date = db.Column(db.String())
    last_active_date = db.Column(db.String())

    def __init__(self, user_key):
        self.user_key = user_key
        self.join_date = datetime.strftime(
            datetime.utcnow() + timedelta(hours=9),
            '%Y.%m.%d %H:%M:%S')
        self.last_active_date = self.join_date

    def __repr__(self):
        return '<User %r>' % (self.user_key)

    
# 편의점 택배
class Delivery(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    reservation_code = db.Column(db.String(), index=True, unique=True)
    
    sender_name = db.Column(db.String(32))
    sender_phone = db.Column(db.String())
    sender_location = db.Column(db.String())
    
    receiver_name = db.Column(db.String(32))
    receiver_phone = db.Column(db.String())
    receiver_location = db.Column(db.String())
    
    def __init__(self):
        self.reservation_code = _createHash()
    
    def __repr__(self):
        return '<Code %r>' % (self.reservation_code)