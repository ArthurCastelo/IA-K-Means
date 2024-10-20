import streamlit as st
import pandas as pd
from sklearn.cluster import KMeans, DBSCAN
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler

# Título do aplicativo
st.title("Segmentação de Nicho de Consumidores com K-Means e DBScan")

# Carregar dados
@st.cache_data
def load_data():
    try:
        df = pd.read_csv('Dados.csv')  # Substitua com o caminho correto
        return df
    except Exception as e:
        st.error(f"Erro ao carregar os dados: {e}")
        return None

df = load_data()

if df is not None:
    st.write("Dados dos Clientes:", df.head())

    # Selecionar colunas relevantes para o clustering
    features = df[['Age', 'Annual Income (k$)', 'Spending Score (1-100)']]

    # Padronizar os dados para DBScan
    scaler = StandardScaler()
    scaled_features = scaler.fit_transform(features)

    # Escolher o algoritmo de clusterização
    alg_choice = st.selectbox("Escolha o algoritmo de clusterização:", ["K-Means", "DBScan"])

    if alg_choice == "K-Means":
        # Definir o número de clusters
        num_clusters = st.slider("Número de clusters (K-Means)", 2, 10, 3)

        # Aplicar K-Means
        kmeans = KMeans(n_clusters=num_clusters)
        df['Cluster'] = kmeans.fit_predict(features)

        # Visualizar clusters com K-Means
        st.subheader(f"Visualização dos Clusters com {num_clusters} Clusters (K-Means)")
        fig, ax = plt.subplots(figsize=(8, 6))
        scatter = ax.scatter(df['Annual Income (k$)'], df['Spending Score (1-100)'], c=df['Cluster'], cmap='viridis')
        ax.set_xlabel('Renda Anual (k$)')
        ax.set_ylabel('Score de Gasto')
        st.pyplot(fig)

    elif alg_choice == "DBScan":
        # Definir os parâmetros para DBScan
        eps = st.slider("Raio de proximidade (EPS) para DBScan", 0.1, 5.0, 1.0)
        min_samples = st.slider("Número mínimo de amostras para DBScan", 1, 20, 5)

        # Aplicar DBScan
        dbscan = DBSCAN(eps=eps, min_samples=min_samples)
        df['Cluster'] = dbscan.fit_predict(scaled_features)

        # Visualizar clusters com DBScan
        st.subheader(f"Visualização dos Clusters com DBScan (EPS={eps}, Min Samples={min_samples})")
        fig, ax = plt.subplots(figsize=(8, 6))
        scatter = ax.scatter(df['Annual Income (k$)'], df['Spending Score (1-100)'], c=df['Cluster'], cmap='plasma')
        ax.set_xlabel('Renda Anual (k$)')
        ax.set_ylabel('Score de Gasto')
        st.pyplot(fig)

    # Mostrar os resultados filtrando apenas as colunas numéricas
    st.subheader("Médias e Dispersão dos Clusters")
    numeric_columns = df.select_dtypes(include=['int64', 'float64']).columns

    # Calcular médias e desvio padrão por cluster
    means = df.groupby('Cluster')[numeric_columns].mean()
    std_devs = df.groupby('Cluster')[numeric_columns].std()

    # Combinar médias e desvios padrão em um único DataFrame
    summary = pd.concat([means, std_devs], axis=1)
    summary.columns = pd.MultiIndex.from_product([['Média', 'Desvio Padrão'], numeric_columns])

    # Encontrar o cluster com a menor dispersão em cada variável
    min_dispersion = std_devs.idxmin()
    
    # Exibir a tabela de médias e desvios padrão
    st.dataframe(summary)

    # Exibir qual cluster possui a menor dispersão
    st.subheader("Cluster com Menor Dispersão")
    st.write(f"O cluster com a menor dispersão é: {min_dispersion}")
else:
    st.error("Falha ao carregar os dados.")
