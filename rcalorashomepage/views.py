from pyramid.view import view_config

@view_config(route_name='home', renderer='templates/mytemplate.pt')
def my_view(request):
    return {'project':'rcaloras-homepage'}

@view_config(name='helloworld', renderer='templates/helloworld.pt')
def helloworld_view(request):
    return {'project':'rcaloras-homepage'}
