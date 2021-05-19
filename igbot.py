from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

uname = input("Enter your username of Instagram : ")
pw = input("Enter the password for the account : ")


PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://www.instagram.com/")
time.sleep(3)


# enter username
username = driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/\
	div[1]/div/form/div/div[1]/div/label/input")

username.send_keys(uname)
username.send_keys(Keys.RETURN)


# enter password
password = driver.find_element_by_xpath("/html/body/div[1]/section/main/article/\
	div[2]/div[1]/div/form/div/div[2]/div/label/input")

password.send_keys(pw)
password.send_keys(Keys.RETURN)


# hit login button
login = driver.find_element_by_xpath(
    "/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]")
login.click()

time.sleep(5)

while True:
    try:
        # hit not now button
        notNow = driver.find_element_by_xpath(
            "/html/body/div[1]/section/main/div/div/div/div/button")
        notNow.click()
        time.sleep(1)

        notNow1 = driver.find_element_by_xpath(
            "/html/body/div[4]/div/div/div/div[3]/button[2]")
        notNow1.click()
        time.sleep(1)
    except:
        print("Please enter correct username and password")
        break

    # go to my profile
    profile = driver.find_element_by_xpath("/html/body/div[1]/section/main/section/div[3]/div[1]/\
		div/div/div[2]/div[1]/div/div/a")
    profile.click()
    time.sleep(3)

    # function for scrolling till the last element

    def scroll():
        scrollBox = driver.find_element_by_xpath(
            "/html/body/div[5]/div/div/div[2]")

        prevHeight, newHeight = 0, 1

        while prevHeight != newHeight:
            prevHeight = newHeight
            time.sleep(1)

            newHeight = driver.execute_script("""
				arguments[0].scrollTo(0, arguments[0].scrollHeight);
				return arguments[0].scrollHeight;
				""", scrollBox)

    # click followers,scroll through it and extract all names

    followers = driver.find_element_by_xpath(
        "/html/body/div[1]/section/main/div/header/section/ul/li[2]/a")
    followers.click()
    time.sleep(4)

    scroll()

    fersnames = driver.find_elements_by_tag_name("a")
    followersList = [name.text for name in fersnames if name.text != " "]

    closebutton = driver.find_element_by_xpath(
        "/html/body/div[5]/div/div/div[1]/div/div[2]/button")
    closebutton.click()

    # click following list,scroll through it and extract all names

    following = driver.find_element_by_xpath(
        "/html/body/div[1]/section/main/div/header/section/ul/li[3]/a")
    following.click()
    time.sleep(4)

    scroll()

    fwingsnames = driver.find_elements_by_tag_name("a")
    followingslist = [na.text for na in fwingsnames if na.text != " "]

    closebutton1 = driver.find_element_by_xpath(
        "/html/body/div[5]/div/div/div[1]/div/div[2]/button")
    closebutton1.click()

    # check

    notFollowedBack = [
        badd for badd in followingslist if badd not in followersList]
    print(notFollowedBack)
    break

driver.quit()
