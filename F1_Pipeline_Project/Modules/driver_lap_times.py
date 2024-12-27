import fastf1
import pandas as pd
import os

def collect_driver_lap_times(config):
    raceYear = config["raceYear"]
    raceLocation = config["raceLocation"]
    sessionType = config["sessionType"]
    outputFile = os.path.join(config["outputDirectory"], f"lapTimes_{raceYear}_{raceLocation}.csv")

    # Load session and collect data
    session = fastf1.get_session(raceYear, raceLocation, sessionType)
    session.load()
    laps = session.laps

    # Extract and save data
    df = laps[["Driver", "LapNumber", "LapTime", "Sector1Time", "Sector2Time", "Sector3Time", "Position", "Time"]]
    df.to_csv(outputFile, index=False)
    print(f"Lap times saved to {outputFile}")
    return outputFile
