# Recaptcha-solver
# recapthca-solver
A simple plugable recaptcha solver. You can use this script with your selenium script.



How to use? 

Sinup for idm cloud
Then go here https://cloud.ibm.com/catalog/services/speech-to-text and hit create 

You Will get a Api key and url address like follwing

![image](https://user-images.githubusercontent.com/83664154/117051782-c03e1500-ad38-11eb-8938-93f232092be2.png)

Replace the api on recaptcha-solver.py on line 11 and 12 with your own api

```python
apikey = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
url = 'https://api.us-south.speech-to-text.watson.cloud.ibm.com/xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
```


Import these before using it on your own script

```python
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from recaptcha_solver import *

# Now use next line of code on captcha page.

solver(driver,WebDriverWait,EC,By,NoSuchElementException)

```






Example:

```python
import undetected_chromedriver as webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from recaptcha_solver import *

chrome_options = webdriver.ChromeOptions()


driver = webdriver.Chrome()
driver.get("https://www.google.com/recaptcha/api2/demo")
solver(driver,WebDriverWait,EC,By,NoSuchElementException)
time.sleep(10000)
driver.close
```





