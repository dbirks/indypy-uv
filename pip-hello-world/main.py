from fastapi import FastAPI

# Create an instance of the FastAPI application
app = FastAPI()


# Define a route for the root URL ("/")
@app.get("/")
async def read_root():
    return {"Hello": "World"}
