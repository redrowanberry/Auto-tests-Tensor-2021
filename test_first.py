from selenium import webdriver as wd
from selenium.webdriver.common.keys import Keys

def test_search():
    d = wd.Chrome()
    d.implicitly_wait(1)
    d.get('https://yandex.ru/')

    # проверяем наличие поля поиска
    search = d.find_element_by_id('text')
    assert search != None, \
        'На странице поиска нет поля для ввода запроса'
    
    # вводим в строку поиска "Тензор"
    search.send_keys('Тензор')
    
    # нажимаем клавишу "Вниз" на клавиатуре, чтобы увидеть таблицу подсказок
    search.send_keys(Keys.ARROW_DOWN)
    suggests = d.find_element_by_css_selector('ul.mini-suggest__popup-content')
    assert suggests != None, \
        'Таблица подсказок не появилось'

    # переходим на страницу результатов поиска
    search.send_keys(Keys.ENTER)

    # проверяем, есть ли на открывшейся странице непосредственно таблица результатов поиска
    result = d.find_element_by_id('search-result')
    assert result != None, \
        'Таблица результатов поиска не появилась'
    
    # проверяем, есть ли в первых пяти результатах поиска ссылка на https://tensor.ru/
    links = []
    for pos in range(1,6):
        s_links = d.find_element_by_css_selector('[accesskey="{}"]'.format(pos))
        links.append(s_links.get_attribute('href'))
        

    tensor_inc = False
    for link in links:
        if link == 'https://tensor.ru/':
            tensor_inc = True
    assert tensor_inc == True, \
        'В первых 5 результатах поиска нет ссылки на https://tensor.ru/, есть другие: {}'.format(links)
    d.quit()