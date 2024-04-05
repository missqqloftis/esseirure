from selenium.webdriver.common.by import By

def click_Xpath(driver, index, xpath):
    """Clicks on the element at the given index in the list of elements with the given xpath.

    Args:
        driver: The WebDriver instance.
        index: The index of the element to click on.
        xpath: The xpath of the elements.
    """
    elements = driver.find_elements(By.XPATH, xpath)
    elements[index].click()
