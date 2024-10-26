This is not a project.it's just example for Selenium Test Website🤞

I gained several experiences during this project

Experiences:

1)when use selenium , its closing browser automatically I used the following code to solve this problem.

    from selenium.webdriver.chrome.options import Options
    options=webdriver.ChromeOptions()
    options.add_experimental_option("detach",True)
    driver = webdriver.Chrome(options=options)
