
---

# Segmentação de Nicho de Consumidores com K-Means e DBScan

Este projeto utiliza a biblioteca [Streamlit](https://streamlit.io/) para criar uma aplicação interativa que realiza a segmentação de nichos de consumidores utilizando os algoritmos de clusterização **K-Means** e **DBScan**. O objetivo é agrupar consumidores com base em três características principais: idade, renda anual e score de gasto, e visualizá-los graficamente.

## Funcionalidades

- Carregamento de um conjunto de dados em formato `.csv` com informações dos consumidores.
- Clusterização utilizando **K-Means** com seleção interativa do número de clusters.
- Clusterização utilizando **DBScan** com configuração interativa do raio de proximidade (EPS) e número mínimo de amostras.
- Visualização dos clusters em gráficos 2D para facilitar a análise.
- Exibição de métricas estatísticas, como média e desvio padrão, para cada cluster.
- Identificação do cluster com a menor dispersão (variabilidade) entre as características analisadas.

## Como Executar o Projeto

1. **Clone o Repositório**

   ```bash
   git clone https://github.com/SEU_USUARIO/NOME_DO_REPOSITORIO.git
   cd NOME_DO_REPOSITORIO
   ```

2. **Instale as Dependências**

   Certifique-se de ter o Python instalado. Para instalar as dependências, execute:

   ```bash
   pip install -r requirements.txt
   ```

3. **Prepare os Dados**

   O arquivo de dados `Dados.csv` deve conter as colunas:
   - `Age` (Idade)
   - `Annual Income (k$)` (Renda Anual em milhares de dólares)
   - `Spending Score (1-100)` (Score de Gasto entre 1 e 100)

   Coloque esse arquivo na mesma pasta do código ou ajuste o caminho no código caso esteja em outro diretório.

4. **Execute a Aplicação**

   Para iniciar a aplicação no Streamlit, execute:

   ```bash
   streamlit run nome_do_arquivo.py
   ```

5. **Interaja com a Aplicação**

   - Carregue os dados e visualize as primeiras linhas.
   - Escolha entre os algoritmos **K-Means** e **DBScan**.
   - Para o **K-Means**, ajuste o número de clusters desejados.
   - Para o **DBScan**, ajuste o raio de proximidade (EPS) e o número mínimo de amostras.
   - Visualize os clusters gerados e explore as métricas de cada grupo.

## Bibliotecas Utilizadas

- **Streamlit**: Framework para criação de aplicações web interativas em Python.
- **Pandas**: Manipulação e análise de dados.
- **Scikit-learn**: Implementação dos algoritmos de clusterização (K-Means e DBScan).
- **Matplotlib**: Criação de gráficos e visualizações.
- **Seaborn**: Biblioteca para visualizações baseadas no Matplotlib.

## Possíveis Melhorias

- Incluir opções para carregar dados de outros formatos (e.g., Excel).
- Adicionar mais algoritmos de clusterização para comparar os resultados.
- Implementar uma análise mais detalhada dos clusters, como o perfil de consumo por cluster.

---

