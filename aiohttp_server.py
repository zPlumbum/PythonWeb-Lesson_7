from aiohttp import web
from models import User


routes = web.RouteTableDef()


@routes.get('/users/{user_id}')
async def get_user(request):
    user_id = request.match_info['user_id']
    user = User.by_id(user_id)
    return user.to_dict()


@routes.post('/users/')
async def post_user(request):
    user = User(**request.json)
    user.set_password(request.json['password'])
    user.add()
    return user.to_dict()


@routes.delete('/users/{user_id}')
async def delete_user(request):
    user_id = request.match_info['user_id']
    user = User.by_id(user_id)
    user.delete()
    return {'response': 'User has been deleted'}


app = web.Application()
app.add_routes(routes)
web.run_app(app)
