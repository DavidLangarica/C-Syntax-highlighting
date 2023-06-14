from pygments import highlight
from pygments.lexers import CSharpLexer
from pygments.formatters import HtmlFormatter
import os
import glob
import time
import psutil

# Resaltamos la sintaxis de un archivo de C#
def highlight_file(file_path):
    try:
        with open(file_path, 'r') as file:
            code = file.read()
            
        lexer = CSharpLexer()
        formatter = HtmlFormatter(linenos=True, style='dracula')
        result = highlight(code, lexer, formatter)
        
        output_file = os.path.splitext(file_path)[0] + '.html'
        with open(output_file, 'w') as file:
            file.write(
                '''
                <!DOCTYPE html><html>
                <head><meta charset="utf-8" /><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>C# Code Highlighter</title></head>
                <body>
                <style>{}</style>
                {}
                </body></html>
                '''
            .format(formatter.get_style_defs('.highlight'), result))

        print(f'Se completó exitosamente el archivo: {file_path}')
    except IOError as e:
        print(f'Hubo un problema con el archivo: {file_path}. Error: {str(e)}')

# Tomamos los archivos a resaltar
csharp_files = glob.glob('./*.cs')

# Cálculo de la memoria y tiempo antes de la ejecución
start_time = time.time()
memory_before = psutil.Process().memory_info().rss

# Procesamiento secuencial 
for file in csharp_files:
    highlight_file(file)
    
# Cálculo de la memoria y tiempo después de la ejecución
memory_after = psutil.Process().memory_info().rss
memory_used = memory_after - memory_before
print(f'Memoria usada: {memory_used} bytes')

end_time = time.time()
execution_time = end_time - start_time
print(f'Tiempo de ejecución {execution_time} segundos')
