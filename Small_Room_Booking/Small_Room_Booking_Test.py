import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from Test_Data import test_data_set_one_hour, test_data_set_five_hour, test_data_set_one_day, test_data_set_three_day, \
    test_data_set_seven_day


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.get("https://muntasir101.github.io/Conference-Room-Booking/")
    driver.implicitly_wait(20)

    yield driver
    driver.quit()


def test_room_booking_small_room_one_hour(driver):
    start_time_data = test_data_set_one_hour["start_time"]
    end_time_data = test_data_set_one_hour["end_time"]
    Select_room = driver.find_element(By.CSS_SELECTOR, "select#room")
    room_type = Select(Select_room)
    room_type.select_by_value("Small Room")

    Start_time = driver.find_element(By.CSS_SELECTOR, "input#start-time")
    Start_time.click()
    Start_time.send_keys(start_time_data["month"])
    Start_time.send_keys(start_time_data["day"])
    Start_time.send_keys(start_time_data["year"])
    Start_time.send_keys(start_time_data["hour"])
    Start_time.send_keys(start_time_data["minute"])

    End_time = driver.find_element(By.CSS_SELECTOR, "input#end-time")
    End_time.click()
    End_time.send_keys(end_time_data["month"])
    End_time.send_keys(end_time_data["day"])
    End_time.send_keys(end_time_data["year"])
    End_time.send_keys(end_time_data["hour"])
    End_time.send_keys(end_time_data["minute"])
    End_time.send_keys(Keys.ARROW_DOWN)

    Book_room_button = driver.find_element(By.CSS_SELECTOR, "#booking-form button")
    Book_room_button.click()

    #Expected_cost_for_one_hour = "Total Cost: $150"

    Actual_cost_for_one_hour_element = driver.find_element(By.CSS_SELECTOR, "#cost")
    Actual_cost_for_one_hour = Actual_cost_for_one_hour_element.text

    if test_data_set_one_hour["expected_cost_for_small_room"] == Actual_cost_for_one_hour:
        print("Test Case Passed.Cost for one hour is $100")
    else:
        print("Test Case Failed.")
        print("Expected Cost: ", test_data_set_one_hour["expected_cost_for_small_room"], "But Found: ", Actual_cost_for_one_hour)


def test_room_booking_small_room_five_hour(driver):
    start_time_data = test_data_set_five_hour["start_time"]
    end_time_data = test_data_set_five_hour["end_time"]
    Select_room = driver.find_element(By.CSS_SELECTOR, "select#room")
    room_type = Select(Select_room)
    room_type.select_by_value("Small Room")

    Start_time = driver.find_element(By.CSS_SELECTOR, "input#start-time")
    Start_time.click()
    Start_time.send_keys(start_time_data["month"])
    Start_time.send_keys(start_time_data["day"])
    Start_time.send_keys(start_time_data["year"])
    Start_time.send_keys(start_time_data["hour"])
    Start_time.send_keys(start_time_data["minute"])

    End_time = driver.find_element(By.CSS_SELECTOR, "input#end-time")
    End_time.click()
    End_time.send_keys(end_time_data["month"])
    End_time.send_keys(end_time_data["day"])
    End_time.send_keys(end_time_data["year"])
    End_time.send_keys(end_time_data["hour"])
    End_time.send_keys(end_time_data["minute"])
    End_time.send_keys(Keys.ARROW_DOWN)

    Book_room_button = driver.find_element(By.CSS_SELECTOR, "#booking-form button")
    Book_room_button.click()

    #Expected_cost_for_five_hour = "Total Cost: $500"

    Actual_cost_for_five_hour_element = driver.find_element(By.CSS_SELECTOR, "#cost")
    Actual_cost_for_five_hour = Actual_cost_for_five_hour_element.text

    if test_data_set_five_hour["expected_cost_for_small_room"] == Actual_cost_for_five_hour:
        print("Test Case Passed.Cost for five hour is $500")
    else:
        print("Test Case Failed.")
        print("Expected Cost: ", test_data_set_five_hour["expected_cost_for_small_room"], "But Found: ",
              Actual_cost_for_five_hour)

def test_room_booking_small_room_one_day(driver):
    start_time_data = test_data_set_one_day["start_time"]
    end_time_data = test_data_set_one_day["end_time"]
    Select_room = driver.find_element(By.CSS_SELECTOR, "select#room")
    room_type = Select(Select_room)
    room_type.select_by_value("Small Room")

    Start_time = driver.find_element(By.CSS_SELECTOR, "input#start-time")
    Start_time.click()
    Start_time.send_keys(start_time_data["month"])
    Start_time.send_keys(start_time_data["day"])
    Start_time.send_keys(start_time_data["year"])
    Start_time.send_keys(start_time_data["hour"])
    Start_time.send_keys(start_time_data["minute"])

    End_time = driver.find_element(By.CSS_SELECTOR, "input#end-time")
    End_time.click()
    End_time.send_keys(end_time_data["month"])
    End_time.send_keys(end_time_data["day"])
    End_time.send_keys(end_time_data["year"])
    End_time.send_keys(end_time_data["hour"])
    End_time.send_keys(end_time_data["minute"])
    #End_time.send_keys(Keys.ARROW_DOWN)

    Book_room_button = driver.find_element(By.CSS_SELECTOR, "#booking-form button")
    Book_room_button.click()

    #Expected_cost_for_one_day = "Total Cost: $800"

    Actual_cost_for_one_day_element = driver.find_element(By.CSS_SELECTOR, "#cost")
    Actual_cost_for_one_day = Actual_cost_for_one_day_element.text

    if test_data_set_one_day["expected_cost_for_small_room"] == Actual_cost_for_one_day:
        print("Test Case Passed.Cost for one day is $800")
    else:
        print("Test Case Failed.")
        print("Expected Cost: ", test_data_set_one_day["expected_cost_for_small_room"], "But Found: ",
              Actual_cost_for_one_day)

def test_room_booking_small_room_three_day(driver):
    start_time_data = test_data_set_three_day["start_time"]
    end_time_data = test_data_set_three_day["end_time"]
    Select_room = driver.find_element(By.CSS_SELECTOR, "select#room")
    room_type = Select(Select_room)
    room_type.select_by_value("Small Room")

    Start_time = driver.find_element(By.CSS_SELECTOR, "input#start-time")
    Start_time.click()
    Start_time.send_keys(start_time_data["month"])
    Start_time.send_keys(start_time_data["day"])
    Start_time.send_keys(start_time_data["year"])
    Start_time.send_keys(start_time_data["hour"])
    Start_time.send_keys(start_time_data["minute"])

    End_time = driver.find_element(By.CSS_SELECTOR, "input#end-time")
    End_time.click()
    End_time.send_keys(end_time_data["month"])
    End_time.send_keys(end_time_data["day"])
    End_time.send_keys(end_time_data["year"])
    End_time.send_keys(end_time_data["hour"])
    End_time.send_keys(end_time_data["minute"])
    #End_time.send_keys(Keys.ARROW_DOWN)

    Book_room_button = driver.find_element(By.CSS_SELECTOR, "#booking-form button")
    Book_room_button.click()

    #Expected_cost_for_three_day = "Total Cost: $2400"

    Actual_cost_for_three_day_element = driver.find_element(By.CSS_SELECTOR, "#cost")
    Actual_cost_for_three_day = Actual_cost_for_three_day_element.text

    if test_data_set_three_day["expected_cost_for_small_room"] == Actual_cost_for_three_day:
        print("Test Case Passed.Cost for three day is $2400")
    else:
        print("Test Case Failed.")
        print("Expected Cost: ",test_data_set_three_day["expected_cost_for_small_room"], "But Found: ", Actual_cost_for_three_day)

def test_room_booking_small_room_seven_day(driver):
    start_time_data = test_data_set_seven_day["start_time"]
    end_time_data = test_data_set_seven_day["end_time"]
    Select_room = driver.find_element(By.CSS_SELECTOR, "select#room")
    room_type = Select(Select_room)
    room_type.select_by_value("Small Room")

    Start_time = driver.find_element(By.CSS_SELECTOR, "input#start-time")
    Start_time.click()
    Start_time.send_keys(start_time_data["month"])
    Start_time.send_keys(start_time_data["day"])
    Start_time.send_keys(start_time_data["year"])
    Start_time.send_keys(start_time_data["hour"])
    Start_time.send_keys(start_time_data["minute"])

    End_time = driver.find_element(By.CSS_SELECTOR, "input#end-time")
    End_time.click()
    End_time.send_keys(end_time_data["month"])
    End_time.send_keys(end_time_data["day"])
    End_time.send_keys(end_time_data["year"])
    End_time.send_keys(end_time_data["hour"])
    End_time.send_keys(end_time_data["minute"])
    #End_time.send_keys(Keys.ARROW_DOWN)

    Book_room_button = driver.find_element(By.CSS_SELECTOR, "#booking-form button")
    Book_room_button.click()

    #Expected_cost_for_seven_day = "Total Cost: $5600"

    Actual_cost_for_seven_day_element = driver.find_element(By.CSS_SELECTOR, "#cost")
    Actual_cost_for_seven_day = Actual_cost_for_seven_day_element.text

    if test_data_set_seven_day["expected_cost_for_small_room"] == Actual_cost_for_seven_day:
        print("Test Case Passed.Cost for seven day is $5600")
    else:
        print("Test Case Failed.")
        print("Expected Cost: ", test_data_set_seven_day["expected_cost_for_small_room"], "But Found: ", Actual_cost_for_seven_day)

