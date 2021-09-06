from fastapi import FastAPI

app = FastAPI(
    title="My title",
    description="My description",
    version="0.0.1",
)


@app.get("/")
def read_root():
    return {"Hello": "World"}
