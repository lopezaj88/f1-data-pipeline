# Formula 1 Data Pipeline

This project automates the collection, processing, and integration of Formula 1 data using Python. It uses the [FastF1](https://theoehrly.github.io/Fast-F1/) library to gather data, outputs it as CSV files, uploads the data to a MySQL database for advanced queries, and prepares it for visualization in tools like Tableau Public.

## Features
- Collects lap times and pit stop data from Formula 1 races.
- Exports data as CSV files.
- Automates uploading CSV files to a MySQL database.
- Prepares data for manual upload to Tableau Public for visualization.
- Fully customizable via a `config.json` file.

---

## Directory Structure

```
/pipeline_project/
    /modules/               # Python modules for individual pipeline tasks
        driver_lap_times.py
        pit_stop_times.py
        upload_to_mysql.py
        driver_data_and_position.py
    /output_data/           # Folder to store generated CSV files
        (CSV files are saved here)
    config.json             # Configuration file
    pipeline.py             # Main pipeline script
```

---

## Installation

### Prerequisites
1. **Python 3.8+**: Install Python from [python.org](https://www.python.org/).
2. **MySQL**: Ensure MySQL is installed and running locally on your machine.
3. **MySQL Workbench** (optional): For managing your MySQL database visually.
4. **Tableau Public**: Download Tableau Public for data visualization from [tableau.com](https://public.tableau.com/).

### Step 1: Clone the Repository
```bash
git clone https://github.com/yourusername/f1-data-pipeline.git
cd f1-data-pipeline
```

### Step 2: Set Up a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate       # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### Step 3: Configure Environment Variables
Set up environment variables to store your MySQL credentials securely:
- **Linux/Mac**: Add these lines to your `~/.bashrc` (or `~/.zshrc`):
  ```bash
  export MYSQL_USER="your_username"
  export MYSQL_PASSWORD="your_password"
  ```
  Then, reload the file:
  ```bash
  source ~/.bashrc
  ```
- **Windows**:
  1. Open "Environment Variables" from the Start Menu.
  2. Add the variables `MYSQL_USER`, `MYSQL_PASSWORD`, `MYSQL_HOST`, `MYSQL_PORT`, and `MYSQL_DATABASE` under "System Variables."

### Step 4: Configure the Project
Edit `config.json` to set the race details and output directory:
```json
{
    "raceYear": 2024,
    "raceLocation": "Brazil",
    "sessionType": "R",
    "outputDirectory": "./output_data"
}
```

Edit the mysqlConfig dictionary in pipeline.py to set mySQL details:
```python
{
'host':'localhost',
'port':3306, # Default port for SQL
'user':os.getenv('MYSQL_USER'),
'password':os.getenv('MYSQL_PASSWORD'),
'database':'databaseName'
}
```

---

## Usage

### Run the Pipeline
To execute the entire pipeline, run:
```bash
python pipeline.py
```

This script:
1. Collects driver lap times, positions, points socred, and pit stop data for the specified race.
2. Saves the data as CSV files in the `/output_data/` folder.
3. Uploads the data to your MySQL database.
4. Prepares the CSV files for manual upload to Tableau Public.

### Manual Tableau Upload
1. Open Tableau Public.
2. Import the CSV files from the `/output_data/` folder.
3. Create dashboards and visualizations as desired.

---

## Modules

### 1. `driver_lap_times.py`
- Collects lap time data for all drivers in a specific race session.
- Outputs: `lapTimes_<year>_<location>.csv`.

### 2. `pit_stop_times.py`
- Collects pit stop data for all drivers in a specific race session.
- Outputs: `pitTimes_<year>_<location>.csv`.

### 3. `driver_position_and_points.py`
- Collects finishing position and points of all drivers in a specific race session.
- Outputs: `driverPositionPoints_<year>_<location>.csv`

### 4. `upload_to_mysql.py`
- Uploads CSV data to MySQL tables for advanced queries.

---

## Security

### Protecting Credentials
Sensitive credentials, such as MySQL passwords, are stored securely using environment variables. Do not hardcode these values or commit them to your repository.

To set up credentials:
1. Use environment variables as described in [Installation](#installation).
2. If using `.env` files with `python-dotenv`, ensure `.env` is added to `.gitignore`.

### `.gitignore`
Ensure sensitive files are excluded from the repository:
```
# Ignore environment variables
.env

# Ignore output files
/output_data/
```

---

## Contributing
Contributions are welcome! Please fork the repository, create a feature branch, and submit a pull request.

---

## License
This project is licensed under the MIT License. See `LICENSE` for details.

---

## Author
**Austin Lopez**  
[GitHub Profile](https://github.com/lopezaj88)  
Email: lopezaj88@gmail.com

