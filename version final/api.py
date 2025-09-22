import json
from flask import Flask, request, jsonify, render_template_string, Response
import pandas as pd

app = Flask(__name__)


# --------------------------------------------------------------------------------------------------------------------------
#                               Atletas con cierto NOC a partir de los datos limpios 
# --------------------------------------------------------------------------------------------------------------------------


def calcular_atletas_noc(data_clean, noc):
    col=["Nombre", "Deporte", "Medalla","NOC"]
    dir="./data"
    # Dataframe relacion NOC y Paises
    
    data_paises =  pd.read_csv(dir+"/"+"noc_regions.csv")
    data_paises["país"]=data_paises["notes"]
    data_paises["país"]=data_paises["país"].fillna(data_paises["region"])
    data_paises=data_paises.drop(columns=["region","notes"])

    athlete_data_by_noc=data_clean.loc[data_clean["NOC"]==noc, col]
    athlete_data_by_noc=athlete_data_by_noc.merge(data_paises, how="left", on="NOC")
    return athlete_data_by_noc

# --------------------------------------------------------------------------------------------------------------------------
#                                              KPI 
# --------------------------------------------------------------------------------------------------------------------------

def calcular_kpi(data_clean):
    # Obtener los 3 deportes más populares
    cond1=data_clean["Año"]>=2000
    cond2=data_clean["Temporada"]=="Summer"

    popularidad_deportes=(data_clean.loc[(cond1 & cond2) ,:]
                                                        .groupby(by=["Deporte"])
                                                        .agg(conteo_atletas=("Deporte", "count"))
                                                        .reset_index()
                                                        .sort_values(by="conteo_atletas", ascending=False)
    )
    top_3_deportes=popularidad_deportes["Deporte"].head(3).values

    # Obtener la edad promedio de los atletas ganadores del oro ...
    cond1=data_clean["Medalla"]=="Gold"
    cond2=data_clean["Año"]>=2000
    cond3=data_clean["Temporada"]=="Summer"
    cond4=data_clean["Deporte"].isin(top_3_deportes)

    prom_edad_top_3_deportes=round(data_clean[(cond1 & cond2 & cond3 & cond4 )].groupby(by="Deporte").agg(prom_edad=("Edad","mean")).reset_index(),2)
    return prom_edad_top_3_deportes


@app.route("/athlete_data_by_noc", methods=["GET"])
def get_atletas_noc():
    noc = request.args.get("noc")  # Parámetro de consulta ?noc=CHI
    dir="./results"
    # Dataframe con los datos limpios
    data_clean = pd.read_csv(dir+"/"+"cleaned_olympic_data.csv", encoding="latin1")

    # Validación del NOC
    if not noc:
        return jsonify({"error": "Debes pasar el parámetro noc"}), 400

    athlete_data_by_noc = calcular_atletas_noc(data_clean, noc)

    # Ordenar json
    result_json = json.dumps(
                            athlete_data_by_noc.to_dict(orient="records"),
                            ensure_ascii=False,   
                            indent=2,             
    )

    return Response(result_json, mimetype="application/json; charset=utf-8")


@app.route("/kpi", methods=["GET"])
def get_kpi():
    # Dataframe con los datos limpios
    dir="./results"
    data_clean = pd.read_csv(dir+"/"+"cleaned_olympic_data.csv", encoding="latin1")
    kpi = calcular_kpi(data_clean)

    # Ordenar json
    result_json = json.dumps(
                            kpi.to_dict(orient="records"),
                            ensure_ascii=False,   
                            indent=2,             
    )

    return Response(result_json, mimetype="application/json; charset=utf-8")


@app.route("/", methods=["GET"])
def home_html():
    endpoint1="/athlete_data_by_noc?noc=CHI"
    endpoint2="/kpi"
    
    html = f"""
    <h1>API de Atletas Olímpicos</h1>
    <p>Bienvenido/a. Puedes probar los siguientes endpoints:</p>
    <ul>
         <li><a href={endpoint1}> "/athlete_data_by_noc?noc=CHI" </a> → Atletas de Chile</li>
        <li> <a href={endpoint2}>  "/kpi                       " </a> → KPI de atletas</li>
    </ul>
    """
    return render_template_string(html)

if __name__ == "__main__":
    app.run(debug=True)
