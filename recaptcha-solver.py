from ibm_watson import SpeechToTextV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import urllib.request
import time
from random_username.generate import generate_username as rd




def voice_solver(random):
    apikey = 'AJkX0XwX5FdlwhpNJFBFcfr06feOxrO1uZPgPypBdwlc'
    url = 'https://api.us-south.speech-to-text.watson.cloud.ibm.com/instances/1906bf89-44a9-4a16-b92a-47abb56a5c51'
    authenticator = IAMAuthenticator(apikey)
    stt = SpeechToTextV1(authenticator=authenticator)
    stt.set_service_url(url)
    with open('voice/' + random + '.mp3', 'rb') as f:
        res = stt.recognize(audio=f, content_type='audio/mp3', model='en-US_NarrowbandModel',
                            continuous=True).get_result()
    output = res['results'][0]['alternatives'][0]['transcript']
    return output





def solver(driver,WebDriverWait,EC,By,NoSuchElementException):


    def solved_tick():
        try:
            driver.switch_to.default_content()
            WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it(
                (By.CSS_SELECTOR, "iframe[src^='https://www.google.com/recaptcha/api2/anchor?']")))
            time.sleep(4)
            driver.find_element_by_xpath("//span[@aria-checked='true']")
            driver.switch_to.default_content()
            return True

        except NoSuchElementException:
            return False


    WebDriverWait(driver, 40).until(EC.frame_to_be_available_and_switch_to_it(
        (By.CSS_SELECTOR, "iframe[src^='https://www.google.com/recaptcha/api2/anchor?']")))
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                                                "span.recaptcha-checkbox.goog-inline-block.recaptcha-checkbox-unchecked.rc-anchor-checkbox"))).click()

    driver.switch_to.default_content()


    WebDriverWait(driver, 40).until(EC.frame_to_be_available_and_switch_to_it(
        (By.CSS_SELECTOR, "iframe[src^='https://www.google.com/recaptcha/api2/bframe?']")))


    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "recaptcha-audio-button"))).click()
    driver.switch_to.default_content()
    time.sleep(5)


    is_solved = solved_tick()

    while (is_solved == False):
        if is_solved == True:
            print("Trying to solve")
            break
        driver.switch_to.default_content()
        WebDriverWait(driver, 40).until(EC.frame_to_be_available_and_switch_to_it(
            (By.CSS_SELECTOR, "iframe[src^='https://www.google.com/recaptcha/api2/bframe?']")))
        time.sleep(2)
        download_link = driver.find_element_by_class_name("rc-audiochallenge-tdownload-link").get_attribute("href")
        random = rd(1)[0]
        urllib.request.urlretrieve(download_link, "voice/" + str(random) + ".mp3")

        # Solving it through IBM Speech to Text Api
        captcha_res = voice_solver(random)
        driver.find_element_by_xpath('//*[@id="audio-response"]').send_keys(captcha_res)
        driver.find_element_by_xpath('//*[@id="recaptcha-verify-button"]').click()
        driver.switch_to.default_content()
        is_solved = solved_tick()

    driver.close()
