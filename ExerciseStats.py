from os import path as os_path  # Import path
import pandas as pd
import datetime


class ExerciseStats:
    def __init__(self, folder="exercises/", exercise_file="exerciseStats.csv"):

        self.filepath = os_path.dirname(os_path.realpath(__file__))
        self.exercise_folder = self.filepath + "/" + folder
        self.folder = folder
        self.exercise_file = exercise_file

    def get_exercise_stats(self, exercise_number):
        path = self.exercise_folder + "" + self.exercise_file
        # tmp = pd.DataFrame.from_csv(path, index_col=0)
        tmp = pd.read_csv(path, index_col=0)

        duration, last_played = list(tmp.loc[exercise_number])[1:]

        return duration, last_played

    def update_exercise_stats(self, exercise_number):
        path = self.exercise_folder + "" + self.exercise_file
        # tmp = pd.DataFrame.from_csv(path)
        tmp = pd.read_csv(path)

        now = datetime.datetime.now()
        now = now.strftime("%Y-%m-%d")

        # tmp.set_value(exercise_number, "Last Played", now)

        # tmp.at[exercise_number, 12] = now  # <- mb?
        tmp.at[exercise_number, "Last Played"] = now

        tmp.to_csv(path)

