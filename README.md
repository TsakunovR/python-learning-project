# Учебный Python-проект

Минимальный проект для изучения Python и автоматизации тестирования. Работает на Windows и macOS.

## Что нужно перед началом

- Установленный Python 3.11
- Терминал (командная строка)

## Пошаговая инструкция

### 1. Клонирование репозитория

Если проект уже скачан — переходите к шагу 2.

Если используете Git:

```bash
git clone <адрес-репозитория>
cd python-learning-project
```

### 2. Создание виртуального окружения (venv)

**macOS / Linux:**

```bash
python3 -m venv venv
```

**Windows (командная строка cmd):**

```cmd
python -m venv venv
```

**Windows (PowerShell):**

```powershell
python -m venv venv
```

### 3. Активация виртуального окружения

**macOS / Linux:**

```bash
source venv/bin/activate
```

**Windows (cmd):**

```cmd
venv\Scripts\activate.bat
```

**Windows (PowerShell):**

```powershell
venv\Scripts\Activate.ps1
```

После активации в начале строки терминала появится `(venv)`.

### 4. Установка зависимостей

```bash
pip install -r requirements.txt
```

### 5. Запуск программы

```bash
python main.py
```

Должно вывестись: **Проект успешно запущен!**

### 6. Запуск тестов

```bash
python -m pytest
```

Все тесты должны пройти успешно (зелёный вывод).

---

## Структура проекта

- `main.py` — основной код (функции и точка входа)
- `tests/test_example.py` — пример тестов
- `requirements.txt` — список библиотек для установки

Удачи в обучении!
