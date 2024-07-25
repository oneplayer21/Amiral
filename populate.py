from app import create_app, db
from app.models import ReferentielFonds, ReferentielInstruments, Positions

app = create_app()

with app.app_context():
    # Vider les tables existantes (si nécessaire)
    db.drop_all()
    db.create_all()

    # Ajouter des données à la table ReferentielFonds
    fonds1 = ReferentielFonds(id=1, nom='Fonds Alpha')
    fonds2 = ReferentielFonds(id=2, nom='Fonds Beta')
    fonds3 = ReferentielFonds(id=3, nom='Fonds Gamma')

    db.session.add_all([fonds1, fonds2, fonds3])

    # Ajouter des données à la table ReferentielInstruments
    instrument1 = ReferentielInstruments(id=1, nom='Instrument A')
    instrument2 = ReferentielInstruments(id=2, nom='Instrument B')
    instrument3 = ReferentielInstruments(id=3, nom='Instrument C')

    db.session.add_all([instrument1, instrument2, instrument3])

    # Ajouter des données à la table Positions
    position1 = Positions(id=1, instrument_id=1, poids=30.0)
    position2 = Positions(id=2, instrument_id=2, poids=50.0)
    position3 = Positions(id=3, instrument_id=3, poids=20.0)

    db.session.add_all([position1, position2, position3])

    # Commit les transactions
    db.session.commit()

print("Base de données peuplée avec succès.")
