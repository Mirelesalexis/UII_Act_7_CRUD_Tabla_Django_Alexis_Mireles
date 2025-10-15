from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.hashers import make_password, check_password # Para encriptar/verificar contraseñas
from .models import Usuario

# Listar usuarios
def listar_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'listar_usuarios.html', {'usuarios': usuarios})

# Ver detalle de un usuario
def detalle_usuario(request, id_usuario):
    usuario = get_object_or_404(Usuario, id_usuario=id_usuario)
    return render(request, 'detalle_usuario.html', {'usuario': usuario})

# Agregar usuario
def agregar_usuario(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        apellido = request.POST['apellido']
        email = request.POST['email']
        contrasena = request.POST['contrasena']
        
        # Encriptar la contraseña antes de guardarla
        hashed_password = make_password(contrasena)
        
        Usuario.objects.create(
            nombre=nombre,
            apellido=apellido,
            email=email,
            contrasena=hashed_password
        )
        return redirect('listar_usuarios')
    return render(request, 'agregar_usuario.html')

# Editar usuario
def editar_usuario(request, id_usuario):
    usuario = get_object_or_404(Usuario, id_usuario=id_usuario)
    if request.method == 'POST':
        usuario.nombre = request.POST['nombre']
        usuario.apellido = request.POST['apellido']
        usuario.email = request.POST['email']
        
        nueva_contrasena = request.POST.get('contrasena')
        if nueva_contrasena: # Si se proporcionó una nueva contraseña, encriptarla y guardarla
            usuario.contrasena = make_password(nueva_contrasena)
            
        usuario.save()
        return redirect('listar_usuarios')
    return render(request, 'editar_usuario.html', {'usuario': usuario})

# Eliminar usuario
def eliminar_usuario(request, id_usuario):
    usuario = get_object_or_404(Usuario, id_usuario=id_usuario)
    if request.method == 'POST':
        usuario.delete()
        return redirect('listar_usuarios')
    return render(request, 'eliminar_usuario.html', {'usuario': usuario})