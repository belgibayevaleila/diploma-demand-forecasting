# VS Code: установка и запуск проекта (Windows)

## 1. Установка

1. Скачать VS Code: <https://code.visualstudio.com/> → **Download for Windows** → установить
   (отметить «Add to PATH» и «Open with Code»).
2. Установить Python 3.11+ с <https://www.python.org/downloads/> (отметить **Add python.exe to PATH**).
3. Установить Git: <https://git-scm.com/download/win>.
4. В VS Code открыть **Extensions** (`Ctrl+Shift+X`) и установить:
   - **Python** (Microsoft)
   - **Jupyter** (Microsoft)
   - *(по желанию)* **LaTeX Workshop**, **GitLens**, **Rainbow CSV**

## 2. Открыть проект

```powershell
cd $HOME\Documents
git clone https://github.com/<логин>/diploma-demand-forecasting.git
code diploma-demand-forecasting
```

## 3. Виртуальное окружение и библиотеки

В терминале VS Code (`` Ctrl+` ``):

```powershell
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

Если PowerShell запрещает активацию: `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned`.

`Ctrl+Shift+P` → **Python: Select Interpreter** → выбрать `.venv`.

## 4. Данные и первичный анализ

```powershell
python src/generate_data.py --seed 2026    # заменить 2026 на 4 последние цифры зачётки
```

Открыть `notebooks/01_eda.ipynb` → вверху справа **Select Kernel** → `.venv` → **Run All**.
Графики сохраняются в `reports/figures/`, сводная таблица — в `reports/eda_summary.csv`.

## 5. Отправить изменения на GitHub

Слева панель **Source Control** (`Ctrl+Shift+G`): написать сообщение → **Commit** → **Sync Changes**.
Или командами из `docs/git_cheatsheet.md`.
