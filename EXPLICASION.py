#Conceptos Básicos Palabra x Palabra

from
 
"""#Q es: Es como decir "de dónde" vas a traer algo. Es pa decirle a Python "oye, tráeme esta cosa DE este lugar"

#Ejemplo cotidiano:"""

from app import create_app

"""#Es como decir: "de la carpeta 'app', tráeme la función 'create_app'"

#Sería como decir: "de la tienda tráeme pan" → from tienda import pan"""

import

"""#Q es: Es "traer" o "importar". Es como traer una caja de herramientas q alguien más ya hizo pa q tu no tengas q hacerlas d nuevo.
#Ejemplos:"""

import flask  """tráeme TODO lo de flask"""
from flask import Flask  """# de flask, solo tráeme Flask"""
"""#Es como:

#import = tráeme toda la caja de herramientas
#from X import Y = de esa caja, solo tráeme el martillo"""

def

"""Q es: Significa "definir" o "define". Es pa crear tus propias funciones (como recetas q puedes usar después)."""


def saludar():
    print("hola parcero")
```

"Es como escribir una receta:"
```
def hacer_arepas():
    - agarra maíz
    - muélelo
    - haz bolitas
    - cocínalas

"Después solo dices hacer_arepas() y Python hace todo eso"




@login_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        correo = request.form.get("correo")
        password = request.form.get("password")

        usuario = User.query.filter_by(correo=correo).first()

        if usuario and bcrypt.check_password_hash(usuario.password, password):
            login_user(usuario)  # guarda la sesión con Flask-Login
            flash("Inicio de sesión exitoso ✅", "success")

            # Redirección según el rol
            if usuario.rol == "superadmin":
                return redirect(url_for("superadmin.dashboard"))
            elif usuario.rol == "admin":
                return redirect(url_for("admin.dashboard"))
            elif usuario.rol == "callcenter":
                return redirect(url_for("callcenter.dashboard"))
            elif usuario.rol == "cliente":
                return redirect(url_for("cliente.dashboard"))
            else:
                flash("Tu rol no tiene un panel asignado ❌", "danger")
                return redirect(url_for("login.login"))
        else:
            flash("Correo o contraseña incorrectos ❌", "danger")

    return render_template("login.html")



@login_bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        nombre = request.form.get("nombre")
        correo = request.form.get("correo")
        password = request.form.get("password")
        telefono = request.form.get("telefono")
        pais = request.form.get("pais")

        # Encriptar contraseña
        hashed_pw = bcrypt.generate_password_hash(password).decode("utf-8")

        # Generar código de verificación (6 dígitos)
        codigo = str(random.randint(100000, 999999))

        # Guardar temporalmente en sesión
        session["temp_user"] = {
            "nombre": nombre,
            "correo": correo,
            "password": hashed_pw,
            "telefono": telefono,
            "pais": pais,
            "rol": "cliente"  # siempre cliente por defecto
        }
        session["verification_code"] = codigo
        session["code_expiry"] = (datetime.datetime.now() + datetime.timedelta(minutes=10)).timestamp()

        # Enviar correo de verificación
        msg = Message(
            subject="Verificación de cuenta",
            recipients=[correo],         # el destinatario es el cliente
            sender="tu_correo@gmail.com",  # remitente configurado en MAIL_USERNAME
            reply_to=correo                # el correo del cliente para que al responder llegue a él
        )
        msg.body = f"Hola {nombre},\n\nTu código de verificación es: {codigo}\n\nEste código expira en 10 minutos."

        try:
            mail.send(msg)
            flash("Se envió un código de verificación a tu correo.", "info")
            return redirect(url_for("login.verify_code"))
        except Exception as e:
            flash(f"Error al enviar el correo: {str(e)}", "danger")
            return redirect(url_for("login.register"))

    return render_template("register.html")
