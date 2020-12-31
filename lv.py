import requests
import time
import json
# from selenium import webdriver
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.wait import WebDriverWait


def main():
    url = 'https://secure.louisvuitton.cn/ajaxsecure/getStockLevel.jsp?storeLang=zhs-cn&pageType=storelocator_section&skuIdList=M40712&null&_=1603769741816'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        res = json.loads(response.text)
        inStock = res['M40712']['inStock']
        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) +
              ": " + str(inStock))
        if inStock:
            write_to_file(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) +
                          ": " + str(inStock))


def write_to_file(content):
    with open('result.txt', 'a', encoding='utf-8') as f:
        f.write(content + '\n')


def browser():
    option = webdriver.ChromeOptions()
    option.add_experimental_option('detach', True)
    b = webdriver.Chrome(options=option)
    try:
        url = 'https://www.louisvuitton.cn/zhs-cn/products/pochette-accessoires-monogram-005656'
        b.get(url)
        # wait = WebDriverWait(b, 10)
        # wait.until(EC.url_to_be(url))
        # toCart = b.find_element_by_id('addToCartSubmit')
        # toCart.click()
        # order = b.find_element_by_id('viewTaxesAndDetails')
        # order.click()
        # wait.until(EC.title_is(u"我的购物袋"))
        # confirm = b.find_element_by_id('proceedToCheckoutButtonTop')
        # confirm.click()
        # wait.until(EC.title_is(u"身份验证"))
        # name = b.find_element_by_id('loginloginForm')
        # pwd = b.find_element_by_id('passwordloginForm')
        # name.send_keys('16620038893')
        # pwd.send_keys('Ll574954033_')
        # login = b.find_element_by_id('loginSubmit_')
        # login.click()
        # wait.until(EC.title_is(u"我的配送信息"))
        # submit = b.find_element_by_id('globalSubmit')
        # submit.click()
        # wait.until(EC.title_is(u"查看我的订单"))
        # check = b.find_element_by_id('acceptTermsTop')
        # check.click()
        # submitToPay = b.find_element_by_id('globalSubmitTop')
        # submitToPay.click()
        pass
    finally:
        pass


if __name__ == '__main__':
    for i in range(5760):
        main()
        time.sleep(10)
