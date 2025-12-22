import os
from pages.saby_main_page import SabyMainPage
from pages.saby_download_page import SabyDownloadPage

def test_download_sbis_plugin(driver):
    saby_main = SabyMainPage(driver)
    saby_download = SabyDownloadPage(driver)
    
    # 1. Открываем saby.ru
    saby_main.open()
    
    # 2. Переходим в "Скачать локальные версии"
    saby_main.open_download_page()
    
    # 3. Скачиваем плагин и получаем ожидаемый размер
    expected_size_mb = saby_download.download_sbis_plugin()
    
    # Стандартное имя файла
    file_name = "sbisplugin-setup-web.exe"
    
    # 4. Ждем завершения скачивания
    file_path = saby_download.wait_for_download(file_name)
    
    assert file_path is not None, "Файл не был скачан за отведенное время"
    assert os.path.exists(file_path), "Файл отсутствует на диске"

    # 5. Проверяем размер файла
    actual_size_bytes = os.path.getsize(file_path)
    actual_size_mb = round(actual_size_bytes / (1024 * 1024), 2)
    
    # Удаляем файл после теста
    if os.path.exists(file_path):
        os.remove(file_path)

    assert actual_size_mb == expected_size_mb, \
        f"Размер файла не совпадает! Ожидали {expected_size_mb} МБ, получили {actual_size_mb} МБ"