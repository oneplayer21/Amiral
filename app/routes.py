from flask import render_template, request, redirect, url_for
from app import db
from app.models import ReferentielFonds, ReferentielInstruments, Positions, ContactSupport

def register_routes(app):
    @app.route('/fonds')
    def fonds():
        fonds = ReferentielFonds.query.all()
        return render_template('fonds.html', fonds=fonds)

    @app.route('/instruments')
    def instruments():
        instruments = ReferentielInstruments.query.all()
        return render_template('instruments.html', instruments=instruments)

    @app.route('/positions/<int:fond_id>')
    def positions(fond_id):
        fond = ReferentielFonds.query.get_or_404(fond_id)
        positions = Positions.query.filter_by(instrument_id=fond_id).all()
        total_poids = sum(position.poids for position in positions)
        return render_template('positions.html', fond=fond, positions=positions, total_poids=total_poids)

    @app.route('/menu')
    def menu():
        return render_template('menu.html')
    
    @app.route('/recherche', methods=['GET'])
    def recherche():
        query = request.args.get('query', '')
        fonds = ReferentielFonds.query.filter(ReferentielFonds.nom.ilike(f'%{query}%')).all()
        instruments = ReferentielInstruments.query.filter(ReferentielInstruments.nom.ilike(f'%{query}%')).all()
        positions = Positions.query.join(ReferentielInstruments).filter(ReferentielInstruments.nom.ilike(f'%{query}%')).all()

        return render_template('recherche.html', fonds=fonds, instruments=instruments, positions=positions, query=query)
    
    @app.route('/contact', methods=['GET', 'POST'])
    def contact():
        if request.method == 'POST':
            nom = request.form['nom']
            email = request.form['email']
            message = request.form['message']
            
            contact_message = ContactSupport(nom=nom, email=email, message=message)
            db.session.add(contact_message)
            db.session.commit()
            
            return redirect(url_for('contact_success'))

        return render_template('contact.html')

    @app.route('/contact-success')
    def contact_success():
        return render_template('contact_success.html')