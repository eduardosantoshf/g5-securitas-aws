from fastapi import FastAPI, Request
my_app = FastAPI()

@my_app.get("/intrusion/{id}")
async def get_video(id):
    return {"video_id": id}
    #req_info = await info.json()
    #return {
    #    "status" : "SUCCESS",
    #    "data" : req_info
    #}