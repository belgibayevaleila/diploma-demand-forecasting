# LaTeX / Overleaf: основные команды

Overleaf — онлайн-редактор LaTeX: слева исходный код `.tex`, справа PDF.
Компиляция: **Recompile** или `Ctrl + S` / `Ctrl + Enter`.
Для русского текста: **Menu → Compiler → pdfLaTeX** и преамбула ниже.

## 1. Каркас документа

```latex
\documentclass[12pt,a4paper]{article}
\usepackage[T2A]{fontenc}            % кириллица
\usepackage[utf8]{inputenc}
\usepackage[english,russian]{babel}  % русские переносы и «Содержание»
\usepackage{amsmath,amssymb}         % формулы
\usepackage{graphicx}                % рисунки
\usepackage{booktabs}                % красивые таблицы
\usepackage[hidelinks]{hyperref}     % кликабельные ссылки

\title{Обзор литературы}
\author{Студент}
\begin{document}
\maketitle
\tableofcontents
\section{Введение}
Текст...
\end{document}
```

## 2. Текст

| Что | Команда |
|-----|---------|
| Раздел / подраздел | `\section{...}`, `\subsection{...}`, `\subsubsection{...}` |
| Новый абзац | пустая строка |
| **Жирный**, *курсив* | `\textbf{...}`, `\emph{...}` |
| «Ёлочки» | `<<текст>>` |
| Тире / диапазон | `---` (тире), `--` (2016--2026) |
| Неразрывный пробел | `~` (`О.~А.~Тихонова`, `рис.~\ref{fig:1}`) |
| Комментарий | `% это не попадёт в PDF` |
| Списки | `\begin{itemize} \item ... \end{itemize}`, `enumerate` — нумерованный |

## 3. Формулы

| Что | Код | Результат |
|-----|-----|-----------|
| В строке | `$a^2 + b^2$` | $a^2+b^2$ |
| Отдельной строкой с номером | `\begin{equation} ... \label{eq:nv} \end{equation}` | (1) |
| Без номера | `\[ ... \]` | |
| Индексы, степени | `x_i`, `x^{2}`, `\mu_{it}` | $x_i$, $x^2$, $\mu_{it}$ |
| Дробь, корень | `\frac{C_u}{C_u+C_o}`, `\sqrt{L+R}` | |
| Сумма, мат. ожидание | `\sum_{i=1}^{n}`, `\mathbb{E}` | |
| Греческие | `\alpha \beta \mu \sigma \tau \lambda` | |
| Скобки по размеру | `\left( ... \right)` | |
| Кусочная функция | `\begin{cases} ... & y \ge q \\ ... & y < q \end{cases}` | |
| Ссылка на формулу | `формула~\eqref{eq:nv}` | формула (1) |

Пример из обзора (оптимальный заказ в задаче о газетчике):

```latex
\begin{equation}\label{eq:cr}
  q^{*} = F^{-1}\!\left(\frac{c_u}{c_u + c_o}\right)
\end{equation}
```

## 4. Рисунки и таблицы

```latex
\begin{figure}[h]
  \centering
  \includegraphics[width=0.9\textwidth]{figures/fig1_demand_rolling.png}
  \caption{Дневной спрос и скользящее среднее}
  \label{fig:demand}
\end{figure}

\begin{table}[h]
  \centering
  \caption{Классы спроса}
  \begin{tabular}{lrrl}
    \toprule
    SKU & ADI & CV$^2$ & Класс \\
    \midrule
    SKU\_D & 1,71 & 0,39 & intermittent \\
    \bottomrule
  \end{tabular}
\end{table}
```

Картинки загружаются в Overleaf кнопкой **Upload** (значок со стрелкой над списком файлов).
Символ `_` в тексте экранируется: `SKU\_A`.

## 5. Список литературы (BibTeX, ГОСТ)

1. Записи хранятся в `references.bib` (`@article{ban2019bigdata, author=..., title=..., ...}`).
2. В тексте: `\cite{ban2019bigdata}` → [3].
3. В конце документа:
   ```latex
   \bibliographystyle{ugost2008}
   \bibliography{references}
   ```
BibTeX-запись почти любой статьи можно скопировать из Google Scholar (кнопка «Цитировать» → BibTeX).

## 6. Совместная работа в Overleaf

- **Share** → ввести e-mail → *Can edit* или *Can view* → **Invite**.
- **History** — история изменений, можно вернуться к старой версии.
- **Review** — комментарии руководителя прямо в тексте.
- **Menu → Download** — скачать PDF или исходники (`.zip`).
