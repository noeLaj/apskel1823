def as_admin(request):
    return{'as_admin':request.user.groups.filter(name='admin').exists()}

def as_owner(request):
    return{'as_owner':request.user.groups.filter(name='owner').exists()}
