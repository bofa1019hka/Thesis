import importlib

def apply_imputation(data, imputation_map):
    # Geht alle Kombinationen der impulation_map durch (bspw. "meterStart": "processing.completion.meterStart")
    for field, func_path in imputation_map.items():
        #Trenne den Pfad auf. Module_path ist der Pfad zur Datei und module der Modulname. Beim ersten . von rechts trennen
        module_path, func_name = func_path.rsplit(".", 1)
        # Import der Datei
        module = importlib.import_module(module_path)
        # Import der Funktion
        func = getattr(module, func_name)
        # Aufruf der Funktion mit den Daten
        data = func(data, field)
    return data