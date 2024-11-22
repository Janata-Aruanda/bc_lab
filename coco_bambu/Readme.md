Configurar ambiente virtual
```
python -m venv .cb_lab
```

Ativar ambiente virtual
```
.\.cb_lab\Scripts\Activate.ps1
```


DESAFIO 1


[ESBOÇO](/img/esboco.png)


[NORMALIZACAO_DER](/img/der.png)

Estrutura do Projeto

COCO_BAMBU/
├── .cb_lab/             # Configurações específicas do ambiente
├── dados/               # Arquivos de dados brutos
│   ├── detail_lines.csv     # Linhas detalhadas de vendas
│   ├── guest_checks.csv     # Informações de contas de clientes
│   ├── menu_items.csv       # Dados dos itens do cardápio
│   ├── impostos.csv         # Dados de impostos
├── img/                 # Imagens e diagramas
│   ├── der.png              # Diagrama de Entidade-Relacionamento (DER)
│   ├── esboco.png           # Esboço do processo de ETL
├── scr/                 # Scripts do pipeline de ETL
│   ├── extract.py           # Script de extração dos dados
│   ├── load.py              # Script de carga dos dados no banco
│   ├── sql.py               # Queries SQL utilizadas no processo
│   ├── transform.py         # Script de transformação dos dados
├── .env                 # Arquivo de configuração do ambiente
├── bc_lab.db            # Banco de dados SQLite gerado
├── ERP.json             # Arquivo de configuração do ERP
├── Readme.md            # Documentação do projeto
├── requirements.txt     # Dependências do projeto

