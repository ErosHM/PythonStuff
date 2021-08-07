import os
import cat_service


def main():
    # Imprimir cabecera
    print_header()
    # Obtener o crear carpeta de salida
    folder = get_or_crate_output_folder()
    print("Carpeta encontrada o creada exitosamente: " + folder)
    # Descargar gatos
    download_cats(folder)
    # Mostrar gatos


def print_header():
    print("CAT FACTORY")


def get_or_crate_output_folder():
    folder = "cat_pictures"
    base_folder = os.path.dirname(__file__)
    full_path = os.path.abspath(os.path.join(base_folder, folder))
    print(full_path)

    # Primero revisar que la direccion exista, despues revisar so la direccion corresponde a un directorio
    if not os.path.exists(full_path) or not os.path.isdir(full_path):
        print("Creando nuevo directorio en {}".format(full_path))
        os.mkdir(full_path)

    return full_path


def download_cats(folder):
    print('Peticion para descargar gatos...')
    cat_count=8
    for i in range(1,cat_count+1):
        name="lolcat {}".format(i)
        print('Descargando gato '+name)
        cat_service.get_cat(folder,name)

    print('Hecho')


if __name__ == '__main__':
    main()
