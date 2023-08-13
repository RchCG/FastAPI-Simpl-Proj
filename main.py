import uvicorn
from fastapi import FastAPI
from API.handlers import users_router

app = FastAPI(title="UsersFiltrationWithoutSQL")

# set routes to the app instance
app.include_router(users_router)

if __name__ == '__main__':
    # run app on the host and port
    uvicorn.run(app, host="0.0.0.0", port=8000)
