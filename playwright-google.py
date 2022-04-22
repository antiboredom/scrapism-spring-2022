from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://google.com")
    page.fill("input.gLFyf", "how do i")
    page.keyboard.press("Enter")

    page.wait_for_timeout(10000)

    browser.close()