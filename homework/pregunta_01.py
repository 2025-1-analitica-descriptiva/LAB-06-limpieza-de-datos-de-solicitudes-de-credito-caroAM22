"""
Escriba el codigo que ejecute la accion solicitada en la pregunta.
"""


def pregunta_01():
    """
    Realice la limpieza del archivo "files/input/solicitudes_de_credito.csv".
    El archivo tiene problemas como registros duplicados y datos faltantes.
    Tenga en cuenta todas las verificaciones discutidas en clase para
    realizar la limpieza de los datos.

    El archivo limpio debe escribirse en "files/output/solicitudes_de_credito.csv"

    """

    import pandas as pd
    import os

    input_file = "files/input/solicitudes_de_credito.csv"
    output_file = "files/output/solicitudes_de_credito.csv"

    data = pd.read_csv(input_file, sep=";")

    data = data.dropna()
    data["sexo"] = data["sexo"].str.lower()
    data["tipo_de_emprendimiento"] = data["tipo_de_emprendimiento"].str.lower()

    data["idea_negocio"] = (
        data["idea_negocio"]
        .str.lower()
        .str.replace("_", " ", regex=False)
        .str.replace("-", " ", regex=False)
        .str.strip()
    )

    data["barrio"] = (
        data["barrio"]
        .str.lower()
        .str.replace("_", " ", regex=False)
        .str.replace("-", " ", regex=False)
    )

    def normalize_date(date):
        parts = date.split("/")
        if len(parts[0]) == 4:
            return f"{parts[2]}/{parts[1]}/{parts[0]}"
        return date

    data["fecha_de_beneficio"] = data["fecha_de_beneficio"].apply(normalize_date)

    data["monto_del_credito"] = (
        data["monto_del_credito"]
        .str.replace(" ", "", regex=False)
        .str.replace("$", "", regex=False)
        .str.replace(",", "", regex=False)
        .astype(float)
    )

    data["línea_credito"] = (
        data["línea_credito"]
        .str.lower()
        .str.replace("_", " ", regex=False)
        .str.replace("-", " ", regex=False)
    )

    unique_columns = [
        "sexo",
        "tipo_de_emprendimiento",
        "idea_negocio",
        "barrio",
        "estrato",
        "comuna_ciudadano",
        "fecha_de_beneficio",
        "monto_del_credito",
        "línea_credito",
    ]
    data = data.drop_duplicates(subset=unique_columns)

    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    data.to_csv(output_file, sep=";", index=False)


pregunta_01()
