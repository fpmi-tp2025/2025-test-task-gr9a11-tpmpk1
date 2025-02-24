import os

def test_src_directory_exists():
    """Проверяет наличие папки src."""
    assert os.path.isdir("src"), "Папка 'src' не найдена!"

def test_c_files_in_src():
    """Проверяет наличие файлов с исходным кодом на языке C в папке src."""
    if os.path.isdir("src"):
        c_files = [f for f in os.listdir("src") if f.endswith(".c")]
        assert len(c_files) > 0, "В папке 'src' не найдены файлы с расширением .c"
    else:
        assert False, "Папка 'src' не найдена!"
