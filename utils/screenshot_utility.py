import os
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont


class ScreenshotUtility:
    def __init__(self, driver, screenshots_dir="screenshots"):
        self.driver = driver
        self.screenshots_dir = screenshots_dir
        self._create_screenshots_directory()

    def _create_screenshots_directory(self):
        if not os.path.exists(self.screenshots_dir):
            os.makedirs(self.screenshots_dir)

    def _generate_filename(self, test_name):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        clean_name = test_name.replace("::", "_").replace("/", "_").replace("\\", "_")
        clean_name = "".join(
            c if c.isalnum() or c in (' ', '_', '-') else '_' for c in clean_name
        )

        return f"FAILED_{clean_name}_{timestamp}.png"

    def _add_banner(self, screenshot_path, error_message):
        try:
            img = Image.open(screenshot_path)
            width, height = img.size
            banner_height = 60

            # Create new image with red banner
            new_img = Image.new('RGB', (width, height + banner_height), color='#FF0000')
            new_img.paste(img, (0, banner_height))

            draw = ImageDraw.Draw(new_img)

            # Load font
            try:
                font = ImageFont.truetype("arial.ttf", 20)
            except:
                font = ImageFont.load_default()

            # Draw banner text
            draw.text((10, 10), "TEST FAILED", fill='white', font=font)
            draw.text((10, 35), error_message[:100], fill='white', font=font)

            new_img.save(screenshot_path)

        except Exception as e:
            print(f"Could not add banner: {str(e)}")

    def take_failure_screenshot(self, test_name, error_message):
        filename = self._generate_filename(test_name)
        filepath = os.path.join(self.screenshots_dir, filename)

        try:
            self.driver.save_screenshot(filepath)
            self._add_banner(filepath, error_message)
            print(f"✓ Screenshot saved: {filepath}")
            return filepath

        except Exception as e:
            print(f"✗ Failed to take screenshot: {str(e)}")
            return None
