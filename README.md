## Geographic Expansion and Analysis Map
This project is a geospatial data visualization tool designed for business analysis. It generates an interactive HTML map from a JSON dataset, allowing for the mapping and analysis of operational points, areas of influence, and potential expansion sites for a company.

The system is ideal for market intelligence, strategic planning, and logistics teams who need a clear and customizable view of their field operations.

(Suggestion: Generate a map, take a screenshot, and place it in a docs/ folder for visual reference)

## Key Features
Interactive Map: Generates a standalone HTML file that requires no web server to run.

Multiple Layers: Allows toggling between a schematic map view ("Tactical") and high-resolution satellite imagery.

Areas of Influence: Visualizes a customizable radius of operation or influence for each point on the map.

Detailed Information: Displays specific information for each point through interactive popups when markers are clicked.

Dependency Visualization: Allows drawing lines between points to represent logistical flows, dependencies, or other relationships.

## 🛠️ Tech Stack
Python 3

Folium for generating interactive maps.

## Installation and Setup
To run this project locally, follow the steps below.

1. Clone the Repository

```Bash

git clone https://github.com/your-username/your-repository.git
cd your-repository
```
2. Create and Activate a Virtual Environment

```Bash

## Create the environment
python -m venv venv

## Activate on Windows (PowerShell)
.\venv\Scripts\Activate.ps1

## Activate on Linux / macOS
source venv/bin/activate
```

3. Install Dependencies
The project has minimal dependencies, listed in the requirements.txt file. To install them, run:

```Bash
pip install -r requirements.txt
```

📈 Usage
Edit the Input Data
Open the file data/centros_gravidade.json. This file contains the list of points that will be displayed on the map. Add, remove, or modify the JSON objects to reflect your company's data. See the Data Structure section below for more details.

Run the Generation Script
With the virtual environment activated, run the main script to generate the map:

```Bash
python main.py
```

View the Result
After execution, a new file will be created at output/mapa_tatico_cg.html. Open this file in any web browser (Chrome, Firefox, etc.) to view and interact with your custom map.

📊 Data Structure
To add your own points, edit the data/centros_gravidade.json file. It is a list of objects, where each object represents a point on the map and must follow the structure below:

| Key                | Type           | Description                                                                      | Example                                   |
| -------------------- | -------------- | ------------------------------------------------------------------------------ | ----------------------------------------- |
| `nome`               | String         | The name of the point of interest (e.g., Headquarters, Branch, Distribution Center).        | `"Porto de Santos"`                       |
| `tipo`               | String         | The category or type of the point.                                              | `"Logistics/Economic"`                   |
| `coord`              | Array (Float)  | The geographic coordinates in `[latitude, longitude]` format.          | `[-23.96, -46.30]`                        |
| `vulnerabilidade`    | Integer        | An index from 0 to 100. Can be used to represent priority, a risk score, or potential. | `70`                                    |
| `impacto`            | String         | Description of the strategic impact or function of the point.                   | `"Disruption of 40% of the import/export flow..."`      |
| `cor`                | String         | The color of the marker on the map (e.g., "red", "blue", "green", "orange").   | `"orange"`                                |
| `raio_influencia`    | Integer        | The radius of the influence area in meters.                                    | `20000`                                   |

🤝 Contributing
Contributions are welcome! Feel free to open an issue to report bugs or suggest new features. If you would like to contribute code, please open a Pull Request.

📄 License
This project is licensed under the MIT License.

