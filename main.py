from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.route import route

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(route)

# bisa hapus
# if __name__ == '__main__':
#     import uvicorn
#
#     app_str = 'main:app'
#     uvicorn.run(app_str, host='192.168.18.55', reload=True, port=8080, workers=1)
