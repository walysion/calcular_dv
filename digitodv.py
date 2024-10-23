import pandas as pd

def calcular_digito_verificador(rut):
    # Separamos el número de la parte del dígito verificador
    rut = str(rut).replace(".", "").replace("-", "")
    if '-' in rut:
        rut, dv = rut.split('-')
    else:
        dv = ''
    
    rut = int(rut)
    
    suma = 0
    multiplicador = 2

    while rut > 0:
        suma += (rut % 10) * multiplicador
        rut //= 10
        multiplicador += 1
        if multiplicador > 7:
            multiplicador = 2
    
    dv_calculado = 11 - (suma % 11)
    if dv_calculado == 11:
        dv_calculado = '0'
    elif dv_calculado == 10:
        dv_calculado = 'K'
    
    return str(dv_calculado)

def procesar_ruts(input_csv, output_csv):
    # Leer el archivo CSV
    df = pd.read_csv(input_csv)
    
    # Asegurarse de que la columna RUT exista
    if 'RUT' not in df.columns:
        raise ValueError("El archivo CSV debe contener una columna llamada 'RUT'")
    
    # Calcular el dígito verificador
    df['Dígito Verificador'] = df['RUT'].apply(calcular_digito_verificador)
    
    # Guardar el nuevo archivo CSV
    df.to_csv(output_csv, index=False)

# Ejemplo de uso
input_csv = 'comp231024.csv'  # Cambia esto al nombre de tu archivo CSV
output_csv = 'ruts_con_dv.csv'  # Nombre del archivo de salida
procesar_ruts(input_csv, output_csv)

print("Proceso completado. El archivo con dígitos verificadores ha sido guardado.")
