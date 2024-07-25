import random
import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def click_element(driver, xpath, question):
    try:
        element = driver.find_element(By.XPATH, xpath)
        element.click()
        print(f"{question} 已经选完")
        time.sleep(random.randint(1, 7))
    except Exception as e:
        print(f"点击元素时发生错误: {e}")

def save_screenshot(driver, path, width, height):
    try:
        # 设置窗口尺寸
        driver.set_window_size(width, height)
        driver.save_screenshot(path)
        print(f"截屏已保存到: {path}")
    except Exception as e:
        print(f"截屏失败: {e}")

def main():
    print("作业开始")

    # 随机 User-Agent 列表
    user_agents = [
        'Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Mobile/15E148 Safari/604.1',
        'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1',
        'Mozilla/5.0 (Linux; Android 10; SM-G975F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36',
        'Mozilla/5.0 (Linux; Android 9; SM-G960U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Mobile Safari/537.36',
        'Mozilla/5.0 (iPhone; CPU iPhone OS 13_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0 Mobile/15E148 Safari/604.1',
        'Mozilla/5.0 (iPhone; CPU iPhone OS 12_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0 Mobile/15E148 Safari/604.1',
        'Mozilla/5.0 (Linux; Android 11; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.91 Mobile Safari/537.36',
        'Mozilla/5.0 (Linux; Android 11; SM-N986B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.105 Mobile Safari/537.36',
        'Mozilla/5.0 (Linux; Android 10; SM-N960F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Mobile Safari/537.36',
        'Mozilla/5.0 (Linux; Android 9; SM-G965U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.127 Mobile Safari/537.36',
        'Mozilla/5.0 (Linux; Android 8.0.0; SM-G950F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.111 Mobile Safari/537.36',
        'Mozilla/5.0 (Linux; Android 7.1.1; Nexus 6P Build/N4F26I) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36',
        'Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5 Build/M4B30Z) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Mobile Safari/537.36',
        'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Mobile/14E5239e Safari/602.1',
        'Mozilla/5.0 (Linux; Android 5.1; Nexus 4 Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Mobile Safari/537.36'
    ]

    # 扩充后的手机视图大小列表
    mobile_view_sizes = [
        {'width': 375, 'height': 667},  # iPhone 8
        {'width': 414, 'height': 736},  # iPhone 8 Plus
        {'width': 360, 'height': 640},  # Nexus 5
        {'width': 412, 'height': 732},  # Galaxy S7
        {'width': 375, 'height': 812},  # iPhone X
        {'width': 360, 'height': 740},  # Pixel 4
        {'width': 375, 'height': 812},  # iPhone 11
        {'width': 411, 'height': 731},  # Nexus 6P
        {'width': 360, 'height': 800},  # Galaxy A52
        {'width': 375, 'height': 667},  # iPhone 7
        {'width': 360, 'height': 720},  # Galaxy S9
        {'width': 393, 'height': 851},  # iPhone 13 Mini
        {'width': 430, 'height': 932},  # iPhone 13 Pro Max
        {'width': 384, 'height': 800},  # OnePlus 8T
        {'width': 412, 'height': 915},  # Galaxy S21 Ultra
        {'width': 384, 'height': 816},  # Google Pixel 6
        {'width': 391, 'height': 844},  # iPhone 14 Pro
        {'width': 430, 'height': 933},  # iPhone 14 Pro Max
        {'width': 360, 'height': 800},  # Galaxy A32
        {'width': 384, 'height': 780},  # Pixel 7
        {'width': 368, 'height': 832},  # Xperia 5 II
        {'width': 375, 'height': 812},  # iPhone SE (2nd generation)
        {'width': 412, 'height': 915},  # Galaxy Note 10+
        {'width': 390, 'height': 844},  # iPhone 12 Pro
        {'width': 360, 'height': 760},  # OnePlus Nord
        {'width': 384, 'height': 780},  # Pixel 7 Pro
        {'width': 390, 'height': 844},  # iPhone 12 Pro Max
        {'width': 384, 'height': 854},  # OnePlus 9
        {'width': 360, 'height': 760},  # Samsung Galaxy M32
        {'width': 396, 'height': 844},  # iPhone 14
        {'width': 384, 'height': 800},  # Xiaomi Mi 11
        {'width': 360, 'height': 800},  # Motorola Moto G Power (2021)
        {'width': 400, 'height': 900},  # Oppo Find X3 Pro
        {'width': 384, 'height': 856},  # OnePlus 8 Pro
        {'width': 400, 'height': 900}   # Sony Xperia 1 II
    ]



    # 随机选择 User-Agent 和手机视图大小
    random_user_agent = random.choice(user_agents)
    random_mobile_view = random.choice(mobile_view_sizes)

    # 设置 Chrome 选项
    options = Options()
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-gpu')
    options.add_argument('--hide-scrollbars')
    options.add_argument(f'user-agent={random_user_agent}')
    options.add_argument(f'--window-size={random_mobile_view["width"]},{random_mobile_view["height"]}')
    # 去掉 headless 选项，以便观察浏览器行为
    # options.add_argument('--headless')

    try:
        # 手动指定 ChromeDriver 路径
        driver_path = 'C:/Python312/chromedriver.exe'  # 修改为实际 ChromeDriver 路径
        print(f"ChromeDriver 路径: {driver_path}")

        # 创建 ChromeDriver 实例
        print("启动 ChromeDriver...")
        driver = webdriver.Chrome(service=Service(driver_path), options=options)
        print("ChromeDriver 成功启动")

        # 打开指定的网页
        url = "*****************************************"
        print(f"尝试打开网页: {url}")
        driver.get(url)
        print(f"成功打开网页: {url}")

        # 等待页面加载完成
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="question"]/section/div[3]/div/div[17]/div[2]/div/div[1]/div/i')))

        # 1、您所在的城区？
        click_element(driver, '//*[@id="question"]/section/div[3]/div/div[1]/div[2]/div/div[1]/div/i', '1、您所在的城区？')

        # 2、您的年龄是？
        elements_group2 = [
            '//*[@id="question"]/section/div[3]/div/div[2]/div[2]/div/div[1]/div/i',
            '//*[@id="question"]/section/div[3]/div/div[2]/div[2]/div/div[2]/div/i',
            '//*[@id="question"]/section/div[3]/div/div[2]/div[2]/div/div[3]/div/i',
            '//*[@id="question"]/section/div[3]/div/div[2]/div[2]/div/div[4]/div/i'
        ]
        random_element2 = random.choices(elements_group2, weights=[1, 2, 3, 1], k=1)[0]
        click_element(driver, random_element2, '2、您的年龄是？')

        # 3、您受教育的程度？
        elements_group3 = [
            '//*[@id="question"]/section/div[3]/div/div[3]/div[2]/div/div[1]/div/i',
            '//*[@id="question"]/section/div[3]/div/div[3]/div[2]/div/div[2]/div/i',
            '//*[@id="question"]/section/div[3]/div/div[3]/div[2]/div/div[3]/div/i',
            '//*[@id="question"]/section/div[3]/div/div[3]/div[2]/div/div[4]/div/i',
            '//*[@id="question"]/section/div[3]/div/div[3]/div[2]/div/div[5]/div/i'
        ]
        random_element3 = random.choices(elements_group3, weights=[1, 1, 3, 3, 3], k=1)[0]
        click_element(driver, random_element3, '3、您受教育的程度？')

        # 4、您知道您所在的城区有开展垃圾分类工作吗？
        click_element(driver, '//*[@id="question"]/section/div[3]/div/div[4]/div[2]/div/div[1]/div/i', '4、您知道您所在的城区有开展垃圾分类工作吗？')

        # 5、您接受过有关垃圾分类的教育或宣传吗？
        elements_group5 = [
            '//*[@id="question"]/section/div[3]/div/div[5]/div[2]/div/div[1]/div/i',
            '//*[@id="question"]/section/div[3]/div/div[5]/div[2]/div/div[2]/div/i'
        ]
        random_element5 = random.choices(elements_group5, weights=[3, 1], k=1)[0]
        click_element(driver, random_element5, '5、您接受过有关垃圾分类的教育或宣传吗？')

        # 6、您认为最有效的宣传途径是？
        elements_group6 = [
            '//*[@id="question"]/section/div[3]/div/div[6]/div[2]/div/div[1]/div/i',
            '//*[@id="question"]/section/div[3]/div/div[6]/div[2]/div/div[2]/div/i',
            '//*[@id="question"]/section/div[3]/div/div[6]/div[2]/div/div[3]/div/i',
            '//*[@id="question"]/section/div[3]/div/div[6]/div[2]/div/div[4]/div/i',
            '//*[@id="question"]/section/div[3]/div/div[6]/div[2]/div/div[5]/div/i'
        ]
        random_element6 = random.choice(elements_group6)
        click_element(driver, random_element6, '6、您认为最有效的宣传途径是？')

        # 7、您所在的社区一般多久开展一次垃圾分类宣传活动？
        click_element(driver, '//*[@id="question"]/section/div[3]/div/div[7]/div[2]/div/div[1]/div/i', '7、您所在的社区一般多久开展一次垃圾分类宣传活动？')

        # 8、您生活的地区垃圾投放点是以什么样形式安放？
        click_element(driver, '//*[@id="question"]/section/div[3]/div/div[8]/div[2]/div/div[1]/div/i', '8、您生活的地区垃圾投放点是以什么样形式安放？')

        # 9、处理垃圾时您有将垃圾分类的习惯吗？
        elements_group9 = [
            '//*[@id="question"]/section/div[3]/div/div[9]/div[2]/div/div[1]/div/i',
            '//*[@id="question"]/section/div[3]/div/div[9]/div[2]/div/div[2]/div/i',
            '//*[@id="question"]/section/div[3]/div/div[9]/div[2]/div/div[3]/div/i'
        ]
        random_element9 = random.choices(elements_group9, weights=[3, 3, 1], k=1)[0]
        click_element(driver, random_element9, '9、处理垃圾时您有将垃圾分类的习惯吗？')

        # 10、您可能会对下列哪些物品进行分类处理？
        elements_group10 = [
            '//*[@id="question"]/section/div[3]/div/div[10]/div[2]/div/div[1]/div/i',
            '//*[@id="question"]/section/div[3]/div/div[10]/div[2]/div/div[2]/div/i',
            '//*[@id="question"]/section/div[3]/div/div[10]/div[2]/div/div[3]/div/i',
            '//*[@id="question"]/section/div[3]/div/div[10]/div[2]/div/div[4]/div/i',
            '//*[@id="question"]/section/div[3]/div/div[10]/div[2]/div/div[5]/div/i',
            '//*[@id="question"]/section/div[3]/div/div[10]/div[2]/div/div[6]/div/i'
        ]
        random_elements_group10 = random.sample(elements_group10, random.choices([1, 2, 3, 4, 5, 6], weights=[1, 2, 4, 4, 2, 1], k=1)[0])
        for xpath in random_elements_group10:
            click_element(driver, xpath, '10、您可能会对下列哪些物品进行分类处理？')

        # 11、您认为可能影响您没有将垃圾彻底分类的原因有哪些？
        elements_group11 = [
            '//*[@id="question"]/section/div[3]/div/div[11]/div[2]/div/div[1]/div/i',
            '//*[@id="question"]/section/div[3]/div/div[11]/div[2]/div/div[4]/div/i',
            '//*[@id="question"]/section/div[3]/div/div[11]/div[2]/div/div[5]/div/i'
        ]
        random_elements_group11 = random.sample(elements_group11, random.choices([1, 2, 3], weights=[1, 2, 4], k=1)[0])
        for xpath in random_elements_group11:
            click_element(driver, xpath, '11、您认为可能影响您没有将垃圾彻底分类的原因有哪些？')

        # 12、如果有关组织进行垃圾分类反馈奖励，您比较喜欢哪一类的奖励？
        elements_group12 = [
            '//*[@id="question"]/section/div[3]/div/div[12]/div[2]/div/div[1]/div/i',
            '//*[@id="question"]/section/div[3]/div/div[12]/div[2]/div/div[2]/div/i',
            '//*[@id="question"]/section/div[3]/div/div[12]/div[2]/div/div[3]/div/i',
            '//*[@id="question"]/section/div[3]/div/div[12]/div[2]/div/div[4]/div/i',
            '//*[@id="question"]/section/div[3]/div/div[12]/div[2]/div/div[5]/div/i'
        ]
        random_elements_group12 = random.sample(elements_group12, random.choices([1, 2, 3, 4, 5], weights=[1, 2, 4, 2, 1], k=1)[0])
        for xpath in random_elements_group12:
            click_element(driver, xpath, '12、如果有关组织进行垃圾分类反馈奖励，您比较喜欢哪一类的奖励？')

        # 13、口香糖属于哪一类垃圾？
        elements_group13 = [
            '//*[@id="question"]/section/div[3]/div/div[13]/div[2]/div/div[2]/div/i',
            '//*[@id="question"]/section/div[3]/div/div[13]/div[2]/div/div[4]/div/i'
        ]
        random_element13 = random.choices(elements_group13, weights=[1, 3], k=1)[0]
        click_element(driver, random_element13, '13、口香糖属于哪一类垃圾？')

        # 14、破碎的碗碟属于哪类垃圾？
        click_element(driver, '//*[@id="question"]/section/div[3]/div/div[14]/div[2]/div/div[3]/div/i', '14、破碎的碗碟属于哪类垃圾？')

        # 15、塑料玩具是什么垃圾？
        click_element(driver, '//*[@id="question"]/section/div[3]/div/div[15]/div[2]/div/div[3]/div/i', '15、塑料玩具是什么垃圾？')

        # 16、废化妆品及其包装物属于其他垃圾。
        elements_group16 = [
            '//*[@id="question"]/section/div[3]/div/div[16]/div[2]/div/div[1]/div/i',
            '//*[@id="question"]/section/div[3]/div/div[16]/div[2]/div/div[2]/div/i'
        ]
        random_element16 = random.choices(elements_group16, weights=[1, 3], k=1)[0]
        click_element(driver, random_element16, '16、废化妆品及其包装物属于其他垃圾。')

        # 17、喝不完的牛奶直接倒进厨余垃圾桶。
        click_element(driver, '//*[@id="question"]/section/div[3]/div/div[17]/div[2]/div/div[2]/div/i', '17、喝不完的牛奶直接倒进厨余垃圾桶。')

        # 延迟3秒后点击提交按钮
        time.sleep(3)
        click_element(driver, '//*[@id="question"]/section/div[4]/button', '提交问卷')

        # 等待确认弹窗并点击确认按钮
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[contains(@class, "van-dialog")]//button[2]')))
        click_element(driver, '/html/body/div[contains(@class, "van-dialog")]//button[2]', '确认提交')

        # 等待页面加载跳转后截屏
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
        screenshot_path = f"D:/projectCode/py/classified-survey-selenium/photo/{random.randint(100000, 999999)}.png"
        save_screenshot(driver, screenshot_path, random_mobile_view["width"], random_mobile_view["height"])

        print("问卷提交完成")

    except WebDriverException as e:
        print(f"ChromeDriver 启动失败: {e}")
    except Exception as e:
        print(f"发生错误: {e}")
    finally:
        # 关闭浏览器
        try:
            driver.quit()
            print("浏览器已关闭")
        except Exception as e:
            print(f"关闭浏览器时发生错误: {e}")

if __name__ == "__main__":
    for i in range(60):
        print(f"开始第 {i + 1} 次运行")
        main()
        print(f"第 {i + 1} 次运行完成")
        # 增加延迟，防止过快的连续请求
        time.sleep(random.randint(2, 3))
