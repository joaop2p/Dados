from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np
import uvicorn

# Carregando modelos e transformadores
kmeans = joblib.load("kmeans_model.pkl")
scaler = joblib.load("scaler.pkl")
label_encoders = joblib.load("label_encoders.pkl")

# Inicializando FastAPI
app = FastAPI()

# Modelo de dados esperado
class Cliente(BaseModel):
    idade: int
    sexo: str
    estado_civil: str
    renda_mensal: float
    cidade: str
    estado: str
    frequencia_compra_mensal: int
    ticket_medio: float
    categoria_preferida: str
    tempo_cliente: int
    utiliza_app: str
    participa_programa_fidelidade: str
    ultima_compra_dias: int
    forma_pagamento_preferida: str
    canal_compra_preferido: str

# Mapeamento descritivo dos clusters (exemplo, personalize conforme sua análise)
clusters_descricao = {
    0: "Clientes fiéis com alta renda e ticket médio elevado",
    1: "Clientes ocasionais com baixa fidelidade",
    2: "Clientes digitais com preferência por app e Pix",
    3: "Clientes tradicionais que compram na loja física",
    4: "Clientes novos com padrões de compra variados"
}

# Rota para prever o cluster
@app.post("/prever_cluster")
def prever_cluster(cliente: Cliente):
    dados_dict = cliente.dict()

    # Codificando atributos categóricos
    for col in label_encoders:
        if dados_dict[col] not in label_encoders[col]:
            return {"erro": f"Valor desconhecido para a coluna '{col}': {dados_dict[col]}"}
        dados_dict[col] = label_encoders[col][dados_dict[col]]

    # Transformando em array e escalando
    features = np.array([list(dados_dict.values())])
    features_scaled = scaler.transform(features)

    # Predição do cluster
    cluster = int(kmeans.predict(features_scaled)[0])
    descricao = clusters_descricao.get(cluster, "Cluster não identificado")

    return {
        "cluster": cluster,
        "descricao": descricao
    }

# Para executar localmente:
# uvicorn nome_do_arquivo:app --reload
