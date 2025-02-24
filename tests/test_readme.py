import os

def test_readme_exists():
    """Проверяет, существует ли файл README.md."""
    assert os.path.exists("README.md"), "Файл README.md не найден!"

def test_readme_content():
    """Проверяет наличие определенных строк в файле README.md."""
    with open("README.md", "r", encoding="utf-8") as file:
        content = file.read()

    # Проверка наличия заголовка
    assert "# Репозиторий КР1" in content, "Заголовок 'Репозиторий КР1' не найден в README.md"

    # Проверка наличия описания
    assert "Это репозиторий для" in content, "Описание репозитория не найдено в README.md"

    # Проверка наличия раздела с инструкцями по установке
    assert "## Установка" in content, "Раздел 'Установка' не найден в README.md"
    
    # Проверка наличия инструкций по установке
    assert "Сборка приложения выполняется" in content, "Описание сборки не найдено в README.md"
    
    # Проверка наличия сведений об авторе
    assert "## Автор" in content, "Раздел 'Автор' не найден в README.md"
    
    
    # Проверка наличия инструкций по установке
    assert "Контрольную работу 1 выполнил/а" in content, "Сведения об авторе не найдены в README.md"
    
def test_readme_contains_link():
    """Проверяет наличие ссылки в файле README.md."""
    try:
        with open("README.md", "r", encoding="utf-8") as file:
            content = file.read()

        # Используем регулярное выражение для поиска ссылок
        link_pattern = r'\[.*?\]\(.*?\)'
        links = re.findall(link_pattern, content)

        assert len(links) > 0, "В файле README.md не найдено ни одной ссылки!"
    

def test_readme_length():
    """Проверяет минимальную длину файла README.md."""
    with open("README.md", "r", encoding="utf-8") as file:
        content = file.read()

    # Проверка минимальной длины содержимого
    assert len(content) > 100, "Содержимое README.md слишком короткое!"
