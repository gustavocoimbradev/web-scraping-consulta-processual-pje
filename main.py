from fastapi import FastAPI
import uvicorn
from playwright.async_api import async_playwright

app = FastAPI()

async def check(case_number: str):
    async with async_playwright() as p:

        # Acessa PJE
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context()
        page = await context.new_page()
        await page.goto("https://pje-consulta-publica.tjmg.jus.br/")

        # Preenche número do processo
        await page.fill(".campoProcessoConsultaPublica>.propertyView:first-of-type input", case_number)

        # Clica em consultar
        await page.click(".consulta-filtro .btn")

        # Navega até a janela de informações
        selector = ".rich-panel.col-sm-9 .btn"

        await page.wait_for_selector(selector, timeout = 10000)

        onclick_payload = await page.get_attribute(selector, "onclick")
        url_path = onclick_payload.split("'")[3]
        final_url = f"https://pje-consulta-publica.tjmg.jus.br{url_path}"

        await page.goto(final_url, wait_until="networkidle")

        # Informações

        informations = {}

        # Pega o polo ativo
        active_pole_element = await page.query_selector(".rich-tabpanel-content-position .rich-tabpanel-content > div:nth-of-type(1) span.text-bold")
        active_pole_text_content = await active_pole_element.text_content()
        if active_pole_text_content:
            active_pole_text = active_pole_text_content.strip()
            informations["Polo Ativo"] = active_pole_text

        # Pega o polo passivo
        active_pole_element = await page.query_selector(".rich-tabpanel-content-position .rich-tabpanel-content > div:nth-of-type(2) span.text-bold")
        active_pole_text_content = await active_pole_element.text_content()
        if active_pole_text_content:
            passive_pole_text = active_pole_text_content.strip()
            informations["Polo Passivo"] = passive_pole_text

        case_element_rows = await page.query_selector_all(".rich-tabpanel-content-position .rich-tabpanel-content > form table tr")

        for row in case_element_rows:
            case_element_columns = await row.query_selector_all("td") 
            for column in case_element_columns:
                column_title = await column.query_selector("div.name label")
                if column_title:
                    title_text = await column_title.text_content()
                column_value = await column.query_selector("div.value")
                if column_value:
                    value_text = await column_value.text_content()
                if title_text.strip() != "" and value_text.strip() != "":
                    informations[title_text.strip()] = value_text.strip()



        # Movimentações
        events_element = await page.query_selector_all(".rich-tabpanel-content-position .rich-tabpanel-content > div:nth-of-type(5) table tbody tr")
        events = []

        for event in events_element:
            event_title = await event.query_selector("td:nth-of-type(1) span")
            if event_title:
                title_text = await event_title.text_content()
                events.append(title_text.strip())

        # Documentos
        documents_element = await page.query_selector_all(".rich-tabpanel-content-position .rich-tabpanel-content > div:nth-of-type(6) table tbody tr")
        documents = []

        for document in documents_element:
            document_link = await document.query_selector("a")
            if (document_link):
                document_title = await document_link.text_content()
                document_onclick = await document_link.get_attribute("onclick")
                document_url = document_onclick.split("'")[3]
                if document_url == "about:blank":
                    docuemnt_href = await document_link.get_attribute("href")
                    document_url = f"https://pje-consulta-publica.tjmg.jus.br{docuemnt_href}"
                documents.append({"title": document_title.strip().replace("Visualizar documentos", ""), "url": document_url.strip()})


        # Fecha o browser
        await browser.close()

        return {
            "Informações": informations,
            "Movimentações": events,
            "Documentos": documents}


@app.get("/pje/{case_number}")
async def route(case_number: str):
    return await check(case_number)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)