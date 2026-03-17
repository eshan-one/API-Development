from fastapi import FastAPI
from fastapi.params import Body
app = FastAPI()

# path operation to start the server

# request GET method url:  "/"
@app.get("/")
async def root():
    return {"message": "I am Steve Rogers!"}


@app.get("/posts")
async def get_posts():
    return {"data": "This is the list of posts!"}


@app.post("/createPosts")
async def create_posts(payload: dict = Body(...)):
    print(payload)
    return {"new_post": f"title: {payload['title']} content: {payload['content']}"}


# The first path operation that matches the request will be executed, so the order of the path operations matters. 
# In this case, if we put the path operation with the path parameter before the one without it, it would never be executed because the path parameter would match all requests. Therefore, we need to put the path operation without the path parameter first, followed by the one with the path parameter.