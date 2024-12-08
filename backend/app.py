from flask import Flask
from database import db
from flask_cors import CORS

# Initialize Flask app
app = Flask(__name__)

# Enable CORS for all routes
CORS(app)

from database.models import StudentResult

# Initialize Flask app
app = Flask(__name__)

# Configure the database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///results.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database with the Flask app
db.init_app(app)

# Routes and other logic here
if __name__ == "__main__":
    app.run(debug=True)
# Import database models
from database.models import StudentResult

@app.route('/upload', methods=['POST'])
def upload_results():
    """
    Endpoint to upload a CSV file and save results to the database.
    """
    file = request.files.get('file')
    if not file:
        return jsonify({"error": "No file uploaded"}), 400

    data = pd.read_csv(file)
    for _, row in data.iterrows():
        student = StudentResult(
            roll_no=row['Roll_No'],
            name=row['Name'],
            sgpa=row['SGPA'],
            failed_courses=row.get('Failed_Courses', None)
        )
        db.session.add(student)
    db.session.commit()

    return jsonify({"message": "Results uploaded successfully"}), 200

@app.route('/results/<roll_no>', methods=['GET'])
def get_result(roll_no):
    """
    Endpoint to fetch a student's result by roll number.
    """
    student = StudentResult.query.filter_by(roll_no=roll_no).first()
    if not student:
        return jsonify({"error": "Student not found"}), 404

    result = {
        "roll_no": student.roll_no,
        "name": student.name,
        "sgpa": student.sgpa,
        "failed_courses": student.failed_courses or "None"
    }
    return jsonify(result), 200

if __name__ == '__main__':
    app.run(debug=True)
