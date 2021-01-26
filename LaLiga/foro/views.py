from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from foro.models import Comentario
from gestionPartidos.models import Partidos
from foro.forms import ComentarioForm
from django.contrib.auth.models import User

#En este caso llamos directamente al nombre del html ya que busca por defecto 
# en template no hace ponerle la ruta con foro.html bastaria salvo que lo metamos 
# otro subdirectorio hay si hay que ponerle la ruta



'''
@login_required(login_url='/accounts/login/')
def foro(request):
   
    listaComentarios = list(Comentario.objects.all())
    return render(request, "foro.html",{"comentarios":listaComentarios})

'''      



@login_required(login_url='/accounts/login/')
def foroselect(request):
   
    listaPartidos = list(Partidos.objects.all())
    return render(request, "foroselect.html",{"partidos":listaPartidos})



#Funcion para sacar el usuario logiado
def getUser(request):
    current_user = request.user
    return current_user




@login_required(login_url='/accounts/login/')
def foro(request,id):

    listaComentarios = list(Comentario.objects.filter(id_partido=id))
    nuevoComentario = None
   

    if request.method == 'POST':    
        comentarioForm = ComentarioForm(data=request.POST)

        if comentarioForm.is_valid():
            nuevoComentario = comentarioForm.save(commit=False)
            nuevoComentario.id_partido = Partidos.objects.get(id=id)
            nuevoComentario.id_usuario = getUser(request)
            nuevoComentario.save()


    else:
        comentarioForm = ComentarioForm()

    return render(request, "foro.html",{"comentarios":listaComentarios,"comentario_Form":comentarioForm})








'''
def post_detail(request, year, month, day, post):
 
   
    new_comment = None
    if request.method == 'POST':
        # A comment was posted
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    # List of similar posts
    post_tags_ids = post.tags.values_list('id', flat=True)
    similar_posts = Post.published.filter(tags__in=post_tags_ids)\
                                  .exclude(id=post.id)
    similar_posts = similar_posts.annotate(same_tags=Count('tags'))\
                                .order_by('-same_tags','-publish')[:4]


    return render(request,
                  'blog/post/detail.html',
                  {'post': post,
                  'comments': comments,
                  'new_comment': new_comment,
                  'comment_form': comment_form,
                  'similar_posts': similar_posts})


'''