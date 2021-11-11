# **IPL Dataset Analytics**
## **Aim**
The main Goal of this project is to convert the raw open data into charts that tell some kind of story
## **Problem Statements**
   **1. Total runs scored by team**

Plot a chart of the total runs scored by each teams over the history of IPL. Hint: use the total_runs field.

**2. Top batsman for Royal Challengers Bangalore**

Consider only games played by Royal Challengers Bangalore. Now plot the total runs scored by every batsman playing for Royal Challengers Bangalore over the history of IPL.

**3. Foreign umpire analysis**

Obtain a source for country of origin of umpires. Plot a chart of number of umpires by in IPL by country. Indian umpires should be ignored as this would dominate the graph.

**4. Stacked chart of matches played by team by season**

Plot a stacked bar chart of ...

* number of games played
* by team
* by season
## **Steps followed to reach the Goal**
  1. Created and activated separate virtual environment for this project.
  2. pylint is enabled in VS Code.
  3.  A separate Repo is created for this project in Local machine
  4. Required datasets(CSV files) that are umpires, matches and deliveries are downloaded.And they are placed in project repo.
  5. To picturize the data "matplot" is needed. So, matplot is installed with pip3.
  6. After that based on each problem statement the code is written accordingly.
  7. After that, to run the file just click on run or to run it in terminal...
  ```
    python3 filename
  ```
  8. After that the all changes are staged and committed.
  9. Finally, the repo is pushed into Github.