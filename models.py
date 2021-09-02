from app import db



class Jobs(db.Model):
    __tablename__ = 'jobs'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    first_name = db.Column(db.String())
    last_name = db.Column(db.String())
    gender = db.Column(db.String())
    job_title = db.Column(db.String())
    

