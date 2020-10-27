import requests
import time


def main():
    url = 'https://secure.louisvuitton.cn/ajaxsecure/getStockLevel.jsp?storeLang=zhs-cn&pageType=storelocator_section&skuIdList=M40712&null&_=1603769741816'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        print(response.text)


if __name__ == '__main__':
    main()
    # for i in range(2880):
    #     main()
    #     time.sleep(30)
