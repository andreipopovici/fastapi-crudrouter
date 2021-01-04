import docker

from fastapi import FastAPI
from fastapi_crudrouter import MongoCRUDRouter
from motor.motor_asyncio import AsyncIOMotorClient

from tests import Potato, PotatoCreate, Carrot, CarrotCreate


def mongo_implementation():
    app = FastAPI()
    # docker_client = docker.from_env()
    # container = docker_client.containers.run('mongo', auto_remove=True, detach=True, name="fastapi-crudrouter-mongo", ports={'27017': '27017'})
    # # container.kill()
    client = AsyncIOMotorClient('mongodb://localhost:27017')

    @app.on_event("shutdown")
    async def shutdown():
        await db.disconnect()

    cursor = client.test.get_collection('potatoes').find({})
    for o in cursor:
        print(o)

    router = MongoCRUDRouter(schema=Potato, collection=client.test.get_collection('potatoes'))
    app.include_router(router)

    return app


if __name__ == '__main__':
    import uvicorn
    app = mongo_implementation()
    uvicorn.run(app)
