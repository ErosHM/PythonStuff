import os


def get_or_create_output_folder():
    base_folder=os.path.dirname(__file__)# folder en donde se encuentra el programa
    folder="cat_pictures" # nombre de la carpeta
    full_path=os.path.join(base_folder,folder) # Carpeta para las imagenes
    # print(full_path)

    if not os.path.exists(full_path) or not os.path.isdir(full_path):
        print("Creando nuevo directorio en {}".format(full_path))
        os.mkdir(full_path)

    return full_path


def show_cats():
    pass


def download_cats(folder):
    pass


def print_header():
    print("_________________________________________________")
    print("___________Programa raro de python_______________")
    print("_________________________________________________")


def main():
    # imprimir la cabecera
    print_header()

    # obtener o crear el folder de salida
    folder=get_or_create_output_folder()
    print("Se ha encontrado o creado la carpeta: "+folder)

    # descargar gatos
    download_cats(folder)

    # mostrar gatos
    show_cats()


if __name__ == '__main__':
    main()
