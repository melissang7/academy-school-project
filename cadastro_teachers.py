from flask.views import MethodView
from flask import request, render_template, redirect
from src.database import mysql

class IndexControl(MethodView):
    def get(self):
         with mysql.cursor() as cur:
            cur.execute("SELECT * FROM teachers")
            data = cur.fetchall()
         return render_template('public/index.html', data = data)


    def post(self): 
        full_n_teacher = request.form['full_n_teacher']
        register_teacher = request.form['register_teacher']
        hist_vh_teacher = request.form['hist_vh_teacher']
        tittle_teacher = request.form['tittle_teacher']
        reg_w_teacher = request.form['reg_w_teacher']
        hiring_d_teacher = request.form['hiring_d_teacher']
        close_d_teacher = request.form['close_d_teacher']
        status_teacher = request.form['status_teacher']

        with mysql.cursor() as cur:
            cur.execute("INSERT INTO teachers(full_n_teacher, reg_teacher, hist_vh_teacher, tittle_teacher, regime_w_teacher, d_hiring_teacher, d_close_teacher, status_teacher) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", (full_n_teacher, register_teacher, hist_vh_teacher, tittle_teacher, reg_w_teacher, hiring_d_teacher, close_d_teacher, status_teacher))
            cur.connection.commit()
            return redirect('/')

class DeleteTeacher(MethodView):
    def post(self, code):
       with mysql.cursor() as cur:
            cur.execute("DELETE FROM teachers WHERE code = %s ", (code, ))
            cur.connection.commit()
            return redirect('/')

class UpdateTeacher(MethodView):
    def post(self, code):
            return "rs"

            
class NotFoundControl(MethodView):
    def get(self, error):
        return f"PAGINA NAO ENCONTRADA{error}"