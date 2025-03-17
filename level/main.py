import pandas as pd
import streamlit as st

import level.helpers as H

df = pd.read_csv("./data/levels.csv")
# bodyweight = st.sidebar.number_input(
#     "Enter Bodyweight", min_value=110, max_value=310, step=1
# )
bodyweight = 200
exercise = st.sidebar.selectbox("Exercises", options=df["Exercise"].unique())
weight = st.sidebar.number_input("Enter Weight", min_value=0, step=5)
reps = st.sidebar.number_input("Enter Reps", min_value=0, step=1)


orm = int(H.calculate_orm(weight, reps))
level, level_orm = H.get_level(exercise, bodyweight, orm)
next_level, next_level_orm = H.get_level_metadata(level, exercise, bodyweight)
level_range = next_level_orm - level_orm
level_percent = int(round((orm - level_orm) / level_range, 2) * 100)


if __name__ == "__main__":
    st.metric("Level", f"{level}")
    st.metric("Progress", f"{level_percent}%")
    st.metric("Current ORM:", orm)
    # st.metric("Lvl ORM", level_orm)
    st.metric("Next Lvl", next_level_orm)
