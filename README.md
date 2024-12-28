# Validatore di file .txt negli archivi ZIP

Questo script Python consente di verificare i file `.txt` contenuti in archivi ZIP in una directory. Se il contenuto dei file non corrisponde alla stringa `validation-ok`, i dettagli dei file non validi vengono registrati in un file `invalid_files.txt`.

## Funzionalità

- Analisi automatica degli archivi ZIP in una directory specificata.
- Controllo del contenuto dei file `.txt` per identificare quelli non validi.
- Salvataggio del nome dell'archivio, del file e del contenuto non valido in un report dettagliato.

## Come utilizzare

1. Posizionare gli archivi ZIP contenenti file `.txt` in una directory.
2. Eseguire lo script e fornire il percorso della directory al prompt.
3. Controllare la console per i messaggi di log e il file `invalid_files.txt` per i dettagli dei file non validi.

## Requisiti

- Python 3.x
- Modulo `zipfile` (incluso nella libreria standard di Python)

## Note

- Il file `invalid_files.txt` verrà aggiornato con i nuovi risultati, senza sovrascrivere i dati già presenti.
- I file validi vengono segnalati tramite messaggi di log sulla console.

## Esecuzione

Per avviare lo script, eseguire il seguente comando in un terminale:

```bash
python nome_script.py
```

## Esempio di output

Esempio di contenuto generato in `ivnalid_files.txt`

```bash
Archivio: esempio.zip
File: esempio.txt
Contenuto: errore di validazione
----------------------------------------
