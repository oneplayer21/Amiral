Pour initaliser le projet:

  .S'assurer d'avoir mysql sur son ordinateur

  .installer les dépedances: pip install -r requirements.txt

  .Initaliser la database mysql: ./init.sh (mot de passe à utiliser: celui de l'utilisateur root)

  .Remplir les tables: python3 populate.py

  .Lancer le projet: python3 run.py

  .Une fois que tout est terminé: sudo systemctl stop mysql
