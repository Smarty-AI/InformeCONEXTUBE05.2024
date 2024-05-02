# Importar las herramientas necesarias para mostrar HTML en un navegador
import webbrowser
import os

# Importar las herramientas necesarias para mostrar HTML
from IPython.display import display, HTML

import subprocess

# Comando para instalar Dash
subprocess.run(["pip", "install", "dash"], check=True)

# Creación del contenido HTML como una cadena de texto
html_content = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Informe Financiero</title>
    <link href="https://fonts.googleapis.com/css2?family=Bebas+Neue&display=swap" rel="stylesheet">
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 40px;
        }
        h1, h2 {
            font-family: 'Bebas Neue', sans-serif;
            color: #0056b3;  /* Color por defecto para los demás títulos */
            margin-bottom: 20px;
        }
        .titulo-especial { /* Clase para el título especial */
            color: #01e3a1; /* Nuevo color para 'Caja y bancos' */
        }
        p {
            font-size: 16px;
            color: #333;
            line-height: 1.6;
        }
        iframe {
            border: none;
            margin-bottom: 20px;
        }
        pre {
            background-color: #cdded7;
            border-left: 3px solid #0056b3;
            padding: 10px;
            font-family: monospace;
        }
        table {
            width: 100%;
            border-collapse: collapse; /* Los bordes de la celda se colapsan en uno solo */
        }
        th, td {
            padding: 10px;
            text-align: left;
            border-bottom: 1px solid #ddd; /* Línea debajo de cada fila */
        }
        th {
            background-color: #565655; /* Color de fondo para la cabecera */
            color: white;
        }
        tr:nth-child(even) {
            background-color: #8ac5ad; /* Color de fondo para filas pares */
        }
        tr:nth-child(odd) {
            background-color: #cdded7; /* Color de fondo para filas impares */
        }
    </style>
</head>
<body>

    <img src="content/source/portada.png" alt="Portada" style="width:100%; height:auto;">

    <table>
        <thead>
            <tr>
                <th>Concepto</th>
                <th>Monto</th>
            </tr>
        </thead>
        <tbody>
            <tr><td>Mayor de cuentas</td><td>558.376</td></tr>
            <tr><td>IVA Ventas Anual</td><td>21.721</td></tr>
            <tr><td>Comprobantes emitidos AFIP</td><td>21.721</td></tr>
            <tr><td>IVA Compras Anual</td><td>6.408</td></tr>
            <tr><td>Comprobantes recibidos AFIP</td><td>6.410</td></tr>
        </tbody>
    </table>

    <h1 class="titulo-especial">Caja y bancos</h1>
    <iframe src="content/source/01_cash.html" width="100%" height="400px"></iframe>
    <p>Se observa un incremento importante en el saldo de Fondo Fijo, se crea en septiembre con 30M. Lo mismo respecto a la tenencia de Valores. Se recomienda relevar controles sobre tenencias de Efectivo y Valores.</p>
    
    <h1 class="titulo-especial">Test de Benford</h1>
    <iframe src="content/source/1_benford0003_plot.html" width="100%" height="400px"></iframe>
    <p>No se observan desvíos significativos entre la distribución de los registros contables y la distribución de Benford.</p>
    
    <h1 class="titulo-especial">Test de repeticiones</h1>
    <iframe src="content/source/2_counts0003_plot.html" width="100%" height="400px"></iframe>
    <p>Top Outliers por repeticiones se observan casi 17.894 registros nulos y un gran número de ajustes de redondeo por centavos e importes mínimos.</p>

    <h1 class="titulo-especial">Test de números redondos</h1>
    <p>Como en procedimientos anteriores, se repiten números redondos, mayormente en colocaciones de inversiones. Relevar documentación de 24 Provisiones en números redondos por un total de 150.263.000.-</p>

    <h1 class="titulo-especial">Distribución de gastos</h1>
    <iframe src="content/source/boxplot.html" width="100%" height="400px"></iframe>
    <p>Se excluyeron del análisis las cuentas Ajustes de inventario, Amortizaciones FAB y diferencias de cambio ya que distorsionan la escala de los gráficos. Revisar cuentas con alta dispersión.</p>

    <h1 class="titulo-especial">Acumulación mensual</h1>
    <iframe src="content/source/5_expenses03_plot.html" width="100%" height="400px"></iframe>
    <iframe src="content/source/5_expenses13_plot.html" width="100%" height="400px"></iframe>
    <iframe src="content/source/5_expenses53_plot.html" width="100%" height="400px"></iframe>
    <iframe src="content/source/5_expenses123_plot.html" width="100%" height="400px"></iframe>
    <iframe src="content/source/5_expenses193_plot.html" width="100%" height="400px"></iframe>
    <iframe src="content/source/5_expenses203_plot.html" width="100%" height="400px"></iframe>
    <iframe src="content/source/5_expenses223_plot.html" width="100%" height="400px"></iframe>
    <iframe src="content/source/5_expenses293_plot.html" width="100%" height="400px"></iframe>
    <iframe src="content/source/5_expenses323_plot.html" width="100%" height="400px"></iframe>
    <iframe src="content/source/5_expenses343_plot.html" width="100%" height="400px"></iframe>
    <iframe src="content/source/5_expenses353_plot.html" width="100%" height="400px"></iframe>
    <iframe src="content/source/5_expenses393_plot.html" width="100%" height="400px"></iframe>
    <iframe src="content/source/5_expenses453_plot.html" width="100%" height="400px"></iframe>
    <iframe src="content/source/5_expenses513_plot.html" width="100%" height="400px"></iframe>
    <iframe src="content/source/5_expenses533_plot.html" width="100%" height="400px"></iframe>
    <iframe src="content/source/5_expenses683_plot.html" width="100%" height="400px"></iframe>
    <p>Las cuentas graficadas presentan cambios significativos de tendencia de un mes a otro. Los valores están ajustados por inflación.</p>

    <h1 class="titulo-especial">Test de fines de semana</h1>
    <iframe src="content/source/weekend.html" width="100%" height="400px"></iframe>
    <p>Se entregará a la empresa un listado de pagos bancarios registrados en domingo para revisar si fueron emitidos efectivamente en domingo.</p>

    <h1 class="titulo-especial">Minería de texto</h1>
    <img src="content/source/word sp 202301.png" width="80%" />
    <img src="content/source/word sp 202302.png" width="80%" />
    <img src="content/source/word sp 202303.png" width="80%" />
    <img src="content/source/word sp 202304.png" width="80%" />
    <img src="content/source/word sp 202305.png" width="80%" />
    <img src="content/source/word sp 202306.png" width="80%" />
    <img src="content/source/word sp 202307.png" width="80%" />
    <img src="content/source/word sp 202308.png" width="80%" />
    <img src="content/source/word sp 202309.png" width="80%" />
    <img src="content/source/word sp 202310.png" width="80%" />
    <img src="content/source/word sp 202311.png" width="80%" />
    <img src="content/source/word sp 202312.png" width="80%" />
    <p>Se observa mucha referencia a material de muestra, pero el saldo de la cuenta de muestras es mínimo. Debido a la cantidad de transacciones, el análisis se realizó en forma mensual.</p>

    <h1 class="titulo-especial">Patrones de asientos</h1>
    <p>Mas de 8.000 asientos de ajuste de inventario.<p>
    <p>748 asientos que solo tienen la cuenta 110104 Cheques en cartera en ambos sentidos.<p>
    <p>449 asientos que solo tienen la cuenta 110402 Facturas por Cobrar Nacional.<p>
    <p>438 asientos que solo tienen la cuenta 110201 Banco Credicoop.<p>
    <p>Consulta con la empresa por qué suceden estos asientos nulos y sobre todo por qué hay tanto ajuste de inventario.</p>

    <h1 class="titulo-especial">Conciliación de compras y ventas</h1>
    <p>Las ventas coinciden con lo reportado por el fisco. En compras hay 9% de comprobantes a conciliar, luego de depurar importaciones y gastos bancarios. Se debe analizar el listado junto a la empresa.</p>

    <h1 class="titulo-especial">Resultados parciales</h1>
    <ul>
        <li>Se requiere analizar procedimiento de tenencias.</li>
        <li>Verificar motivo de la existencia de registros nulos (igual a cero) y de asientos de una sola cuenta en ambos sentidos.</li>
        <li>Revisar el plan de cuentas para evitar dispersión en cuentas de gastos. En especial aquellas que el sistema indica, para mejorar el seguimiento analíticos de los gastos.</li>
        <li>Verificar provisiones de gastos, según muestra generada por el sistema.</li>
        <li>Verificar outliers según análisis de dispersión.</li>
        <li>Relevar procedimiento de inventarios debido a la cantidad y monto de ajustes registrados.</li>
        <li>Verificar diferencias en compras, tanto aquellas registradas por la empresa y no por el fisco, como aquellas informadas por el fisco y que la empresa no tiene.</li>

</body>
</html>
"""

# Guardar el HTML en un archivo temporal y abrirlo en el navegador
file_path = 'temp.html'
with open(file_path, 'w', encoding='utf-8') as f:
    f.write(html_content)
webbrowser.open('file://' + os.path.realpath(file_path))