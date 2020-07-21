#!/Library/Frameworks/Python.framework/Versions/3.8/bin/python3



from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import datetime
import sys




def check_availibility(code):

	options = Options()
	options.headless = True 

	PATH = "/Applications/chromedriver"
	driver = webdriver.Chrome(PATH, options = options)


	#Set availibility to "Unvailable" by default
	availibility = "Unavailable"

	#Open Rogue Fitness webpage
	driver.get("https://www.roguefitness.com")
	print(driver.title)

	#Navigate to kettlebell products webpage using search bar 
	search = driver.find_element_by_id("site-search-input")
	search.send_keys("kettlebells")
	search.send_keys(Keys.RETURN)

	time.sleep(2)

	kettlebell_link = driver.find_element_by_link_text("Rogue Kettlebells")
	kettlebell_link.send_keys(Keys.RETURN)

	time.sleep(2)

	#Locate specific product element 
	product_code = "product-purchase-wrapper-" + str(code)
	product = driver.find_element_by_class_name(product_code)
	product_name = product.find_element_by_xpath('.//*[@class="item-name"]').text
	
	#Check if product available
	try:
		notification = product.find_element_by_xpath('.//button[@class="v-btn v-btn-gray v-btn-full"]').text
	except NoSuchElementException:
		availibility = "Available"
	
	#Close browser
	driver.quit()

	#Return availibility status
	return availibility


# def checkout(code):

	# options = Options()
	# options.headless = False 

	# PATH = "/Applications/chromedriver"
	# driver = webdriver.Chrome(PATH, options = options)

	# driver.get("https://www.roguefitness.com")
	# print(driver.title)

	# #Navigate to kettlebell products webpage using search bar 
	# search = driver.find_element_by_id("site-search-input")
	# search.send_keys("kettlebells")
	# search.send_keys(Keys.RETURN)

	# time.sleep(2)

	# kettlebell_link = driver.find_element_by_link_text("Rogue Kettlebells")
	# kettlebell_link.send_keys(Keys.RETURN)

	# time.sleep(2)

	# #Locate specific product quantity input 
	# product_code = "grouped-product-item-" + str(code)
	# product = driver.find_element_by_id(product_code)

	# #
	# product.send_keys("1")
	# product.send_keys(Keys.RETURN)


	# checkout_button = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="side-cart"]/div/div[3]/div[1]/div[1]/button')))
	# driver.execute_script("arguments[0].click();", checkout_button)

	# complete_order = input("Waiting to confirm order....")

	# checkout_button = driver.find_element_by_xpath('//*[@id="side-cart"]/div/div[3]/div[1]/div[1]/button').click()
	# return "successfully Added to Cart"




#    Product Codes
#===============================
#   9 lb Kettlebells     7165
#  13 lb Kettlebells     7163
#  18 lb Kettlebells     7161
#  26 lb Kettlebells     7159
#  35 lb Kettlebells     7157
#  40 lb Kettlebells     72613
#  44 lb Kettlebells     7155
#  53 lb Kettlebells     7153
#  62 lb Kettlebells     7151
#  70 lb Kettlebells     7149
#  80 lb Kettlebells     7147
#  88 lb Kettlebells     7145
#  97 lb Kettlebells     7143
# 106 lb Kettlebells     7141
# 124 lb Kettlebells     7139
# 150 lb Kettlebells     7137
# 176 lb Kettlebells     7135
# 203 lb Kettlebells     7133

kettlebells = {7165: '9 lb Kettlebells',
			   7163: '13 lb Kettlebells',
			   7161: '18 lb Kettlebells',
			   7159: '26 lb Kettlebells',
			   7157: '35 lb Kettlebells',
			   72613:'40 lb Kettlebells',
			   7155: '44 lb Kettlebells',
			   7153: '53 lb Kettlebells',
			   7151: '62 lb Kettlebells',
			   7149: '70 lb Kettlebells',
			   7147: '80b Kettlebells',
			   7145: '88 lb Kettlebells',
			   7143: '97 lb Kettlebells',
			   7141: '106 lb Kettlebells',
			   7139: '124 lb Kettlebells',
			   7137: '150 lb Kettlebells',
			   7135: '176 lb Kettlebells',
			   7133: '203 lb Kettlebells'}

results_stdout = sys.stdout

# code = int(input("Enter product code: "))
item_status = check_availibility(7155)
# print(kettlebells[product_code] + ": " + item_status)

now = datetime.datetime.now()

original_stdout = sys.stdout # Save a reference to the original standard output

with open('kettlebell_results.txt', 'w') as f:
	sys.stdout = f # Change the standard output to the file we created.

	if item_status == "Available":
		options = Options()
		options.headless = False 

		PATH = "/Applications/chromedriver"
		driver = webdriver.Chrome(PATH, options = options)

		driver.get("https://www.roguefitness.com/rogue-kettlebells")

		time.sleep(5)

		#Locate specific product quantity input 
		product_code = "grouped-product-item-" + str(7155)
		product = driver.find_element_by_id(product_code)

		#
		product.send_keys("1")
		product.send_keys(Keys.RETURN)

		print (now.strftime("%Y-%m-%d %H:%M:%S") + " -- " + "1 " + kettlebells[7155] + " successfully added to cart")
		print("Return to webpage to complete transaction")


	# print()
	# print (now.strftime("%Y-%m-%d %H:%M:%S") + " -- " + "1 " + kettlebells[7155] + " successfully added to cart")

	else:
		print(now.strftime("%Y-%m-%d %H:%M:%S") + " -- " + kettlebells[7155] + " not available")

f.close()
sys.stdout = original_stdout # Reset the standard output to its original value


