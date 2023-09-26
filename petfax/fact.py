from flask import ( Blueprint, render_template, request, redirect ) 
from . import modles

bp = Blueprint('fact', __name__, url_prefix="/facts")

@bp.route('/new')
def new(): 
    return render_template('facts/new.html')

@bp.route('/', methods = ['GET', 'POST'])
def index():
    if request.method == 'POST':     
        submitter = request.form['submitter']
        fact = request.form['fact']

        new_fact = modles.Fact(submitter=submitter, fact=fact)
        modles.db.session.add(new_fact)
        modles.db.session.commit()

        return redirect('/facts')
    
    results = modles.Fact.query.all()
    
    return render_template('facts/index.html', facts = results)