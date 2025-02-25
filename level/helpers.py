import pandas as pd

df = pd.read_csv("./data/levels.csv")


def get_level(exercise, bodyweight, orm):
    mask = (df["Exercise"] == exercise) & (
        df["Bodyweight"] == round(bodyweight / 10) * 10
    )
    row_dict = df.loc[mask, df.columns[1:-1]].squeeze().to_dict()
    level = min(row_dict, key=lambda k: abs(row_dict[k] - orm))
    level_candidates = {
        k: v for k, v in row_dict.items() if v <= orm
    }  # Only keep values ≤ orm

    if level_candidates:
        level = max(level_candidates, key=lambda k: level_candidates[k])
    return level, row_dict[level]


def get_level_metadata(level, exercise, bodyweight):
    mask = (df["Exercise"] == exercise) & (
        df["Bodyweight"] == round(bodyweight / 10) * 10
    )
    index = min(df.columns.get_loc(level) + 1, len(df.columns) - 1)
    next_level = df.columns[index]
    next_level_orm = df.loc[mask, next_level].squeeze()  # .to_dict()
    return next_level, next_level_orm


def calculate_orm(weight, reps):
    return weight * (1 + reps / 30)
