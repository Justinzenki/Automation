from selenium import webdriver

print('Input your user name')
userEmail = input()
print('Input your password')

browser = webdriver.Firefox()
browser.get('http://https://login.microsoftonline.com/login.srf?wa=wsignin1.0&rpsnv=4&ct=1453277609&rver=6.7.6640.0&wp=MCMBI&wreply=https:%2F%2Fportal.office.com%2Flanding.aspx%3Ftarget%3D%252fdefault.aspx&lc=1033&id=501392&msafed=0')

emailElem = browser.find_element_by_id('cred_userid_inputtext')
emailElem.send_keys(userEmail)

passwordElem = browser.find_element_by_id('cred_userid_inputtext')
passwordElem.send_keys(userPassword)


