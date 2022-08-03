How to run the script
1- enable execution of getGE11FOSData
   chmod +x scripts/getGE11FOSData
2- choose the FOS sensors to retieve 
   OPEN the scripts/getGE11FOSData
   all the sensors available are listed
   put a # in front of the sensors you DON'T want to retrieve
3- choose the start date and end date for data to retrieve
   Inside scripts/getGE11FOSData
   the variables to edit are StartTime and EndTime, in the following format (Line 77)
   StartTime='2022-08-01 00:00:01'
   EndTime='2022-08-02 23:59:59'
4- Run the script 
   ./scripts/getGE11FOSData
5- Make a list of files to plot 
   python scripts/lister.py
6- Run the plotter script
   python scripts/plotter.py
