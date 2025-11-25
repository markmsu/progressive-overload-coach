
# we import fastapi, which is the framework that lets us build apis quickly
# think of fastapi as the tool that gives us "@app.get" and "@app.post"
from fastapi import FastAPI

# we import the router object from our health route file.
# "router" is a group of endpoints defined in routes/health.py
# we bring it in here so the main app knows about those endpoints
from app.routes.health import router as health_router

# this creates the main FastAPI application.
# think of this as the backend server object that holds all routes.
# the title/version show up in the auto docs page
app = FastAPI(
    title="Progressive Overload Coach API",
    version="0.1"
)

# this attaches the health router onto the main app.
# why? because we want to keep routes in seperate files
# but we still need to "plug them into" the main app
# after this line runs, /health endpoint becomes active
app.include_router(health_router)

# this defines a simple root endpoint '/'.
# its mainly here to test if API is alive.
# if you go to localhost:8000/ you should see the message below.
@app.get("/")
def root():
    # FastAPI auto converts the Python dict to JSON
    return {"message" : "API is running"}





