from fastapi import FastAPI

app = FastAPI()

@app.get("/welcome")
def welocme():
    return {
        "message": "hi ahmed"
    }
