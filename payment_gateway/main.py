from fastapi import FastAPI

STUDENT_N = 4

app = FastAPI(title="Payment Gateway Service")

PAYMENTS = {
    401: {
        "tx_id": 401,
        "amount": 250,
        "status": "Success"
    }
}


@app.post("/process-payment")
def process_payment():
    return {
        "student_id": STUDENT_N,
        "tx_id": 401,
        "status": "Success"
    }


@app.get("/status/{tx_id}")
def get_status(tx_id: int):
    if tx_id in PAYMENTS:
        return {
            "student_id": STUDENT_N,
            "payment": PAYMENTS[tx_id]
        }

    return {
        "student_id": STUDENT_N,
        "error": "Transaction not found"
    }
