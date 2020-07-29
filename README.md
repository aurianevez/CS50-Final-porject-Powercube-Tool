# CS50-Final-project-Powercube-Tool

The purpose of this Flask webapp is to offer a structure that allows the user to complete its PowerCube analysis directly into a form that contains all the element of the  framework, and to render a styled document of this analysis. 

<p align="center">
     <img width ="600" src="/gif readme/presentation.gif">
</p>    



## Motivation

This is the final project for the CS50 class. I wanted this project to be meaningful as well as useful. So I decided to link two of my passions which are social and environmental justice with coding! In the past, I have use the power cube to analyse power dynamic created by partcipatory methods for a research project. As I was implementing this framework to my analysis, I created an excel spread sheet to save the different elements of my analysis on the same page, which would allow me to have a global vision of my work. I decided to creat this app in order to facilitate the process of analysing and having a styled result at the end.

## Built with

* Python
* Flask
* sqlite3
* HTLM / CSS / JavaScript /Bootstrap

## Getting Started !

### If you are a complete Newbie do the following step:

1. You need to download an editor, I personaly use [Visual Studio Code](https://code.visualstudio.com/?wt.mc_id=DX_841432)

2. You need to install python3    
    
    *The mac version will be added once I'll have access to a mac to test the procedure*
	
    On Windows:
    
    * in your search bar search the "Command Prompt" program (that is already in your computer) - Open it 
    * Once it's open type `python` and press Enter
    * if python is already install on your computer you should see this message :  
    
    	```
        Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:57:54) [MSC v.1924 64 bit (AMD64)] on win32
        Type "help" "copyright", "credits" or "license" for more information.
        ``` 
     * If python is not install the Miscroft Store will open (if not search it in the search bar) and will offer you to download the latest version of python. Click on 	download. Once it's done go back to the "Command Prompt" program and type Python again, you should get the message as cited previously. Make sur you exit python and press CTLR + z and then Enter.
     
     * In the "Command Prompt" make sur that pip is instaled, type `pip -V`and press enter. If it's installed you should get the following message:

        ```
        pip 20.1.1 from C:\Program Files\WindowsApps\PythonSoftwareFoundation.
        Python.3.8_3.8.1520.0_x64__qbz5n2kfra8p0\lib\site-packages\pip (python 3.8)
        ```   
	     
     * You can close the the "Command Prompt" program.  
     
3. You need to install sqlite3
      
     On Windows:
      
     * Go to the Sqlite [download page](https://www.sqlite.org/download.html):
      
     * In the download page go to the Precompiled Binaries for Windows - Download the __sqlite-tools__-win32. It will download as a zip folder.  
     
     * Go to the explorer - in Local Disck (C:) create a new foler called sqlite. Once you have created the folder, extract and copy the elements that are in the zip folder and paste them in the sqlite folder you just created. You should have: qlite3.def, sqlite3.dll and sqlite3.exe files.
      
     * Now you need to add a PATH in the system environment. To do so, in your search bar search the program(already in your computer): "Edit the system environement variables". Once it is open, click on environment variable button at the bottom of the tiny window - In system variables slect PATH and edit (right picture bellow) - click on new and write the path that you can copy from the folder file (C:\sqlite - see in the left picture bellow)

<br>
 
<p align="center">
     <img width ="500" src="/gif readme/sqlite_path.gif">
</p>    
<p align="center">
     <img width ="400" src="/gif readme/environment_variable.gif">  
</p>

4. Now, You can set up your environment:  

    Open visual studio code:  
       
    * In the nav bar click on terminal and then new terminal. A window should appear at the bottom of the screen  
    * First we need to make sure that python is set up in the environment. To do so press ctrl+shift+P and tiny windows should open at the top of the screen like in the image bellow and type `Python: select interpretor` (if nothing appear, don't worry, go to the next step :) !):  
		
	<p align="center">
		<img width ="400" src="/gif readme/setting_python.gif">
	</p>    

	* If nothing appeared when you typed `Python: select interpretor`, that means we need to install python in visual studio as well, on the left of the screen there is a 	vertical side bar, select the element with four square and type python in the search bar - select the first element called python and click on the tiny bleu square 		install (of course in the gif I don't the install bleu button because it is already installed on my computer). Once it's stop execute the previous step, this time you should be able to select an interpretor!
	
	<p align="center">
		<img width ="600" src="/gif readme/python_vs.gif">
	</p>   
	
	Then:  
		
	* You can install Flask, in the terminal type: `pip install Flask` and press enter  
		

## Running the webapp in your environment!

__Download the files from the github repro and open them in visual studio__ :

* In one folder you should have the following elements:  
	* application.py
	* a folder called: templates
	* a folder called: static
	* analysis.sqlite3
* From visual studio code in the nav bar click on file and then open folder select the folder with the cited elements.

On windows:  



  If you terminal runs on powershell: 
  <p align="center">
  <img width ="700" src="/gif readme/powershell.gif">
	</p>

  * in the terminal type `$env:FLASK_APP="application.py"` and press enter
  * still in the terminal type : `python -m flask run` and press enter
  * Flask will start running and it will provide you a link (http://127.0.0.1:5000/), when you click on it, it will redirect you to the webapp! 
  <p align="center">
  <img width ="700" src="/gif readme/running.gif">
  </p>
  
  ## Once the webapp is running
  
  When you start running the app, table in a database (that will containt your analysis) will be created. Every new analysis and all the modification to existing one will be saved in the database. If you stop running the webapp and run it another day the database (analysis.sqlite3) will be in your folder with all the other files needed to run the app. Therefore you will have access to everything you have saved previously. To stop running the webapp in the terminal press CTRL + C (for crash).     
  
  * If you want to erase all your analysis: 
  	* First you need to stop the webapp if tis running execute CTRL + C in the terminal to stop anything running.
	* go into your terminal and type : `sqlite3 analysis.sqlite3` and press enter 
	* like in the exemple bellow you shoud see that now you are running "in" sqlite3 --> `sqlite>`
	* you can now type some sqlite query. In this case we want to `DROP TABLE`, in other words delete table. type the following:
		* `DROP TABLE forms;` press enter
		* `DROP TABLE levels;`press enter
		* `DROP TABLE spaces;`press enter
		* `DROP TABLE users;`press enter
		* To exit sqlite press CTRL + C or CLTR + Z + ENTER
	<p align="center">
  	<img width ="700" src="/gif readme/sqlite_drop.gif">
  	</p>
		
		
  
  __Extracting your analysis__    
  * Once you have choosen which analysis to extract and press on the extract button, you will be redirected to a page with your analysis to save it click right, select print, save as a pdf. Dont hesitate to go back in the form analysis and play with extra space to have the final result the way you want :) 
   <p align="center">
  <img width ="700" src="/gif readme/print.gif">
  </p>
  
  ## Acknowledgement and Contact 
  
  I would like to thank particularly the support that I have received while creating this project as well as all the stackoverflow contributors !   
  
  You can contact me at auriane.vez[at]gmail.com, any contribution are welcomed :). Also if my explanation are unclear contact me!
  
 
  

