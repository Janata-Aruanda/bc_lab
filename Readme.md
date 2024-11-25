# Arquitetura da pipeline
![](/img/arq.png)

## Comentario

Ao salvar os dados no dw pensei em deixa um backup em formato de arquivo parquet, mas acabei não realizando essa etapa
# Introdução

Foi desenvolvido um script para a pipeline de dados com o objetivo de testar minhas habilidades no desenvolvimento de soluções analíticas. Foram utilizadas tecnologias open source para essa atividade. Durante o processo, foi realizada uma requisição para baixar o arquivo de um repositório. Como os dados estavam em formato semi-estruturado, foi necessário extrair as principais informações utilizando Python. Em seguida, os dados foram normalizados com a biblioteca Pandas e carregados para um data warehouse simples


# Para ativar o ambiente variavel

```
.\.cb_lab\Scripts\Activate.ps1 
```

# Para instalar as depências para o ambiente

```
pip install -r requirements.txt
```

