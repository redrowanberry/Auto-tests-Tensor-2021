from selenium import webdriver as wd
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


def test_pictures():
    d = wd.Chrome()
    d.implicitly_wait(1)
    d.get('https://yandex.ru/')
    # ищем на странице значок "Картинки"
    pic = d.find_element_by_css_selector('[data-id="images"]')
    pic_link = pic.get_attribute('href')
    assert pic_link != None, \
        'Значок с подписью "Картинки" не содержит ссылку'
    # кликаем по значку "Картинки", переходим на страницу с популярными категориями
    pic.click()
    
    # т.к. открылась новая вкладка, но "главной" осталась страница поиска Яндекса,
    # выбираем активной вкладку с категориями картинок
    d.window_handles
    d.switch_to_window(d.window_handles[1])
    c_url = d.current_url
    action_url = c_url.split('?')[0]
    #проверяем, какой url открылся: https://yandex.ru/images/ или другой какой-то
    expected_url = 'https://yandex.ru/images/'
    assert action_url == expected_url, \
        'Мы перешли не по ссылке {}, а попали на {}'.format(expected_url, action_url)

    # ищем первую категорию картиночек и запоминаем её название,
    # кликаем по первой категории и проверяем открылась ли она
    first_category = d.find_element_by_css_selector('[data-grid-name="im"]')
    pic_name = first_category.get_attribute('data-grid-text')
    first_category.click()
    first_cat_url = d.current_url
    assert c_url != first_cat_url, \
        'Первая категория картинок не открылась, мы остались на {} вкладке'.format(c_url)
    
    # на странице картиночек из первой категории запоминаем поисковый запрос
    # и сравниваем с названием категории, имя которой запомнили на предыдущей странице
    input_name = d.find_element_by_class_name('input__control')
    val_input = input_name.get_attribute('value')
    assert pic_name == val_input, \
        'Переходили по категории {}, а в тексте поиска содержится {}. Результаты не совпадают'.format(pic_name, val_input)
    time.sleep(1)

    # ищем на странице картиночек из первой категории первую картинку,
    # запоминаем, какую ссылку содержит эта картиночка,
    # кликаем по первой картиночке
    first_pic = d.find_element_by_css_selector('a.serp-item__link')
    first_pic_link = first_pic.get_attribute('href')
    first_pic.click()
    time.sleep(1)
    first_pic_url = d.current_url
    assert first_pic_link != first_pic_url, \
        'Картинка не открылась'
    
    
    # картинка открылась крупно, запоминаем, какая конкретно картинка открылась, 
    # наводим на неё мышью, чтобы появились стрелки для перехода вправо
    pic_class = '[class="MMImage-Origin"]'
    move = d.find_element_by_css_selector('{}'.format(pic_class))
    pic0 = move.get_attribute('src')
    hover = ActionChains(d)
    big_pic1 = d.current_url
    hover.move_to_element(move).perform()
    
    # кликаем на кнопку "Вперед", чтобы перелистнуть на следующую картинку
    d.find_element_by_xpath("//div[contains(@class, 'CircleButton_type_next')]").click()
    time.sleep(1)  

    # запоминаем, какая именно картинка открылась после клика по кнопке "Вперед"
    move1 = d.find_element_by_css_selector('{}'.format(pic_class))
    pic1 = move1.get_attribute('src')
    assert pic0 != pic1, 'Картинки совпадают, при нажатии на кнопку "Вперед" картинка не изменяется'
    
    # кликаем по кнопке "Назад"
    d.find_element_by_xpath("//div[contains(@class, 'CircleButton_type_prev')]").click()
    time.sleep(1)
    
    # проверяем, какая картинка открылась после нажатия 
    move2 = d.find_element_by_css_selector('{}'.format(pic_class))
    pic2 = move2.get_attribute('src')
    assert pic0 == pic2, \
        'Картинки не совпадают, при возвращении на предыдующую картинку открывается не то изображение'


















    








    

