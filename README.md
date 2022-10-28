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
- pytest


 ## Interface and manual
 - To compare add two source codes(by file or write it by hand), then click 'compare' and you will see result.
 If you want to save compare, you need also to click 'save result'
 
 ![image](https://user-images.githubusercontent.com/114457052/198499426-8d5f0c17-e809-4844-a11d-13efd4e04d24.png)
 
 - If you want a custom appearance click on 'settings' button and choose whatever you like
 
 ![image](https://user-images.githubusercontent.com/114457052/198500208-d891df4a-3b5d-4e74-8983-e54347bef081.png)
 
 - To reproduce compare click on 'History' button, then by double click you can upload compare!
 
 ![image](https://user-images.githubusercontent.com/114457052/198500524-426b0d42-f47c-4f5b-94f1-e88233ab2281.png)
 
