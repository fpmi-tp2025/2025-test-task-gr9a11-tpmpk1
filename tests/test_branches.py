import subprocess

def get_branches():
    """Возвращает список всех веток в репозитории."""
    result = subprocess.run(['git', 'branch'], capture_output=True, text=True)
    branches = result.stdout.splitlines()
    # Удаляем префикс '* ' для текущей ветки
    branches = [branch.strip() for branch in branches if branch.strip() != '']
    return branches

def test_main_branch_exists():
    """Проверяет наличие ветки main."""
    branches = get_branches()
    assert 'main' in branches, "Ветка 'main' не найдена!"

def test_development_branch_exists():
    """Проверяет наличие ветки development."""
    branches = get_branches()
    assert 'development' in branches, "Ветка 'development' не найдена!"

