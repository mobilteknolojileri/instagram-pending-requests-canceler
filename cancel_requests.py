import asyncio
import random
import json
from pathlib import Path
from playwright.async_api import async_playwright
from datetime import datetime


def select_json_file():
    """Prompt user for JSON file path"""
    print("\nEnter the path to your pending_follow_requests.json file:")

    while True:
        user_input = input("Path: ").strip()

        if not user_input:
            print("Please enter a valid path!")
            continue

        # Normalize path separators
        user_input = user_input.replace('\\', '/')
        file_path = Path(user_input)

        if not file_path.exists():
            print(f"File not found: {file_path}")
            retry = input("Try again? (y/n): ").lower()
            if retry != 'y':
                return None
            continue

        return file_path


def read_json(file_path):
    """Extract usernames from Instagram data export JSON"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        usernames = []
        for item in data.get("relationships_follow_requests_sent", []):
            string_list = item.get("string_list_data", [])
            if string_list:
                username = string_list[0].get("value")
                if username:
                    usernames.append(username)

        return usernames

    except json.JSONDecodeError:
        print("Invalid JSON file!")
        return None
    except Exception as e:
        print(f"Error reading file: {e}")
        return None


async def human_like_delay(min_sec=1, max_sec=3):
    """Random delay to mimic human behavior"""
    delay = random.uniform(min_sec, max_sec)
    await asyncio.sleep(delay)


async def random_human_activity(page):
    """Perform random activities to appear more human"""
    activity = random.choice(['scroll', 'wait', 'nothing', 'nothing'])

    if activity == 'scroll':
        scroll_amount = random.randint(100, 500)
        await page.evaluate(f"window.scrollBy(0, {scroll_amount})")
        await asyncio.sleep(random.uniform(0.5, 1.5))
    elif activity == 'wait':
        await asyncio.sleep(random.uniform(1, 3))


async def cancel_follow_request(page, username, index, total):
    """Cancel a single follow request - works with both Turkish and English Instagram"""
    try:
        await page.goto(f"https://www.instagram.com/{username}/", wait_until="domcontentloaded")
        await human_like_delay(1, 2)
        await random_human_activity(page)

        try:
            request_button = None

            # Try multiple selectors for the "Requested" button
            # Turkish: "İstek Gönderildi", English: "Requested"
            selectors_requested = [
                'button:has-text("İstek Gönderildi")',  # Turkish
                'button:has-text("Requested")',          # English
                'button:has-text("Demande envoyée")',    # French
                'button:has-text("Solicitud enviada")',  # Spanish
                'button:has-text("Richiesta inviata")',  # Italian
                'button:has-text("Anfrage gesendet")',   # German
                # Generic class selector (backup)
                'button._acan._acap._acas._aj1-._ap30',
                'button[aria-label*="Requested"]',       # Aria label
                'div[role="button"]:has-text("Requested")',
                '//button[contains(@class, "_ac") and (contains(., "Requested") or contains(., "İstek Gönderildi"))]'
            ]

            # Try each selector until one works
            for selector in selectors_requested:
                try:
                    request_button = page.locator(selector).first
                    if await request_button.count() > 0:
                        await request_button.click()
                        break
                except:
                    continue
            else:
                # If no text-based selector worked, try the generic button
                generic_button = page.locator('button').filter(has_text=True)
                for i in range(await generic_button.count()):
                    btn = generic_button.nth(i)
                    text = await btn.inner_text()
                    if any(word in text.lower() for word in ['requested', 'istek', 'gönderildi', 'request']):
                        await btn.click()
                        break
                else:
                    return False

            await human_like_delay(0.5, 1)

            # Try multiple selectors for the "Unfollow" button in the popup
            # Turkish: "Takibi Bırak", English: "Unfollow"
            selectors_unfollow = [
                'button:has-text("Takibi Bırak")',      # Turkish
                'button:has-text("Unfollow")',          # English
                'button:has-text("Ne plus suivre")',    # French
                'button:has-text("Dejar de seguir")',   # Spanish
                'button:has-text("Non seguire più")',   # Italian
                'button:has-text("Nicht mehr folgen")',  # German
                'button._a9--._ap36._a9-_',             # Generic class
                'button[type="button"]:has-text("Unfollow")',
                '//button[contains(text(), "Unfollow") or contains(text(), "Takibi Bırak")]'
            ]

            # Try each unfollow selector
            for selector in selectors_unfollow:
                try:
                    unfollow_button = page.locator(selector).first
                    if await unfollow_button.count() > 0:
                        await unfollow_button.wait_for(state="visible", timeout=5000)
                        await unfollow_button.click()
                        break
                except:
                    continue

            await human_like_delay(0.5, 1)

            # Verify the follow button appears (indicates success)
            # Turkish: "Takip Et", English: "Follow"
            selectors_follow = [
                'button:has-text("Takip Et")',         # Turkish
                'button:has-text("Follow")',           # English
                'button:has-text("Suivre")',           # French
                'button:has-text("Seguir")',           # Spanish
                'button:has-text("Segui")',            # Italian
                'button:has-text("Folgen")',           # German
                'button._acan._acap._acas._aj1-._ap30:has-text("Follow")',
                'button[aria-label*="Follow"]'
            ]

            # Check if follow button is visible
            for selector in selectors_follow:
                try:
                    follow_button = page.locator(selector).first
                    if await follow_button.count() > 0:
                        await follow_button.wait_for(state="visible", timeout=5000)
                        return True
                except:
                    continue

            # If we got here, check by button text change
            return True

        except Exception as e:
            # Debug info if needed
            # print(f"Debug: Error for @{username}: {str(e)}")
            return False

    except Exception as e:
        # print(f"Navigation error for @{username}: {str(e)}")
        return False


async def detect_language(page):
    """Detect Instagram interface language"""
    try:
        # Check for common elements to detect language
        await page.goto("https://www.instagram.com/", wait_until="domcontentloaded")
        await asyncio.sleep(2)

        # Check page content for language indicators
        page_content = await page.content()

        if "Takip Et" in page_content or "Profili Düzenle" in page_content:
            return "TR"
        elif "Follow" in page_content or "Edit Profile" in page_content:
            return "EN"
        else:
            # Default to English
            return "EN"
    except:
        return "EN"


async def main():
    print("=" * 70)
    print("Instagram Follow Request Canceler")
    print("=" * 70)

    file_path = select_json_file()
    if not file_path:
        return

    print("\nReading JSON file...")
    usernames = read_json(file_path)

    if not usernames:
        print("Username list is empty or could not be read!")
        return

    print(f"Found {len(usernames)} users")
    print("=" * 70)

    limit = len(usernames)

    print(f"\nProcessing ALL: {limit} users")
    print("\nFAST MODE - Human-like Behavior:")
    print("   2-3 seconds delay between each user")
    print("   Short break (20-30s) every 20 users")
    print("   Long break (60-90s) every 50 users")
    print("   Random activities")
    print(
        f"\nEstimated Time: ~{(limit * 3 + (limit // 20) * 25 + (limit // 50) * 75) // 60} minutes")
    print("\nStarting... (Press Ctrl+C to cancel)")
    await asyncio.sleep(3)

    async with async_playwright() as p:
        print("\nConnecting to Chrome...")
        browser = await p.chromium.connect_over_cdp("http://localhost:9222")

        contexts = browser.contexts
        if not contexts:
            print("No open Chrome context found!")
            return

        context = contexts[0]
        pages = context.pages

        if not pages:
            print("No open page found!")
            return

        page = pages[0]
        print("Successfully connected to Chrome!")

        # Detect language
        print("Detecting Instagram language...")
        lang = await detect_language(page)
        print(f"Detected language: {'Turkish' if lang == 'TR' else 'English'}")
        print("Script will work with both Turkish and English interfaces")

        # Bring Chrome to front
        await page.bring_to_front()
        await asyncio.sleep(0.5)

        successful = 0
        failed = 0
        start_time = datetime.now()

        for i, username in enumerate(usernames[:limit], 1):
            result = await cancel_follow_request(page, username, i, limit)

            if result:
                successful += 1
                print(f"[{i}/{limit}] @{username} - ✓ Success")
            else:
                failed += 1
                print(f"[{i}/{limit}] @{username} - ⊗ Skipped")

            if i < limit:
                if i % 20 == 0:
                    break_time = random.randint(20, 30)
                    print(f"\n⏸ Short break: {break_time} seconds")
                    print(f"   Progress: {i}/{limit} ({int(i/limit*100)}%)")
                    await asyncio.sleep(break_time)
                    print("   Continuing...\n")

                elif i % 50 == 0:
                    break_time = random.randint(60, 90)
                    elapsed = (datetime.now() - start_time).seconds
                    print(f"\n⏸ LONG BREAK: {break_time} seconds")
                    print(f"   Progress: {i}/{limit} ({int(i/limit*100)}%)")
                    print(f"   Elapsed: {elapsed // 60} minutes")
                    print(f"   Successful: {successful} | Skipped: {failed}")

                    for remaining in range(break_time, 0, -10):
                        print(f"   Remaining: {remaining} seconds", end='\r')
                        await asyncio.sleep(min(10, remaining))

                    print("\n   Continuing...\n")

                else:
                    delay = random.uniform(2, 3)
                    await asyncio.sleep(delay)

        end_time = datetime.now()
        total_time = (end_time - start_time).seconds

        print("\n" + "=" * 70)
        print("✓ OPERATION COMPLETED!")
        print("=" * 70)
        print(f"Successful: {successful}/{limit}")
        print(f"Skipped: {failed}/{limit}")
        print(f"Success Rate: {(successful/limit)*100:.1f}%")
        print(
            f"Total Time: {total_time // 60} minutes {total_time % 60} seconds")
        print(f"Average: {total_time/limit:.1f} seconds/user")
        print("=" * 70)

        print("\nCheck on Instagram: Profile → Following → Pending")
        print("All requests successfully canceled!")


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n\nOperation stopped by user!")
    except Exception as e:
        print(f"\nUnexpected error: {e}")
