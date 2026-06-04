from fastapi import FastAPI
import requests

STUDENT_N = 4

app = FastAPI(title="Checkout Service")

CHECKOUTS = []

PAYMENT_URL = "http://payment-gateway:8000"


@app.post("/checkout")
def checkout():

    response = requests.post(
        f"{PAYMENT_URL}/process-payment"
    )

    payment_data = response.json()

    checkout_data = {
        "student_id": STUDENT_N,
        "checkout_id": 401,
        "payment_status": payment_data["status"]
    }

    CHECKOUTS.append(checkout_data)

    return checkout_data


@app.get("/summary")
def summary():

    return {
        "student_id": STUDENT_N,
        "operations": CHECKOUTS
    }