from database import db

class StudentResult(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    roll_no = db.Column(db.String(20), unique=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    sgpa = db.Column(db.Float, nullable=False)
    failed_courses = db.Column(db.String(200), nullable=True)

    def __repr__(self):
        return f"<StudentResult {self.roll_no}>"
