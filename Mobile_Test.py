import cv2
import numpy as np
from time import sleep
from _overlapped import NULL

def wait_for_loading(self, loading_img_path, loading_scrn_path, timeout):
    
    load_img = cv2.imread(loading_img_path,0)          # Loading Image @UndefinedVariable
    
    print(self.driver.save_screenshot(loading_scrn_path))
    
    load_scrn = cv2.imread(loading_scrn_path, 0)   # Loading Screenshot @UndefinedVariable
    
    # Default timeout is 60 seconds
    if (timeout == NULL):
        timeout = 60
        
    time_spent = 0
    count = 1
        
    while (count > 0 & time_spent <= timeout):
        # Save a screenshot of the screen
        self.driver.save_screenshot(loading_scrn_path)
        
        load_scrn = cv2.imread(loading_scrn_path, 0)   # Loading Screenshot @UndefinedVariable
        count = len(find_matches(load_scrn, load_img, 0.97))
        sleep(2)
        time_spent += 2
        
    if (time_spent > timeout):
        print("Test failed! Load time exceeded timeout of ", timeout, " seconds!")
        self.driver.quit()
    else:
        print("Loading ended in aprox. ", time_spent, " seconds.")

def skip_ads(self, close_img_path, close_img_alt_path, ad_scrn_path, timeout):
    
    close_img = cv2.imread(close_img_path,0)          # Close ad Image @UndefinedVariable
    close_img_alt = cv2.imread(close_img_alt_path,0)          # Close ad alternative Image @UndefinedVariable
    
    print(self.driver.save_screenshot(ad_scrn_path))
    
    ad_scrn = cv2.imread(ad_scrn_path, 0)   # Ad Screenshot @UndefinedVariable
    
    # Default timeout is 60 seconds
    if (timeout == NULL):
        timeout = 60
        
    time_spent = 0
    count = 0
        
    while ((count < 1) & (time_spent < timeout)):
        # Save a screenshot of the screen
        self.driver.save_screenshot(ad_scrn_path)
        
        ad_scrn = cv2.imread(ad_scrn_path, 0)   # Ad Screenshot @UndefinedVariable
        close_ad = find_matches(ad_scrn, close_img, 0.9)
        count = len(close_ad)
        # First close image not found, try to find the alternative one
        if (count == 0):
            close_ad = find_matches(ad_scrn, close_img_alt, 0.9)
            count = len(close_ad)
        sleep(2)
        time_spent += 2
        
    if (time_spent >= timeout):
        print("Test failed! Ad time exceeded timeout of ", timeout, " seconds!")
        self.driver.quit()
    else:
        if (count > 1):
            close_point = []
            close_point.append(close_ad[0])
        else:
            close_point = close_ad
        self.driver.tap(close_point)
        print("Ad closed in aprox. ", time_spent, " seconds.")
        sleep(1)
        
def find_matches(screenshot, template, threshold):
    w, h = template.shape[::-1]
        
    res = cv2.matchTemplate(screenshot,template,cv2.TM_CCOEFF_NORMED)  # @UndefinedVariable
    loc = np.where( res >= threshold )
    count = 0
    points = []
    # Counts the matches themselves
    #and saves their centers to an array
    for pt in zip(*loc[::-1]):
        count = count + 1
        points.append((pt[0]+w/2, pt[1]+h/2))
    print(count, " match(es) found.")
    return points