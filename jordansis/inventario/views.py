from django.shortcuts import render,HttpResponse
from .models import grupo, clientes, proveedor, productos, notas
from django.views.generic.list import ListView
from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy
from django.shortcuts import render,HttpResponse
from reportlab.pdfgen import canvas
# Create your views here.
from reportlab.lib.pagesizes import letter
from reportlab.platypus import Table
import io
from reportlab.platypus import SimpleDocTemplate, Paragraph, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import Table
from django.contrib.auth.mixins import LoginRequiredMixin

class grupolistar(LoginRequiredMixin,ListView):
    login_url = 'login'
    model = grupo
    template_name = 'mantenimientos/grupolistar.html'

class grupoguardar(CreateView):
    model = grupo
    fields = ['gruponombre','grupoanulado']
    template_name = 'mantenimientos/grupoguardar.html'
    success_url = reverse_lazy('grupolistar')

class grupomodificar(UpdateView):
    model = grupo
    fields = ['gruponombre','grupoanulado']
    template_name = 'mantenimientos/grupoguardar.html'
    success_url = reverse_lazy('grupolistar')

def hello_pdf(request):
    # Cree el objeto HttpResponse con los encabezados de PDF adecuados.
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename=hello.pdf'

    # Cree el objeto PDF, utilizando el objeto de respuesta como su "archivo".
    p = canvas.Canvas(response)

    # Cree el objeto PDF, utilizando el objeto de respuesta como su "archivo".
    # Consulte la documentación de ReportLab para obtener la lista completa de funciones.
    p.drawString(100, 100, "Hello world.")

    # Cierre el objeto PDF limpiamente y listo.
    p.showPage()
    p.save()
    return response

def grupos_print(self, pk=None):
   response = HttpResponse(content_type='application/pdf')
   buff = io.BytesIO()
   doc = SimpleDocTemplate(buff,
                           pagesize=letter,
                           rightMargin=40,
                           leftMargin=40,
                           topMargin=60,
                           bottomMargin=18,
                           )
   categorias = []
   styles = getSampleStyleSheet()
   header = Paragraph("Listado de Grupos", styles['Heading1'])
   categorias.append(header)
   headings = ('Id', 'Grupo', 'Activo')
   if not pk:
      todosgrupos= [(p.id, p.gruponombre, p.grupoanulado)
                         for p in grupo.objects.all().order_by('pk')]
   else:
      todosgrupos = [(p.id, p.gruponombre, p.grupoanulado)
                         for p in grupo.objects.filter(id=pk)]
   t = Table([headings] + todosgrupos)
   t.setStyle(TableStyle(
      [
         ('GRID', (0, 0), (3, -1), 1, colors.dodgerblue),
         ('LINEBELOW', (0, 0), (-1, 0), 2, colors.darkblue),
         ('BACKGROUND', (0, 0), (-1, 0), colors.dodgerblue)
      ]
   ))


   categorias.append(t)
   doc.build(categorias)
   response.write(buff.getvalue())
   buff.close()
   return response

################CLIENTES################################################################################################################################################

class clientelistar(LoginRequiredMixin,ListView):
    login_url = 'login'
    model = clientes
    template_name = 'mantenimientos/clientelistar.html'

class clienteguardar(CreateView):
    model = clientes
    fields = ['clientecedula','clientenombre','clientetelefono','clienteanulado']
    template_name = 'mantenimientos/clienteguardar.html'
    success_url = reverse_lazy('clientelistar')

class clientemodificar(UpdateView):
    model = clientes
    fields = ['clientecedula', 'clientenombre', 'clientetelefono', 'clienteanulado']
    template_name = 'mantenimientos/clientemodificar.html'
    success_url = reverse_lazy('clientelistar')

def cliente_print(self, pk=None):
   response = HttpResponse(content_type='application/pdf')
   buff = io.BytesIO()
   doc = SimpleDocTemplate(buff,
                           pagesize=letter,
                           rightMargin=40,
                           leftMargin=40,
                           topMargin=60,
                           bottomMargin=18,
                           )
   lista = []
   styles = getSampleStyleSheet()
   header = Paragraph("Listado de cliente", styles['Heading1'])
   lista.append(header)
   headings = ('Id', 'cedula', 'nombre', 'telefono', 'activo')
   if not pk:
      todoslista= [(p.id,p.clientecedula, p.clientenombre, p.clientetelefono, p.clienteanulado)
                         for p in clientes.objects.all().order_by('pk')]
   else:
      todoslista = [(p.id,p.clientecedula, p.clientenombre, p.clientetelefono, p.clienteanulado)
                         for p in clientes.objects.filter(id=pk)]
   t = Table([headings] + todoslista)
   t.setStyle(TableStyle(
      [
         ('GRID', (0, 0), (4, -1), 1, colors.dodgerblue),
         ('LINEBELOW', (0, 0), (-1, 0), 2, colors.darkblue),
         ('BACKGROUND', (0, 0), (-1, 0), colors.dodgerblue)
      ]
   ))


   lista.append(t)
   doc.build(lista)
   response.write(buff.getvalue())
   buff.close()
   return response

################ Proveedor ################################################################################################

class proveedorlistar(LoginRequiredMixin,ListView):
    login_url = 'login'
    model = proveedor
    template_name = 'mantenimientos/proveedorlistar.html'

class proveedorguardar(CreateView):
    model = proveedor
    fields = ['proveedorcedula','proveedornombres','proveedortelefono','proveedoranulado']
    template_name = 'mantenimientos/proveedorguardar.html'
    success_url = reverse_lazy('proveedorlistar')

class proveedormodificar(UpdateView):
    model = proveedor
    fields = ['proveedorcedula', 'proveedornombres', 'proveedortelefono', 'proveedoranulado']
    template_name = 'mantenimientos/proveedormodificar.html'
    success_url = reverse_lazy('proveedorlistar')

def proveedor_print(self, pk=None):
   response = HttpResponse(content_type='application/pdf')
   buff = io.BytesIO()
   doc = SimpleDocTemplate(buff,
                           pagesize=letter,
                           rightMargin=40,
                           leftMargin=40,
                           topMargin=60,
                           bottomMargin=18,
                           )
   lista = []
   styles = getSampleStyleSheet()
   header = Paragraph("Listado de Proveedor", styles['Heading1'])
   lista.append(header)
   headings = ('Id', 'cedula', 'nombres', 'telefono', 'activo')
   if not pk:
      todoslista= [(p.id,p.proveedorcedula, p.proveedornombres, p.proveedortelefono, p.proveedoranulado)
                         for p in proveedor.objects.all().order_by('pk')]
   else:
      todoslista = [(p.id,p.proveedorcedula, p.proveedornombres, p.proveedortelefono, p.proveedoranulado)
                         for p in proveedor.objects.filter(id=pk)]
   t = Table([headings] + todoslista)
   t.setStyle(TableStyle(
      [
         ('GRID', (0, 0), (4, -1), 1, colors.dodgerblue),
         ('LINEBELOW', (0, 0), (-1, 0), 2, colors.darkblue),
         ('BACKGROUND', (0, 0), (-1, 0), colors.dodgerblue)
      ]
   ))


   lista.append(t)
   doc.build(lista)
   response.write(buff.getvalue())
   buff.close()
   return response

################ Productos ################################################################################################

class productoslistar(LoginRequiredMixin,ListView):
    login_url = 'login'
    model = productos
    template_name = 'mantenimientos/productoslistar.html'

class productosguardar(CreateView):
    model = productos
    fields = ['productosnombre','productospreciovta','productoscodigo','productosexistencia','productosgrupo']
    template_name = 'mantenimientos/productosguardar.html'
    success_url = reverse_lazy('productoslistar')

class productosmodificar(UpdateView):
    model = productos
    fields = ['productosnombre','productospreciovta','productoscodigo','productosexistencia','productosgrupo']
    template_name = 'mantenimientos/productosmodificar.html'
    success_url = reverse_lazy('productoslistar')

def productos_print(self, pk=None):
   response = HttpResponse(content_type='application/pdf')
   buff = io.BytesIO()
   doc = SimpleDocTemplate(buff,
                           pagesize=letter,
                           rightMargin=40,
                           leftMargin=40,
                           topMargin=60,
                           bottomMargin=18,
                           )
   lista1 = []
   styles = getSampleStyleSheet()
   header = Paragraph("Listado de Productos", styles['Heading1'])
   lista1.append(header)
   headings = ('Id', 'nombre', 'preciovta', 'codigo', 'existencia','grupo')
   if not pk:
      todoslista = [(p.id,p.productosnombre, p.productospreciovta, p.productoscodigo, p.productosexistencia, p.productosgrupo)
                         for p in productos.objects.all().order_by('pk')]
   else:
      todoslista = [(p.id,p.productosnombre, p.productospreciovta, p.productoscodigo, p.productosexistencia, p.productosgrupo)
                         for p in productos.objects.filter(id=pk)]
   t = Table([headings] + todoslista)
   t.setStyle(TableStyle(
      [
         ('GRID', (0, 0), (6, -1), 1, colors.dodgerblue),
         ('LINEBELOW', (0, 0), (-1, 0), 2, colors.darkblue),
         ('BACKGROUND', (0, 0), (-1, 0), colors.dodgerblue)
      ]
   ))


   lista1.append(t)
   doc.build(lista1)
   response.write(buff.getvalue())
   buff.close()
   return response


class notalistar(LoginRequiredMixin,ListView):
    login_url = 'login'
    model = notas
    template_name = 'mantenimientos/notaslistar.html'

class notaguardar(CreateView):
    model = notas
    fields = ['notaestudiante']
    template_name = 'mantenimientos/notasguardar.html'
    success_url = reverse_lazy('notaslistar')

class notamodificar(UpdateView):
    model = notas
    fields = ['notaestudiante']
    template_name = 'mantenimientos/notasmodificar.html'
    success_url = reverse_lazy('notaslistar')

def nota_print(self, pk=None):
   response = HttpResponse(content_type='application/pdf')
   buff = io.BytesIO()
   doc = SimpleDocTemplate(buff,
                           pagesize=letter,
                           rightMargin=40,
                           leftMargin=40,
                           topMargin=60,
                           bottomMargin=18,
                           )
   categorias = []
   styles = getSampleStyleSheet()
   header = Paragraph("Listado de Notas", styles['Heading1'])
   categorias.append(header)
   headings = ('Id', 'notas')
   if not pk:
      todosgrupos= [(p.id, p.notaestudiante)
                         for p in notas.objects.all().order_by('pk')]
   else:
      todosgrupos = [(p.id, p.notaestudiante)
                         for p in notas.objects.filter(id=pk)]
   t = Table([headings] + todosgrupos)
   t.setStyle(TableStyle(
      [
         ('GRID', (0, 0), (3, -1), 1, colors.dodgerblue),
         ('LINEBELOW', (0, 0), (-1, 0), 2, colors.darkblue),
         ('BACKGROUND', (0, 0), (-1, 0), colors.dodgerblue)
      ]
   ))


   categorias.append(t)
   doc.build(categorias)
   response.write(buff.getvalue())
   buff.close()
   return response
