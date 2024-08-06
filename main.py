# 1525620
# Ruben Espinoza

import csv


def write_binary_file(filename, data):
    with open(filename, "wb") as file:
        for item in data:
            file.write(item.encode('utf-8') + b'\n')
    print(f"Archivo binario '{filename}' creado y datos agregados :)")


def read_binary_file(filename):
    with open(filename, "rb") as file:
        return file.read().decode('utf-8')


def write_hex_file(filename, data):
    with open(filename, "w") as file:
        file.write(data.hex())
    print(f"Archivo hexadecimal '{filename}' creado con éxito.")


def write_bin_file(filename, data):

    def bytes_to_bin(byte_data):
        return ''.join(format(byte, '08b') for byte in byte_data)

    bin_content = bytes_to_bin(data)

    with open(filename, "w") as file:
        file.write(bin_content)
    print(f"Archivo binario '{filename}' creado con éxito.")


def convert_and_write_csv(input_file, output_file):
    text_content = read_binary_file(input_file)

    # Dividir el texto en líneas y reorganizar los datos
    lines = text_content.strip().split('\n')
    reorganized_data = []
    for line in lines:
        carnet, nombre = line.split(maxsplit=1)
        reorganized_data.append([nombre, carnet])

    # Escribir los datos en un archivo CSV
    with open(output_file, "w", newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Nombre', 'Carnet'])  # Escribir encabezado
        writer.writerows(reorganized_data)

    print(f"Archivo CSV '{output_file}' creado con éxito.")


# Datos de los estudiantes
students = [
    "1637723 ALBIZUREZ ALPIREZ DANIEL",
    "1524323 BARRIOS ESTRADA JOSUE EMANUEL",
    "2121323 BAUTISTA FUENTES DANIEL EDUARDO",
    "1549223 CÁCERES FUENTES JULIO ALEJANDRO",
    "1549223 CARRETO AGUILÓN DENNYS ROLANDO YOSIMAR"
]

# Archivo binario
binary_filename = "students.bin"
write_binary_file(binary_filename, students)

# Leer el archivo binario
binary_content = read_binary_file(binary_filename)

# Archivo hexadecimal
hex_filename = "students_hex.txt"
write_hex_file(hex_filename, binary_content.encode('utf-8'))

# Archivo binario en bits
bin_filename = "students_bin.txt"
write_bin_file(bin_filename, binary_content.encode('utf-8'))

# Archivo CSV
csv_filename = "Estudiantes.csv"
convert_and_write_csv(binary_filename, csv_filename)
