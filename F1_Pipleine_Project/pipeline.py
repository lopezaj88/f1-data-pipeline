from Modules.driver_lap_times import collect_driver_lap_times
from Modules.pit_stop_times import collect_pit_stop_times
from Modules.driver_position_and_points import collect_driver_position_and_points
from Modules.upload_to_mysql import upload_to_mysql
import json
import os

mysqlConfig = {
    'host': 'localhost',
    'port': 3306,
    'user': os.getenv('MYSQL_USER'),
    'password': os.getenv('MYSQL_PASSWORD'),
    'database': 'databaseName'
}

# Load configuration
with open("config.json") as configFile:
    config = json.load(configFile)

def main():
    outputDir = config["outputDirectory"]
    os.makedirs(outputDir, exist_ok=True)

    # Step 1: Collect data
    lapFile = collect_driver_lap_times(config)
    pitFile = collect_pit_stop_times(config)
    positionPointsFile = collect_driver_position_and_points(config)

    # Step 2: Upload to MySQL
    upload_to_mysql(lapFile, "lap_times", config["mysql"])
    upload_to_mysql(pitFile, "pit_times", config["mysql"])
    upload_to_mysql(positionPointsFile, 'driver_position_points', config['mysql'])

    print(f"Data pipeline completed. CSVs are ready for Tableau in {outputDir}.")

if __name__ == "__main__":
    main()
