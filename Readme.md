# Introdução

Este documento apresenta a solução para o Desafio de Engenharia de Dados proposto pela Coco Bambu em 2024. O desafio está dividido em duas etapas principais que simulam cenários reais enfrentados em uma rede de restaurantes.
A solução foi desenvolvida com base em boas práticas de engenharia de dados, visando escalabilidade, eficiência e clareza no processamento dos dados, usando tecnologias open-source.

# Objetivo

O objetivo deste projeto é demonstrar habilidades em modelagem de dados, design de pipelines de ingestão e armazenamento, e construção de soluções resilientes para manipulação de grandes volumes de dados em um ecossistema corporativo. A proposta também inclui o planejamento e justificativa técnica para cada etapa do processo, com foco na criação de sistemas prontos para produção.

## Desafio 

Desafio 1: Transformação de dados provenientes de um endpoint de API ERP em um esquema estruturado que suporte operações relacionadas ao negócio.

Desafio 2: Armazenamento e manipulação de respostas de APIs que fornecem dados financeiros e operacionais, com foco na criação de um pipeline eficiente e resiliente.


# Arquitetura da pipeline

A arquitetura proposta para o primeiro desafio foi projetada para executar as seguintes etapas de forma eficiente e escalável:
Realizar uma requisição ao endpoint da API REST utilizando Python para coletar os dados.
Transformar os dados recebidos em um formato estruturado que suporte consultas e análises.
Armazenar os dados transformados em um Data Warehouse para facilitar o acesso e a integração com ferramentas de inteligência de negócios.
Salvar os dados em um formato otimizado para armazenamento e processamento, garantindo eficiência no uso de recursos.

![](/img/arq.png)

### Comentário

Ao salvar os dados no dw pensei em deixa um backup em formato de arquivo parquet, mas acabei não realizando essa etapa

A arquitetura proposta para o segundo desafio foi desenvolvida com o objetivo de organizar e otimizar o armazenamento e a leitura dos dados. A abordagem adotada consiste em particionar os dados por ano, mês e dia, garantindo um acesso eficiente e estruturado, além de facilitar consultas e operações específicas sobre os dados armazenados.

![](/img/Untitled-2024-06-28-1436.png)

## Por que armazenar as respostas das APIs

Armazenar as respostas das APIs no data lake não apenas garante a preservação e acessibilidade dos dados, mas também suporta a evolução contínua dos processos analíticos. Permite responder rapidamente às demandas de negócio.

## Alterar campo na resposta da API

Implicaria na quebra do pipeline de dados e na necessidade de atualização do schema. Como consequência, os scripts que acessam o campo anterior precisarão ser refatorados para utilizar o novo nome

# Kanban
Neste desafio, utilizei a metodologia ágil em conjunto com o Kanban, utilizando a plataforma Trello para organizar e gerenciar as demandas.

![](/img/kanban.png)


## Gestão de Fluxo de Atividade

Esse desafio foi desenvolvida em etapas, seguindo uma gestão de fluxo para garantir a organização e o cumprimento dos prazos. Abaixo, o planejamento das atividades realizadas ao longo da semana

| Dia      | Atividade                                                                 |
|----------|---------------------------------------------------------------------------|
| **Segunda**  | Definir a estrutura do Data Lake (Desafio 2).                             |
| **Terça**    | Definir a estrutura do Data Lake (Desafio 2) e entender o caso de uso.    |
| **Quarta**   | Entender o caso de uso.                                                  |
| **Quinta**   | Entender o caso de uso e criação do repositório.                          |
| **Sexta**    | Criação do repositório.                                                  |
| **Sábado**   | Criação do pipeline ELT (Desafio 1).                                      |
| **Domingo**  | Finalizar a criação do pipeline ELT (Desafio 1) e entrega do desafio.     |


# Para ativar o ambiente variavel

```
.\.cb_lab\Scripts\Activate.ps1 
```

# Para instalar as depências para o ambiente

```
pip install -r requirements.txt
```

