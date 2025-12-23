# ⚖️ Consulta Processual PJe

> API ágil e eficiente para consulta pública de processos judiciais no sistema PJe.

Bem-vindo ao **Consulta Processual**, uma solução robusta baseada em **FastAPI** e **Playwright** projetada para automatizar a extração de dados públicos de sistemas PJe (Processo Judicial Eletrônico).

---

## 🚀 Funcionalidades

Este projeto oferece uma API simples para acessar dados complexos:

- **🔍 Coleta de Metadados**: Extrai automaticamente Polo Ativo, Polo Passivo, Juízo, Classe, e outros detalhes vitais do processo.
- **📜 Histórico de Movimentações**: Recupera a lista completa de andamentos processuais.
- **📂 Acesso a Documentos**: Gera links diretos para visualização de documentos anexados.
- **⚡ Alta Performance**: Utiliza execução assíncrona para respostas rápidas.
- **🐳 Docker Ready**: Ambiente containerizado configurado para deploy imediato.

## 🛠️ Tech Stack

Construído com tecnologias modernas para garantir estabilidade e escalabilidade:

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Playwright](https://img.shields.io/badge/Playwright-2EAD33?style=for-the-badge&logo=playwright&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)

## 🏁 Como Iniciar

Você pode rodar este projeto localmente ou em um container Docker.

### 🏠 Execução Local

1. **Clone o repositório e instale as dependências Python:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Instale as dependências do browser (Chromium):**
   ```bash
   playwright install chromium
   ```

3. **Inicie o servidor:**
   ```bash
   python main.py
   ```
   🚀 O servidor estará rodando em: `http://localhost:8000`

### 🐳 Execução via Docker (Recomendado)

Se você possui Node.js instalado, utilize os scripts facilitadores do `package.json`:

| Ação | Comando | Descrição |
| :--- | :--- | :--- |
| **Iniciar** | `npm run docker-start` | Compila a imagem e inicia o container na porta 8000. |
| **Parar** | `npm run docker-stop` | Para o container em execução. |
| **Reiniciar** | `npm run docker-restart` | Para, remove e recria o container do zero. |

> Alternativamente, você pode usar comandos Docker nativos (`docker build` e `docker run`) conforme definido no script.

## 🔌 Documentação da API

### Consultar Processo

Recupera todas as informações disponíveis para um número de processo.

**Endpoint:**
`GET /pje/{numero_do_processo}`

**Exemplo de Requisição:**
```bash
curl http://localhost:8000/pje/5009028-56.2023.8.13.0145
```

**Formato da Resposta:**
```json
{
  "Informações": {
    "Polo Ativo": "Fulano de Tal",
    "Polo Passivo": "Empresa X",
    "Classe": "Procedimento Comum Cível",
    ...
  },
  "Movimentações": [
    "Expedição de documento",
    "Conclusos para despacho",
    ...
  ],
  "Documentos": [
    {
      "title": "Petição Inicial",
      "url": "https://..."
    },
    ...
  ]
}
```

---

<div align="center">
  <sub>Desenvolvido com foco em automação jurídica.</sub>
</div>
