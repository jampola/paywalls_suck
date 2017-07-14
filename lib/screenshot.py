from selenium import webdriver
import os, hashlib

br = webdriver.PhantomJS()
save_location = "./static/screenshots/"
# 10 seconds should be enough for most pages. YMMV.
timeout = 10

def get_screenshot(url,width,height):
	# if no dimentions included, default to 0
	if not width: width = 0
	if not height: height = 0

	# if the user forgets to append http(s), we'll do it for them.
	if 'http' not in url:
		url="http://{}".format(url)

	# Some homebrew random filename string here.
	fname = hashlib.md5(os.urandom(128)).hexdigest()[:8] + '.png'
	br.set_window_size(width,height)
	br.set_page_load_timeout(timeout)
	br.get(url)
	br.save_screenshot(save_location + fname)
	br.quit
	return fname