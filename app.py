from flask import Flask, render_template, request, jsonify, send_file
import os
import stripe
import csv
import tempfile

app = Flask(__name__)

# Stripe setup
stripe.api_key = os.environ.get("STRIPE_SECRET_KEY")
PUBLISHABLE_KEY = os.environ.get("STRIPE_PUBLISHABLE_KEY")

# Home route
@app.route("/")
def index():
    return render_template("index.html", publishable_key=PUBLISHABLE_KEY)

# Upload route (stub for now)
@app.route("/upload", methods=["POST"])
def upload():
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400
    f = request.files["file"]
    temp_dir = tempfile.mkdtemp()
    file_path = os.path.join(temp_dir, f.filename)
    f.save(file_path)
    # TODO: analyze/bleed-fix logic
    return jsonify({"message": "File uploaded successfully", "filename": f.filename})

# Create Stripe checkout session
@app.route("/create-checkout-session", methods=["POST"])
def create_checkout_session():
    try:
        session = stripe.checkout.Session.create(
            payment_method_types=["card"],
            line_items=[{
                "price_data": {
                    "currency": "usd",
                    "product_data": {"name": "Bleed Buddy File Conversion"},
                    "unit_amount": 599,
                },
                "quantity": 1,
            }],
            mode="payment",
            success_url="https://your-domain.com/success",
            cancel_url="https://your-domain.com/cancel",
        )
        return jsonify({"id": session.id})
    except Exception as e:
        return jsonify(error=str(e)), 403

# Email subscription route
@app.route("/subscribe", methods=["POST"])
def subscribe():
    email = request.form.get("email")
    if not email:
        return jsonify({"error": "Email required"}), 400
    with open("subscribers.csv", "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([email])
    return jsonify({"message": "Subscribed successfully!"})

if __name__ == "__main__":
    app.run(debug=True)
