from flask import Flask, url_for, render_template, redirect, escape, request, json
from flask_mysqldb import MySQL
import logging

app = Flask(__name__)
app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "admin"
app.config["MYSQL_PASSWORD"] = ""
app.config["MYSQL_DB"] = "experiment"
mysql = MySQL(app)

handler = logging.FileHandler("app.log")  # errors logged to this file
handler.setLevel(logging.ERROR) # only log errors and above
app.logger.addHandler(handler)  # attach the handler to the app's logger

@app.route("/")
def main():
    return render_template("index.html")

@app.route("/info")
def info():
    return render_template("info.html")

@app.route("/next", methods=["GET"])
def next():
    return redirect(url_for('intro'))

@app.route("/intro")
def intro():
    return render_template("intro.html")

@app.route("/exp1")
def exp1():
    return render_template("exp1.html")

@app.route("/exp2")
def exp2():
    return render_template("exp2.html")

@app.route("/save", methods=["POST"])
def save():
    cur = mysql.connection.cursor()
    json_dict = request.get_json()
    repeatexp = (json_dict["RepeatExp"])
    age = (json_dict["Age"])
    gender = (json_dict["Gender"])
    edlevel = (json_dict["EducationLevel"])
    edfield = (json_dict["EducationField"])
    colourblind = (json_dict["ColourBlind"])
    redrange = (json_dict["RedRange"])
    greenrange = (json_dict["GreenRange"])
    email = (json_dict["Email"])
    stimuli = str(json_dict["StimuliAssigned"])
    YSelectedTotal = int(json_dict["YSelectedTotal"])
    YRedTop = int(json_dict["YRedTop"])
    YRedBtm = int(json_dict["YRedBtm"])
    YGreenTop = int(json_dict["YGreenTop"])
    YGreenBtm = int(json_dict["YGreenBtm"])
    YNew = int(json_dict["YNew"])
    NSelectedTotal = int(json_dict["NSelectedTotal"])
    NRedTop = int(json_dict["NRedTop"])
    NRedBtm = int(json_dict["NRedBtm"])
    NGreenTop = int(json_dict["NGreenTop"])
    NGreenBtm = int(json_dict["NGreenBtm"])
    NNew = int(json_dict["NNew"])
    AttendedRed = float(json_dict["AttendedRed"])
    AttendedGreen = float(json_dict["AttendedGreen"])
    AttendedNew = float(json_dict["AttendedNew"])
    TimeTaken = int(json_dict["TimeTaken"])
    fields = (repeatexp, age, gender, edlevel, edfield, colourblind, redrange, greenrange, email, stimuli, YSelectedTotal, YRedTop, YRedBtm, YGreenTop, YGreenBtm, YNew, NSelectedTotal, NRedTop, NRedBtm, NGreenTop, NGreenBtm, NNew, AttendedRed, AttendedGreen, AttendedNew, TimeTaken)
    sql = """INSERT INTO data_table (RepeatExp, Age, Gender, EducationLevel, EducationField, ColourBlind, RedRange, GreenRange, Email, AttendedColour, YSelectedTotal, YRedTop, YRedBtm, YGreenTop, YGreenBtm, YNew, NSelectedTotal, NRedTop, NRedBtm, NGreenTop, NGreenBtm, NNew, AttendedRed, AttendedGreen, AttendedNew, TimeTaken) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"""
    cur.execute(sql, fields)
    mysql.connection.commit()
    return None

@app.route("/end")
def end():
    return render_template("end.html")

@app.errorhandler(404)
def page_not_found(error):
    return 'This page does not exist', 404
    
if __name__ == "__main__":
        app.run()

