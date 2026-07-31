import re
from playwright.sync_api import sync_playwright

SEEDS = ["46", "47", "48", "49", "50", "51", "52", "53", "54", "55"]  # your assigned seeds


def main():
    total = 0.0
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        for seed in SEEDS:
            url = f"https://sanand0.github.io/tdsdata/js_table/?seed={seed}"
            print(f"Scraping {url} ...")
            page.goto(url, wait_until="networkidle")
            page.wait_for_selector("table")

            cells = page.locator("table td").all_inner_texts()
            seed_sum = 0.0
            for cell_text in cells:
                match = re.search(r"-?\d+(\.\d+)?", cell_text.strip())
                if match:
                    seed_sum += float(match.group())

            print(f"  seed={seed} subtotal={seed_sum}")
            total += seed_sum
        browser.close()

    int_total = int(round(total))
    print(f"TOTAL_SUM={int_total}")


if __name__ == "__main__":
    main()
