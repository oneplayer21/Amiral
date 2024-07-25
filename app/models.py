from app import db

class ReferentielFonds(db.Model):
    __tablename__ = 'referentielfonds'  # Nom de la table dans la base de données
    
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(100), nullable=False)
    
    def __repr__(self):
        return f'<ReferentielFonds {self.nom}>'

class ReferentielInstruments(db.Model):
    __tablename__ = 'referentielinstruments'  # Nom de la table dans la base de données
    
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(100), nullable=False)
    
    def __repr__(self):
        return f'<ReferentielInstruments {self.nom}>'

class Positions(db.Model):
    __tablename__ = 'positions'
    
    id = db.Column(db.Integer, primary_key=True)
    instrument_id = db.Column(db.Integer, db.ForeignKey('referentielinstruments.id'), nullable=False)
    poids = db.Column(db.Float, nullable=False)
    
    instrument = db.relationship('ReferentielInstruments', backref='positions')
    
    def __repr__(self):
        return f'<Positions {self.id} - {self.instrument.nom}>'

class Performances(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fond_id = db.Column(db.Integer, db.ForeignKey('referentielfonds.id'))
    date = db.Column(db.Date, nullable=False)
    valeur = db.Column(db.Float, nullable=False)

class ContactSupport(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    message = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<ContactSupport {self.id} - {self.nom}>'

