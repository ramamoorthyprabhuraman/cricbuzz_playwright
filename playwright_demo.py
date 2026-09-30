from playwright.sync_api import sync_playwright
from datetime import datetime

print("Starting the Playwright script...")
print(f"Current date and time: {datetime.now()}")

# Daily Live Scores
# Chromium --> Cricbuzz --> Live Scores --> Extract page content
# --> Screenshot --> Final text file

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    # 1. Navigation to Cricbuzz
    page.goto(
        "https://www.cricbuzz.com",
        wait_until="domcontentloaded"
    )

    page.screenshot(path="cricbuzz.png")

    print("Cricbuzz opened successfully.")

    # 2. Open Live Scores
    page.goto(
        "https://www.cricbuzz.com/cricket-match/live-scores",
        wait_until="domcontentloaded"
    )

    # Wait until the URL contains live-scores
    page.wait_for_url("**/cricket-match/live-scores")

    page.screenshot(path="cricbuzz_live_scores.png")

    print("Live Scores page opened successfully.")


    # 3. Extract visible page text
    page_content = page.locator("body").inner_text()

    # 4. Add date and time
    current_datetime = datetime.now()

    final_content = (
        "CRICBUZZ DAILY LIVE SCORES\n"
        "============================\n"
        f"Date and Time: {current_datetime}\n\n"
        f"{page_content}"
    )

    # 5. Save to text file
    with open(
        "cricbuzz_live_scores.txt",
        "w",
        encoding="utf-8"
    ) as f:
        f.write(final_content)

    print(
        "Live scores extracted and saved to "
        "cricbuzz_live_scores.txt"
    )

    browser.close()

    print("Script completed successfully.")
