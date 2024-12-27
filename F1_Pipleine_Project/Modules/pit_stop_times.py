import fastf1
import pandas as pd
import os

def collect_pit_stop_times(config):
    raceYear = config["raceYear"]
    raceLocation = config["raceLocation"]
    sessionType = config["sessionType"]
    outputFile = os.path.join(config["outputDirectory"], f"pitTimes_{raceYear}_{raceLocation}.csv")

    # Load session and collect data
    session = fastf1.get_session(raceYear, raceLocation, sessionType)
    session.load()
    laps = session.laps

    # Extract and save data
    # Filter rows where PitInTime or PitOutTime is not NaT
    filteredLaps = laps[(laps['PitInTime'].notna()) | (laps['PitOutTime'].notna())]

    # Convert PitInTime and PitOutTime to numeric values (seconds)  
    def convertToSeconds(timedeltaSeries):
        """Converts a timedelta series to total seconds."""
        return timedeltaSeries.dt.total_seconds()

    filteredLaps['PitInTime'] = pd.to_timedelta(filteredLaps['PitInTime'])
    filteredLaps['PitOutTime'] = pd.to_timedelta(filteredLaps['PitOutTime'])

    filteredLaps['PitInTime'] = convertToSeconds(filteredLaps['PitInTime'])
    filteredLaps['PitOutTime'] = convertToSeconds(filteredLaps['PitOutTime'])

    # Select relevant columns for export
    df = filteredLaps[['Driver', 'LapNumber', 'Stint', 'PitInTime', 'PitOutTime']]
    df.to_csv(outputFile, index=False)
    print(f"Pit Times saved to {outputFile}")
    return outputFile
