"""Задание 0. Генерация синтетических данных о продажах.

Дневные продажи 5 SKU за 2023–2025 годы (5 480 строк).
Код взят из методички руководителя без изменения логики;
seed вынесен в параметр командной строки.

Запуск из корня репозитория:
    python src/generate_data.py --seed 2026

seed = последние 4 цифры номера зачётной книжки.
"""
import argparse
from pathlib import Path

import numpy as np
import pandas as pd

# база, тренд/день, сила годовой сезонности, доля дней без продаж
SKUS = {
    "SKU_A": (40, 0.010, 0.25, 0.00),
    "SKU_B": (15, 0.004, 0.40, 0.00),
    "SKU_C": (8, 0.000, 0.10, 0.00),
    "SKU_D": (3, 0.001, 0.05, 0.35),  # прерывистый спрос
    "SKU_E": (60, -0.008, 0.15, 0.00),
}
DOW_EFFECT = np.array([0.9, 0.95, 1.0, 1.0, 1.1, 1.3, 1.2])  # пн..вс
HOLIDAYS = pd.to_datetime([
    "2023-03-21", "2024-03-21", "2025-03-21",   # Наурыз
    "2023-12-16", "2024-12-16", "2025-12-16",   # День Независимости
    "2023-12-31", "2024-12-31", "2025-12-31",   # Новый год
])
K = 5.0  # параметр отрицательного биномиального: var = mu + mu^2 / k


def generate(seed: int) -> pd.DataFrame:
    rng = np.random.default_rng(seed)
    dates = pd.date_range("2023-01-01", "2025-12-31", freq="D")
    t = np.arange(len(dates))
    rows = []
    for sku, (base, trend, season, zero_p) in SKUS.items():
        promo = rng.random(len(dates)) < 0.05
        price = 1000 * (1 - 0.2 * promo) * (1 + 0.00005 * t)
        mu = ((base + trend * t)
              * (1 + season * np.sin(2 * np.pi * (dates.dayofyear - 80) / 365.25))
              * DOW_EFFECT[dates.dayofweek]
              * np.where(promo, 1.6, 1.0)
              * np.where(dates.isin(HOLIDAYS), 1.8, 1.0))
        mu = np.clip(mu, 0.1, None)
        demand = rng.negative_binomial(K, K / (K + mu))
        demand = np.where(rng.random(len(dates)) < zero_p, 0, demand)
        rows.append(pd.DataFrame({
            "date": dates, "sku": sku, "demand": demand,
            "price": price.round(0), "promo": promo.astype(int),
            "holiday": dates.isin(HOLIDAYS).astype(int),
        }))
    return pd.concat(rows, ignore_index=True)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed", type=int, default=2026,
                        help="последние 4 цифры номера зачётной книжки")
    parser.add_argument("--out", type=Path,
                        default=Path(__file__).resolve().parents[1] / "data" / "sales.csv")
    args = parser.parse_args()

    df = generate(args.seed)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(args.out, index=False)
    print(f"seed={args.seed}: сохранено {len(df)} строк в {args.out}")


if __name__ == "__main__":
    main()
