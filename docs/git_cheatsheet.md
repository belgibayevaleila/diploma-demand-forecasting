# Git: основные команды

Git — система контроля версий: она запоминает историю изменений файлов.
GitHub — сайт, на котором хранится копия репозитория (remote), её видит руководитель.

## 1. Настройка (один раз на компьютере)

```bash
git --version                                   # проверить, что Git установлен
git config --global user.name "Имя Фамилия"     # имя автора коммитов
git config --global user.email "почта@github"   # та же почта, что в GitHub
git config --global init.defaultBranch main     # основная ветка — main
git config --list                               # посмотреть настройки
```

## 2. Создать или скачать репозиторий

```bash
git init                                        # сделать текущую папку репозиторием
git clone https://github.com/USER/REPO.git      # скачать репозиторий с GitHub
git remote add origin https://github.com/USER/REPO.git   # связать локальную папку с GitHub
git remote -v                                   # проверить, куда смотрит origin
```

## 3. Ежедневный цикл: изменить → добавить → зафиксировать → отправить

```bash
git status                     # что изменилось (красное — не добавлено, зелёное — добавлено)
git add файл.py                # добавить один файл в «индекс» (staging)
git add .                      # добавить все изменения в текущей папке
git commit -m "Задание 1: EDA" # зафиксировать снимок с понятным сообщением
git push                       # отправить коммиты на GitHub
git push -u origin main        # первый push: связать ветку main с origin
git pull                       # забрать изменения с GitHub (например, правки с другого ПК)
```

## 4. История и сравнение

```bash
git log --oneline --graph      # краткая история коммитов
git diff                       # что изменено, но ещё не добавлено
git diff --staged              # что добавлено, но ещё не закоммичено
git show <hash>                # содержимое конкретного коммита
```

## 5. Отмена изменений

```bash
git restore файл.py            # вернуть файл к последнему коммиту (локальные правки пропадут!)
git restore --staged файл.py   # убрать файл из индекса, правки остаются
git commit --amend -m "..."    # исправить сообщение последнего (ещё не отправленного) коммита
git revert <hash>              # безопасно отменить коммит новым коммитом
```

## 6. Ветки

```bash
git branch                     # список веток
git switch -c task-2           # создать ветку task-2 и перейти в неё
git switch main                # вернуться в main
git merge task-2               # влить task-2 в текущую ветку
git branch -d task-2           # удалить ветку после слияния
```

## 7. Файл `.gitignore`

В нём перечислено то, что **не** попадает в репозиторий: `.venv/`, `__pycache__/`,
`.ipynb_checkpoints/`, временные файлы LaTeX. Пароли и ключи API в репозиторий не добавляем никогда.

## 8. Правила для этого проекта

- Один коммит — одно логическое изменение: `Задание 2: Хольт–Винтерс и MAE/RMSE/MASE`.
- Перед `git push` выполните в ноутбуке **Restart & Run All**: руководитель проверяет по GitHub.
- После каждого задания обновляйте таблицу статусов в `README.md`.

## Пример: как был создан этот репозиторий

```bash
git init
git add .
git commit -m "Задания 0–1: данные, EDA, обзор литературы, README"
git remote add origin https://github.com/USER/diploma-demand-forecasting.git
git push -u origin main
```
