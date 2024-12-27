import fastf1
import pandas as pd 
import os

def collect_driver_position_and_points(config):
    raceYear = config['raceYear']
    raceLocation = config['raceLocation']
    sessionType = config['sessionType']
    outputFile = os.path.join(config['outputDirectory'], f'driverPositionPoints_{raceYear}_{raceLocation}.csv')
    
    # Load session and collect data
    session = fastf1.get_session(raceYear, raceLocation, sessionType)
    session.load()
    
    # Initialize a list to store driver data
    driverDataList = []

    # Iterate through results using iterrows to gather data
    for _, row in session.results.iterrows():
        driverAbbr = row['Abbreviation']  # Driver abbreviation
        teamName = row['TeamName']  # Team name
        points = row['Points']  # Points scored
        startingPosition = row['GridPosition']  # Starting grid position
        finishingPosition = row['Position']  # Final race position

        # Collect data into a dictionary
        driverData = {
            "driver": driverAbbr,
            "team": teamName,
            "startingPosition": startingPosition,
            "finishingPosition": finishingPosition,
            "points": points
        }
        driverDataList.append(driverData)

    # Convert the list of driver data to a pandas DataFrame
    df = pd.DataFrame(driverDataList)

    # Save the DataFrame to a CSV file
    df.to_csv(outputFile, index=False)
    print(f'Driver Position and Points saved to {outputFile}')
    return outputFile