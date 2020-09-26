import matplotlib.pyplot as plt
import seaborn as sns
from io import BytesIO
import base64
from django.contrib.auth.models import User

def get_salesman_from_id(val):
    salesman = User.objects.all().get(id=val) #Retorna la funcion __str__ con su nombre usuario
    print(salesman)
    return salesman

def get_image():
    buffer = BytesIO() # Almacena bytes de una imagen
    plt.savefig(buffer, format='png') # create grafico ocupando imagen
    buffer.seek(0) # establece el cursos al principio de stream
    image_png = buffer.getvalue() # recupera todo el contenido del archivo

    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')

    buffer.close() # libera memoria

    return graph

def get_simple_plot(chart_type, *args, **kwargs):
    plt.switch_backend('AGG')
    fig = plt.figure(figsize=(10,4))
    x = kwargs.get('x')
    y = kwargs.get('y')
    data = kwargs.get('data')
    
    if chart_type == 'bar plot':
        title = 'Precio total por día (Barra)'
        plt.title(title)
        plt.bar(x,y)
    elif chart_type == 'line plot':
        title = 'Precio total por día (Línea)'
        plt.title(title)
        plt.plot(x,y)
    else:
        title = 'Cantidad de productos'
        plt.title(title)
        sns.countplot('name', data=data)
    
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    graph = get_image()
    return graph