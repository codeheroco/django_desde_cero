from django import forms
from models import Articulo, Comentario

from django.utils import timezone   


class ArticuloForm(forms.ModelForm):

   class Meta:
      model = Articulo

   #Validamos que el autor no sea menor a 3 caracteres
   def clean_autor(self):
      diccionario_limpio = self.cleaned_data
      
      autor = diccionario_limpio.get('autor')

      if len(autor) < 3:
         raise forms.ValidationError("El autor debe contener mas de tres caracteres")

      return autor	 

   #Validamos que el titulo no sea mayor a 50 caracteres
   def clean_titulo(self):
      diccionario_limpio = self.cleaned_data
      
      titulo = diccionario_limpio.get('titulo')

      if len(titulo) > 50:
         raise forms.ValidationError("El titulo debe ser menor a 50 caracteres")

      return titulo	

   #Validamos que el texto no sea mayor a 400 caracteres
   def clean_texto(self):
      diccionario_limpio = self.cleaned_data
      
      texto = diccionario_limpio.get('texto')

      if len(texto) > 400:
         raise forms.ValidationError("El texto no debe estar vacio")

      return texto	 

   #Validamos que la fecha no sea mayor a la fecha actual
   def clean_fecha(self):
      diccionario_limpio = self.cleaned_data
      
      fecha_articulo = diccionario_limpio.get('fecha')

      #Obtenemos la fecha actual
      fecha_actual = timezone.now()

      if fecha_actual < fecha_articulo:
         raise forms.ValidationError("El fecha no debe ser mayor al dia de hoy")

      return fecha_articulo


class ComentarioForm(forms.ModelForm):

   class Meta:
      model = Comentario
      fields = ('nombre', 'cuerpo')
      