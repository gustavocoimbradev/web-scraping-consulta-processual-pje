# web-scraping-consulta-processual-pje

API de **Web Scraping** para consulta pública de processos judiciais em sistemas PJe, desenvolvida com FastAPI e Playwright.

Esta ferramenta realiza a extração automatizada de dados diretamente do portal público do tribunal, simulando a navegação de um usuário real para obter informações detalhadas do processo, movimentações e documentos.

## Como Usar

### Execução via Docker

Utilize os scripts configurados no `package.json`:

*   **Iniciar**: `npm run docker-start` (Disponibiliza a API na porta 8000)
*   **Parar**: `npm run docker-stop`
*   **Reiniciar**: `npm run docker-restart`

### Execução Local

1.  Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```
2.  Instale o navegador necessário:
    ```bash
    playwright install chromium
    ```
3.  Inicie o servidor:
    ```bash
    python main.py
    ```

---

## API

### Consultar Processo

**Endpoint:** `GET /pje/{numero_do_processo}`

**Exemplo de uso:**
```bash
curl http://localhost:8000/pje/5000000-00.2025.8.13.0000
```

**Exemplo de Resposta:**

```json
{
  "Informações": {
    "Polo Ativo": "FULANO DE TAL - CPF: 000.000.000-00 (RECORRENTE)",
    "Polo Passivo": "EMPRESA EXEMPLO LTDA - CNPJ: 00.000.000/0001-00 (RECORRIDO(A))",
    "Número Processo": "5000000-00.2025.8.13.0000",
    "Data da Distribuição": "20/01/2025",
    "Classe Judicial": "[CÍVEL] PROCEDIMENTO DO JUIZADO ESPECIAL CÍVEL (436)",
    "Assunto": "DIREITO CIVIL (899)  -  Responsabilidade Civil (10431)  -  Indenização por Dano Moral (10433)",
    "Jurisdição": "Comarca de Exemplo - Juizado Especial",
    "Órgão Julgador": "Unidade Jurisdicional Cível - 1º JD da Comarca de Exemplo"
  },
  "Movimentações": [
    "16/06/2025 12:04:36 - Arquivado Definitivamente",
    "16/06/2025 12:04:14 - Expedição de Certidão Trânsito em Julgado.",
    "22/05/2025 00:27:26 - Decorrido prazo de FULANO DE TAL em 21/05/2025 23:59.",
    "..."
  ],
  "Documentos": [
    {
      "title": "24/03/2025 13:31:01 - Projeto de Sentença-Jesp (Projeto de Sentença-Jesp)",
      "url": "https://pje-consulta-publica.tjmg.jus.br:443/pje/ConsultaPublica/..."
    },
    {
      "title": "20/03/2025 15:40:55 - ATA - (11) (Ata de Audiência (Sem Sentença))",
      "url": "https://pje-consulta-publica.tjmg.jus.br/pje/ConsultaPublica/..."
    }
  ]
}
```
