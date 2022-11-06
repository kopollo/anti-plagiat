# Anti-plagiat
Check similarity of python source codes with convenient user interface
 ## Features
- Amazing algorithm to compare python code by levenshtein distance
- Opportunity to upload source code from file
- Saving result of compare in database
  - Input Source codes
  - similarity percentage 
  - datetime
- Possibility to reproduce compare from database using the interface
- Supports custom appearance
  - font
  - font size
  - dark/light theme

 ## Dependencies
 - PyQt5
 - pyqt5-tools
 - PyQt5-stubs

## Codestyle linters and test frameworks
The project has been checked and tested with the following tools:
- flake8
- mypy
- pydocstyle
- pytest
## How to start
- By entrance point - main.py
- By .exe file which you can find in https://disk.yandex.ru/d/nvngAcscoKwfoQ


 ## Interface and manual
 - To compare add two source codes(by file or write it by hand), then click 'compare' and you will see result.
 If you want to save compare, you need also to click 'save result'
 
![test_compar2](https://user-images.githubusercontent.com/114457052/200168938-0c3b8656-8c89-451b-9964-91f0c3b7bb5b.gif)
 - If you want a custom appearance click on 'settings' button and choose whatever you like
 
![test_settings2](https://user-images.githubusercontent.com/114457052/199976717-75d0bf29-4eb2-4b60-ab06-c1bf47b854c6.gif)
 
 - To reproduce compare click on 'History' button, then by double click you can upload compare!
 
 ![image](https://user-images.githubusercontent.com/114457052/198500524-426b0d42-f47c-4f5b-94f1-e88233ab2281.png)
 
