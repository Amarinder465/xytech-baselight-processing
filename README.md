# Xytech Baselight Processing

This script processes Xytech and Baselight files to generate a consolidated output in CSV format.

## Usage

### Prerequisites
- Python 3.x installed

### Running the Script
1. Clone or download this repository.
2. Open a terminal in the project directory.

3. Run the script with the following command:
    ```bash
    python Sorting_Frames.py xytech_file_path baselight_file_path
    ```
    Replace `xytech_file_path` and `baselight_file_path` with the paths to your Xytech and Baselight files.

## Script Overview

The script performs the following tasks:
- Reads data from Xytech and Baselight files.
- Extracts paths, roles, and notes from Xytech data.
- Combines information from Baselight and Xytech based on specified criteria.
- Generates an output CSV file with sorted information.

## Example Data

### Xytech Workorder 1107

- Producer: Joan Jett
- Operator: John Doe
- Job: Dirtfixing

#### Location:
- /hpsans13/production/starwars/reel1/partA/1920x1080
- /hpsans12/production/starwars/reel1/VFX/Hydraulx
- /hpsans13/production/starwars/reel1/VFX/Framestore
- /hpsans14/production/starwars/reel1/VFX/AnimalLogic
- /hpsans13/production/starwars/reel1/partB/1920x1080
- /hpsans15/production/starwars/pickups/shot_1ab/1920x1080

#### Notes:
Please clean files noted per Colorist Tom Brady

#### Image Paths and Frame Numbers:
- /images1/starwars/reel1/partA/1920x1080: 32 33 34 67 68 69 122 123 155 1023 1111 1112 1160 1201 1202 1203 1204 1205 1211 1212 1213 1214
- /images1/starwars/reel1/VFX/Hydraulx: 1251 1252 1253 1260 <err> 1270 1271 1272
- ...

## Output

The script generates an output CSV file named `output.csv` with sorted information.
EXAMPLE
Joan Jett,John Doe,Dirtfixing,Please clean files noted per Colorist Tom Brady 
 

/hpsans13/production/starwars/reel1/partA/1920x1080,32-34
/hpsans13/production/starwars/reel1/partA/1920x1080,67-69
/hpsans13/production/starwars/reel1/partA/1920x1080,122-123
...

---

Feel free to enhance this README with more details about your project, usage instructions, and any other relevant information.
