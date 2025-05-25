from flask import Flask, request, render_template, redirect, url_for
from models import db, Equipment
from constants import CATEGORIES

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()

@app.route('/')
def index():
    q = request.args.get('q', '').strip()
    cat = request.args.get('category', '')

    query = Equipment.query

    if q:
        query = query.filter(Equipment.name.ilike(f'%{q}%'))

    if cat and cat in CATEGORIES:
        query = query.filter_by(category=cat)

    items = query.order_by(Equipment.id).all()
    return render_template('index.html', items=items, q=q, cat=cat, categories=CATEGORIES)

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        eq = Equipment(
            name=request.form['name'],
            inventory_number=request.form['inv_num'],
            category=request.form['category'],
            status=request.form['status'],
            purchase_date=request.form['purchase_date'],
            location=request.form['location']
        )
        db.session.add(eq)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add.html', categories=CATEGORIES)

@app.route('/delete/<int:id>')
def delete(id):
    Equipment.query.filter_by(id=id).delete()
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
