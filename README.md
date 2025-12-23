# Consulta Processual PJe

API para consulta pública de processos judiciais em sistemas PJe, desenvolvida com FastAPI e Playwright.

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
curl http://localhost:8000/pje/5000680-02.2025.8.13.0707
```

**Exemplo de Resposta:**

```json
{
  "Informações": {
    "Polo Ativo": "GUSTAVO LIMA COIMBRA - CPF: 135.351.516-86 (RECORRENTE)",
    "Polo Passivo": "EBAZAR.COM.BR. LTDA - CNPJ: 03.007.331/0001-41 (RECORRIDO(A))",
    "Número Processo": "5000680-02.2025.8.13.0707",
    "Data da Distribuição": "20/01/2025",
    "Classe Judicial": "[CÍVEL] PROCEDIMENTO DO JUIZADO ESPECIAL CÍVEL (436)",
    "Assunto": "DIREITO CIVIL (899)  -  Responsabilidade Civil (10431)  -  Indenização por Dano Moral (10433\n    DIREITO DO CONSUMIDOR (1156)  -  Responsabilidade do Fornecedor (6220)  -  Rescisão do contrato e devolução do dinheiro (7768",
    "Jurisdição": "Varginha - Juizado Especial",
    "Órgão Julgador": "Unidade Jurisdicional Cível - 1º JD da Comarca de Varginha"
  },
  "Movimentações": [
    "16/06/2025 12:04:36 - Arquivado Definitivamente",
    "16/06/2025 12:04:14 - Expedição de Certidão Trânsito em Julgado.",
    "22/05/2025 00:27:26 - Decorrido prazo de GUSTAVO LIMA COIMBRA em 21/05/2025 23:59.",
    "..."
  ],
  "Documentos": [
    {
      "title": "24/03/2025 13:31:01 - Projeto de Sentença-Jesp (Projeto de Sentença-Jesp)",
      "url": "https://pje-consulta-publica.tjmg.jus.br:443/pje/ConsultaPublica/DetalheProcessoConsultaPublica/documentoSemLoginHTML.seam?ca=..."
    },
    {
      "title": "20/03/2025 15:40:55 - ATA - (11) (Ata de Audiência (Sem Sentença))",
      "url": "https://pje-consulta-publica.tjmg.jus.br/pje/ConsultaPublica/DetalheProcessoConsultaPublica/listView.seam?idBin=..."
    }
  ]
}
```
