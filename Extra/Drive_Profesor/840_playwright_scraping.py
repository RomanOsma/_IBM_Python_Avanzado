from playwright.sync_api import sync_playwright

url = 'https://midu.dev'

with sync_playwright() as p:
  browser = p.chromium.launch(headless=False, slow_mo=2000)
  page = browser.new_page()
  page.goto(url)

  first_article_anchor = page.locator('article a').first
  print(first_article_anchor.text_content())
  first_article_anchor.click()

  page.wait_for_load_state()

  curso_content_container = page.locator('text="Contenido del curso"')
  curso_content_sibling = curso_content_container.locator('xpath=./div/')

  browser.close()