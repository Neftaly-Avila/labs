
bibliotecas = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
cadena_unida = ' '.join(bibliotecas)
cadena_con_hashtags = '#' + cadena_unida.replace(' ', ' #')

print(cadena_con_hashtags)
