import shutil
import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from googletrans import Translator
import logging


def main():
    # Configure logging settings
    logging.basicConfig(
        filename='my_script.log',
        level=logging.DEBUG,  # Set the logging level to capture all messages
        format='%(asctime)s - %(levelname)s - %(message)s'
    )
    logger = logging.getLogger()

    url = input("Enter The Novel base chapter link: ")
    start_chapter = input("Enter the chapter number to start with: ")

    options = webdriver.FirefoxOptions()
    options.set_preference("dom.webdriver.enabled", False)
    options.set_preference("dom.webnotifications.enabled", False)
    options.set_preference("intl.accept_languages", "en-US, en")
    options.headless = False  # Change to True if you want to run headless

    driver = webdriver.Firefox(options=options)

    try:
        driver.get(url)
        # driver.find_element(By.CSS_SELECTOR, "#clicktoexp").click()
        # Attempt to get novel name from the selector with ID 'book_name2'
        try:
            book_name_element = driver.find_element(By.ID, 'book_name2')
            novel_name = book_name_element.text.strip().replace(":", "").replace("?", "").replace("<", "").replace(">", "")
            translator = Translator()
            chapter_directory  = translator.translate(novel_name, dest="en", src='vi').text
        except NoSuchElementException:
            chapter_directory = input("Enter the name of the chapter directory: ")

        # Create the main directory if it does not exist
        novel_chapter_directory = os.path.join(os.getcwd(), chapter_directory)
        if not os.path.exists(novel_chapter_directory):
            os.makedirs(novel_chapter_directory, exist_ok=True)

        translator = Translator()

        chapters_elements = driver.find_elements(By.CSS_SELECTOR, "a.listchapitem")
        chapters_list = []
        for element in chapters_elements:
            chapters_list.append(element.text)
            print(element.text)

        logger.debug(chapters_list)

        print(chapters_list)

        chapters_dict = dict()

        for chapter in chapters_list:
            split_result = chapter.split(':')
            if len(split_result) > 1:
                id = split_result[0].strip().replace("Chương ", "")
                value = split_result[1].strip()
                if id.isdigit():
                    chapters_dict.update({id: value})
                else:
                    continue

        print(chapters_dict)

        # Sort chapters_dict in ascending order based on keys
        sorted_chapters = dict(sorted(chapters_dict.items(), key=lambda x: int(x[0])))

        for elem in sorted_chapters:
            if int(elem) >= int(start_chapter):
                chapter_id = elem

                logger.info(f"Processing chapter {chapter_id}: {chapters_dict[elem]}")
                try:
                    chapter_element = driver.find_element(By.PARTIAL_LINK_TEXT, chapters_dict[elem])
                    if chapter_element.is_displayed() and chapter_element.is_enabled():
                        chapter_element.click()
                        logger.info("Clicked successfully")
                        time.sleep(3)
                    else:
                        logger.error("Element found but not clickable")
                except Exception as e:
                    logger.error(f"Element not found or clickable: {e}")

                time.sleep(3)

                novel_text = driver.find_element(By.CSS_SELECTOR, "#content-container").text.replace(
                    "@Bạn đang đọc bản lưu trong hệ thống\n\n",
                    "") + "\n\nThank you for reading this story at Novelsemperor.com. Your support enables us to keep the site running!"
                logger.debug(novel_text)
                chunks_for_translate = [novel_text[i:i + 4500] for i in range(0, len(novel_text), 4500)]

                for line in chunks_for_translate:
                    translate_result = translator.translate(line, dest="en", src='vi').text
                    file_path = os.path.join(novel_chapter_directory, f"{chapter_id}.txt")
                    with open(file_path, mode='a', encoding='utf-8') as f:
                        f.write(translate_result)

                logger.info(f'Chapter {chapter_id} - DONE!')
                driver.execute_script("window.history.go(-1)")
                WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#clicktoexp"))).click()
                time.sleep(3)
    except Exception as ex:
        logger.error(f"An error occurred: {ex}")
    finally:
        driver.close()
        driver.quit()
        print("Novel Save Successfully")


if __name__ == '__main__':
    main()
