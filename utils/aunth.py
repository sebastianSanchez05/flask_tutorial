from flask import session, request, make_response

def is_session():
    return not session['user']

def create_session():
    usuario = {
        'ip': request.remote_addr,
        'nombre': "Sebastian"
    }
    session["user"] = usuario

    """ response = make_response( redirect("/show") )
    response.set_cookie("user_ip", usuario["ip"])
    response.set_cookie("user_name", usuario["nombre"]) """
