from flask import Flask, render_template, request, jsonify
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

app = Flask(__name__)

# Create a new chat bot named UBCAdmissionsBot
chatbot = ChatBot(
    'UBCAdmissionsBot',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        'chatterbot.logic.BestMatch'
    ],
    database_uri='sqlite:///database.sqlite3'
)

# Custom training data for UBC Admissions Bot
trainer = ListTrainer(chatbot)
trainer.train([
    "Hello",
    "Hello! Welcome to the UBC Admissions Office. How can I assist you today?",
    "Admission Requirements",
    "UBC's general admission requirements for undergraduate programs include completion of secondary school with a competitive average, specific course prerequisites, and English language proficiency. For detailed requirements, visit: https://you.ubc.ca/applying-ubc/admitted/admission-requirements/",
    "Application Process",
    "You can apply to UBC by following these steps: 1. Choose your program and check specific requirements. 2. Prepare your documents. 3. Create an account on the UBC application portal and complete the application. 4. Pay the application fee and submit your application. For more details, visit: https://you.ubc.ca/applying-ubc/how-to-apply/",
    "Document Submission",
    "You can submit your documents electronically through the UBC application portal. If sending physical documents, mail them to: UBC Admissions Office, 1200-1874 East Mall, Vancouver, BC V6T 1Z1, Canada. For more details, visit: https://you.ubc.ca/applying-ubc/admitted/submitting-your-documents/",
    "Scholarships and Financial Aid",
    "UBC offers various options including merit-based scholarships, need-based financial aid, and external awards. For more information, visit: https://you.ubc.ca/financial-planning/scholarships-awards-canadian-students/",
    "Campus Tours",
    "You can book a campus tour online through our Campus Tours page. Tours are available throughout the year. Visit: https://you.ubc.ca/tours-info-sessions/",
    "Contact Information",
    "You can reach the UBC admissions office by: Phone: +1 604-822-9836, Email: admissions.inquiry@ubc.ca, Mail: UBC Admissions Office, 1200-1874 East Mall, Vancouver, BC V6T 1Z1, Canada. For more contact options, visit: https://you.ubc.ca/contact-us/"
])

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get_response", methods=["POST"])
def get_bot_response():
    user_input = request.json.get("message")
    response = chatbot.get_response(user_input)
    return jsonify({"response": str(response)})

if __name__ == "__main__":
    app.run(debug=True)
