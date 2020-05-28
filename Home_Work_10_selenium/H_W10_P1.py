import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from Home_Work_python.Learn_python3.Home_Work_10_selenium.custome_wait import presence_of_elements

dr = webdriver.Chrome(executable_path=r"/Users/fabric/PycharmProjects/chromedriver")
dr.get('http://localhost:8888/oxwall/')
wait = WebDriverWait(dr, 10)


# скрипт логирования пользователя
# frame_element = dr.find_element(By.NAME, "demobody")
# dr.switch_to.frame(frame_element)
sing_in = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'ow_signin_label')))
sing_in.click()
username_email_field = dr.find_element(By.CSS_SELECTOR, '.ow_user_name input').send_keys('fabric')
pass_field = dr.find_element(By.CSS_SELECTOR, '.ow_password input').send_keys('pass')
button_sign_in = dr.find_element(By.NAME, 'submit').click()


# Подсчет постов до публикации
count_of_post = len(dr.find_elements(By.CLASS_NAME, 'ow_newsfeed_item'))
print(count_of_post)


# написания коментария
comment_field = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.ow_smallmargin textarea')))
comment_field.send_keys("test comment123")
add_comment_button = dr.find_element(By.CLASS_NAME, 'ow_attachment_btn input').click()


# custom_wait
results = wait.until(presence_of_elements((By.CLASS_NAME, "ow_newsfeed_item"), count_of_post), message="Less than ")
print("Count After = ", len(results))
assert len(results) == count_of_post + 1

# Добавить пост с фотографией
enter_field = dr.find_element(By.CSS_SELECTOR, '.ow_smallmargin textarea').click()
button_attach = dr.find_element(By.CSS_SELECTOR, "input.mlt_file_input").send_keys('/Users/fabric/oxwall.jpg')
wait.until(EC.invisibility_of_element((By.CSS_SELECTOR, "a.ow_photo_attachment_pic.ow_attachment_preload.loading")))
add_comment_withphoto_button = dr.find_element(By.CLASS_NAME, 'ow_attachment_btn input').click()

time.sleep(2)
# разлогирование пользователя c ховером
button_sign_out = dr.find_element(By.CSS_SELECTOR, '.ow_console_item.ow_console_dropdown.ow_console_dropdown_hover')
action = ActionChains(dr)
action.move_to_element(button_sign_out)
action.perform()
button_log_out = dr.find_element(By.XPATH, "//li[7]/div/a")
button_log_out.click()

dr.close()
