from django.core.management import BaseCommand

class Command(BaseCommand):

    def handle(self, *args, **options):
        repetidos = [1,2,3,"1","2","3",3,4,5]
        r = [1,"5",2,"3"]
        d_str = '{"valor":125.3,"codigo":123}'

        #Eliminamos los repetidos y convertimos a int los valores del arreglo
        sin_repetidos= list(set(map(lambda x:  int(x), repetidos)))
        print("Sin repetidos: ",sin_repetidos)

        #Convertimos a int los valores del arreglo
        r = list(set(map(lambda x:  int(x), r )))
        en_comun= [i for i in sin_repetidos if i in r]
        print("En común: ", en_comun)
        
        #Limpiamos el string obtenido para luego convertilo a diccionario
        d_str= d_str.replace('"', '').replace('{', '').replace('}','')
        diccionario = dict(char.split(":") for char in d_str.split(","))
        print("Diccionario ", type(diccionario), diccionario)
