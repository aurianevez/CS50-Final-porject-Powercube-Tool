from flask import Flask, render_template, request, redirect
import sqlite3
from sqlite3 import Error


# configure application
app = Flask(__name__)

# templates auto-reload
app.config["TEMPLATES_AUTO_RELOAD"] = True


#configuration sqlite
# connecting to SQLite database
connection = sqlite3.connect('analysis.sqlite3', check_same_thread=False)

#crearing a cursor
db = connection.cursor()

#----------- creation of db's tables -----------#
# users 
db.execute('''CREATE TABLE IF NOT EXISTS 'users'('id' INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 'title' TEXT)''')

# forms 
db.execute('''CREATE TABLE IF NOT EXISTS 'forms' ('analysis_id' INT, 'visible' TEXT, 'invisible' TEXT, 'hidden' TEXT)''')

# spaces
db.execute('''CREATE TABLE IF NOT EXISTS 'spaces' ('analysis_id' INT, 'closed' TEXT, 'invited' TEXT, 'created' TEXT)''')

#levels
db.execute('''CREATE TABLE IF NOT EXISTS 'levels' ('analysis_id' INT,'level_1_chosen' TEXT, 'level_1' TEXT, 'level_2_chosen' TEXT, 'level_2' TEXT, 'level_3_chosen' TEXT, 'level_3' TEXT, 'level_4_chosen' TEXT, 'level_4' TEXT, 'level_5_chosen' TEXT, 'Level_5' TEXT, 'level_6_chosen' TEXT, 'Level_6' TEXT)''')


#------------- Index ------------#

@app.route('/')
def index():
    return render_template("index.html")

#------------- About ----------------#
@app.route("/about")
def about():
    return render_template('about.html')

#------------ Analysis -------------#
@app.route("/analysis", methods=["GET", "POST"])
def power_analysis():
   
    if request.method == "GET":

        return list_existing_analysis_title()
     
    if request.method == "POST":
        
        # retriving analysis_id from the post method formular after the first run of the program
        analysis_id = request.form.get('analysis_id')
       
        actual_title = None

        # retriving from the get formular the title for a new analysis or the analysis selected from the rolldown menu
        title = request.form.get('title')
        title_in_database = request.form.get('title_in_database')
    
        
        # inserting new analysis into the database and defining actual_title
        if title is not None:  
            actual_title = title     
            db.execute("INSERT INTO users ('title') VALUES (?)", (title,))
            connection.commit()
        
        # if selected from the rolldown menu, defining actual_title
        if title_in_database is not None:
            actual_title = title_in_database
     
        
        # if analysis_id = none because it is the first run of the code then:
        if analysis_id is None and actual_title is not None:
            analysis_id = get_analysis_id_by_title(actual_title)
          

        # updating title of analysis from post form
        title_update = request.form.get('title_update')
        if title_update is not None:
            db.execute("UPDATE users SET title = ? WHERE id = ?", (title_update, analysis_id))
            connection.commit()
            
        #----------------- forms -----------------#
        # retrieving element from the form
        visible = request.form.get('visible')
        invisible = request.form.get('invisible')
        hidden = request.form.get('hidden')

        db.execute("SELECT * FROM forms WHERE analysis_id =:analysis_id", {'analysis_id':analysis_id})
        Forms = db.fetchone()
        
        # if first entry
        if Forms is None and visible is not None:
            db.execute("INSERT INTO forms ('analysis_id', 'visible') VALUES (?, ?)", (analysis_id, visible))
        
        # otherwise update
        if visible is not None:
            db.execute("UPDATE forms SET visible = ? WHERE analysis_id = ?", (visible, analysis_id))
        
        # saving commit and changes
        connection.commit()
        
        # if first entry
        if Forms is None and invisible is not None:
            db.execute("INSERT INTO forms ('analysis_id', 'invisible') VALUES (?, ?)", (analysis_id, invisible))
        
        # otherwise update
        if invisible is not None:
            db.execute("UPDATE forms SET invisible = ? WHERE analysis_id = ?", (invisible, analysis_id))
        
        # saving commit and changes
        connection.commit()
        
        # if first entry
        if Forms is None and hidden is not None:
            db.execute("INSERT INTO forms ('analysis_id', 'hidden') VALUES (?, ?)", (analysis_id, hidden))
        
        # otherwise update
        if hidden is not None:
            db.execute("UPDATE forms SET hidden = ? WHERE analysis_id = ?", (hidden, analysis_id))
        
        # saving commit and changes
        connection.commit()

        #--------------------------- levels ---------------------------------#

        # retrieving element form the form
        level_1 = request.form.get('level_1')
        level_2 = request.form.get('level_2')
        level_3 = request.form.get('level_3')
        level_4 = request.form.get('level_4')
        level_5 = request.form.get('level_5')
        level_6 = request.form.get('level_6')

        level_1_chosen = request.form.get('level_1_chosen')
        level_2_chosen = request.form.get('level_2_chosen')
        level_3_chosen = request.form.get('level_3_chosen')
        level_4_chosen = request.form.get('level_4_chosen')
        level_5_chosen = request.form.get('level_5_chosen')
        level_6_chosen = request.form.get('level_6_chosen')

        db.execute("SELECT * FROM levels WHERE analysis_id =:analysis_id", {'analysis_id':analysis_id})
        Levels = db.fetchone()

        
        # if first entry
        if Levels is None and level_1 is not None:
            db.execute("INSERT INTO levels ('analysis_id', 'level_1') VALUES (?, ?)", (analysis_id, level_1))
        
        # otherwise update
        if level_1 is not None:
            db.execute("UPDATE levels SET level_1 = ? WHERE analysis_id = ?", (level_1, analysis_id))
        
        # saving commit and changes
        connection.commit()

        # if non-existant yet
        if Levels is None and level_1_chosen is not None:
            db.execute("INSERT INTO levels ('analysis_id', 'level_1_chosen') VALUES (?, ?)", (analysis_id, level_1_chosen))

        # if existant 
        if level_1_chosen is not None:
            db.execute("UPDATE levels SET level_1_chosen = ? WHERE analysis_id = ?", (level_1_chosen, analysis_id))

        connection.commit()

        # if first entry
        if Levels is None and level_2 is not None:
            db.execute("INSERT INTO levels ('analysis_id', 'level_2') VALUES (?, ?)", (analysis_id, level_2))
        
        # otherwise update
        if level_2 is not None:
            db.execute("UPDATE levels SET level_2 = ? WHERE analysis_id = ?", (level_2, analysis_id))
        
        # saving commit and changes
        connection.commit()

        # if non-existant yet
        if Levels is None and level_2_chosen is not None:
            db.execute("INSERT INTO levels ('analysis_id', 'level_2_chosen') VALUES (?, ?)", (analysis_id, level_2_chosen))

        # if existant 
        if level_2_chosen is not None:
            db.execute("UPDATE levels SET level_2_chosen = ? WHERE analysis_id = ?", (level_2_chosen, analysis_id))

        connection.commit()

        # if non-existant yet
        if Levels is None and level_3 is not None:
            db.execute("INSERT INTO levels ('analysis_id', 'level_3') VALUES (?, ?)", (analysis_id, level_3))
        
        # if existant 
        if level_3 is not None:
            db.execute("UPDATE levels SET level_3 = ? WHERE analysis_id = ?", (level_3, analysis_id))
        
        # saving commit and changes
        connection.commit()

        # if non-existant yet
        if Levels is None and level_3_chosen is not None:
            db.execute("INSERT INTO levels ('analysis_id', 'level_3_chosen') VALUES (?,?)", (analysis_id, level_3_chosen))

        # if existant 
        if level_3_chosen is not None:
            db.execute("UPDATE levels SET level_3_chosen = ? WHERE analysis_id = ?", (level_3_chosen, analysis_id))

        connection.commit()

        
        # if non-existant yet
        if Levels is None and level_4 is not None:
            db.execute("INSERT INTO levels ('analysis_id', 'level_4') VALUES (?, ?)", (analysis_id, level_4))
        
        #  if existant 
        if level_4 is not None:
            db.execute("UPDATE levels SET level_4 = ? WHERE analysis_id = ?", (level_4, analysis_id))
        
        # saving commit and changes
        connection.commit()      

        # if non-existant yet
        if Levels is None and level_4_chosen is not None:
            db.execute("INSERT INTO levels ('analysis_id', 'level_4_chosen') VALUES (?, ?)", (analysis_id, level_4_chosen))

        # if existant 
        if level_4_chosen is not None:
            db.execute("UPDATE levels SET level_4_chosen = ? WHERE analysis_id = ?", (level_4_chosen, analysis_id))

        connection.commit()

        # if non-existant yet
        if Levels is None and level_5 is not None:
            db.execute("INSERT INTO levels ('analysis_id', 'level_5') VALUES (?, ?)", (analysis_id, level_5))
        
        # if existant 
        if level_5 is not None:
            db.execute("UPDATE levels SET level_5 = ? WHERE analysis_id = ?", (level_5, analysis_id))
        
        # saving commit and changes
        connection.commit()


        # if non-existant yet
        if Levels is None and level_5_chosen is not None:
            db.execute("INSERT INTO levels ('analysis_id', 'level_5_chosen') VALUES (?, ?)", (analysis_id, level_5_chosen))

        # if existant 
        if level_5_chosen is not None:
            db.execute("UPDATE levels SET level_5_chosen = ? WHERE analysis_id = ?", (level_5_chosen, analysis_id))

        connection.commit()
        
        # if non-existant yet
        if Levels is None and level_6 is not None:
            db.execute("INSERT INTO levels ('analysis_id', 'level_6') VALUES (?, ?)", (analysis_id, level_6))
        
        # if existant 
        if level_6 is not None:
            db.execute("UPDATE levels SET level_6 = ? WHERE analysis_id = ?", (level_6, analysis_id))
        
        # saving commit and changes
        connection.commit()

        # if non-existant yet
        if Levels is None and level_6_chosen is not None:
            db.execute("INSERT INTO levels ('analysis_id', 'level_6_chosen') VALUES (?, ?)", (analysis_id, level_6_chosen))

        # if existant 
        if level_6_chosen is not None:
            db.execute("UPDATE levels SET level_6_chosen = ? WHERE analysis_id = ?", (level_6_chosen, analysis_id))

        connection.commit()

        #----------------- Spaces --------------#
        #retrieving element from the form
        closed = request.form.get('closed')
        invited = request.form.get('invited')
        created = request.form.get('created')

        db.execute("SELECT * FROM spaces WHERE analysis_id=:analysis_id", {'analysis_id':analysis_id})
        Spaces = db.fetchone()
        
        # if non-existant yet
        if Spaces is None and closed is not None:
            db.execute("INSERT INTO spaces ('analysis_id', 'closed') VALUES (?, ?)", (analysis_id, closed))
        
        # if existant 
        if closed is not None:
            db.execute("UPDATE spaces SET closed = ? WHERE analysis_id = ?", (closed, analysis_id))
        
        # saving commit and changes
        connection.commit()

        # if non-existant yet
        if Spaces is None and invited is not None:
            db.execute("INSERT INTO spaces ('analysis_id', 'invited') VALUES (?, ?)", (analysis_id, invited))
        
        # if existant 
        if invited is not None:
            db.execute("UPDATE spaces SET invited = ? WHERE analysis_id = ?", (invited, analysis_id))
        
        # saving commit and changes
        connection.commit()

        # if non-existant yet
        if Spaces is None and created is not None:
            db.execute("INSERT INTO spaces ('analysis_id', 'created') VALUES (?, ?)", (analysis_id, created))
        
        # if existant 
        if created is not None:
            db.execute("UPDATE spaces SET created = ? WHERE analysis_id = ?", (created, analysis_id))
        
        # saving commit and changes
        connection.commit()


        # ------------ selecting element to display once saved ------------#
        db.execute("SELECT * FROM forms WHERE analysis_id =:analysis_id", {'analysis_id':analysis_id})
        Forms = db.fetchone()
        
        db.execute("SELECT * FROM levels WHERE analysis_id =:analysis_id", {'analysis_id':analysis_id})
        Levels = db.fetchone()

        db.execute("SELECT * FROM spaces WHERE analysis_id=:analysis_id", {'analysis_id':analysis_id})
        Spaces = db.fetchone()

        db.execute("SELECT title FROM users WHERE id=:analysis_id", {'analysis_id':analysis_id})
        Title = db.fetchone()

       
        return render_template('analysis.html', Forms = Forms, Levels = Levels, Spaces = Spaces, Title = Title, analysis_id = analysis_id, title_in_database = title_in_database)

#------------------ power cube -------------------#

@app.route('/power_cube', methods = ["GET"])
def powercube():
    if request.method == "GET":
        return render_template('power_cube.html')


#-------------- Export Analysis ------------- #
@app.route('/export', methods = ["GET", "POST"])
def export():
    if request.method == "GET":
        return list_title_export()

    if request.method == "POST":
        
        #retrieving title selected to export
        title = request.form.get('title_in_database')

        #selecting the id of the title selected
        db.execute("SELECT id FROM users WHERE title=:title", {'title':title})
        id_retrived = db.fetchone()
        id = id_retrived[0]

        if id is not None:

            db.execute("SELECT * FROM forms WHERE analysis_id=:id", {'id':id})
            Forms = db.fetchone()

            db.execute("SELECT * FROM levels WHERE analysis_id=:id", {'id':id})
            Levels = db.fetchone()

            db.execute("SELECT * FROM spaces WHERE analysis_id=:id", {'id':id})
            Spaces = db.fetchone()

            #returning element of the analysis to the export template
            return render_template("pdf.html", Forms = Forms, Levels = Levels, Spaces = Spaces, title = title)


#-------------- defining functions --------#
def list_title_export():
    db.execute("SELECT title FROM users")
    Title_export = db.fetchall()
    return render_template('export.html', Title_export = Title_export)

def list_existing_analysis_title():
    db.execute("SELECT title FROM users")
    Title = db.fetchall()
    return render_template('creat_analysis.html', Title = Title)


def get_analysis_id_by_title(x):
    db.execute("SELECT id FROM users WHERE title=?", (x,))
    y = db.fetchone()
    if y is not None:
        return y[0]
    else:
        raise Exception('Did not get any titles id back')
