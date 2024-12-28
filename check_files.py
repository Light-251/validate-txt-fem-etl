import os
import zipfile

def validate_files_in_zips(directory):
    """
    Controlla i file .txt contenuti negli archivi ZIP in una directory.
    Verifica se il contenuto del file .txt è diverso da 'validation-ok'.

    :param directory: Percorso della directory contenente gli archivi ZIP.
    """
    print("Avvio del programma di validazione...")
    invalid_files = []

    for filename in os.listdir(directory):
        if filename.endswith(".zip"):
            zip_path = os.path.join(directory, filename)

            try:
                with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                    for file_name in zip_ref.namelist():
                        if file_name.endswith(".txt"):
                            with zip_ref.open(file_name) as file:
                                content = file.read().decode('utf-8').strip()
                                if content != "validation-ok":
                                    print(f"Il file {file_name} in {filename} ha un contenuto non valido: {content}")
                                    invalid_files.append((filename, file_name, content))
                                else:
                                    print(f"Il file {file_name} in {filename} è valido.")
            except zipfile.BadZipFile:
                print(f"Errore: {filename} non è un file ZIP valido.")

    if invalid_files:
        with open("invalid_files.txt", "a") as output_file:
            for zip_name, txt_name, txt_content in invalid_files:
                output_file.write(f"Archivio: {zip_name}\n")
                output_file.write(f"File: {txt_name}\n")
                output_file.write(f"Contenuto: {txt_content}\n")
                output_file.write("-" * 40 + "\n")
        print("Nomi degli archivi ZIP con contenuto non valido e i relativi contenuti salvati in 'invalid_files.txt'.")
    else:
        print("Nessun file con contenuto non valido trovato.")

if __name__ == "__main__":
    # Richiede il percorso della directory contenente gli archivi ZIP.
    # La directory dovrebbe contenere solo file ZIP, ognuno con file .txt al suo interno.
    directory_path = input("Inserisci il percorso della directory contenente gli archivi ZIP: ")
    validate_files_in_zips(directory_path)

    # Come usare il programma:
    # 1. Posizionare gli archivi ZIP contenenti file .txt in una directory.
    # 2. Eseguire lo script e fornire il percorso della directory al prompt.
    # 3. Il programma creerà (o aggiornerà) un file 'invalid_files.txt' contenente 
    #    i dettagli dei file con contenuti non validi.
    # Nota: I file validi avranno un messaggio nel log della console.
