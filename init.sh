USER="root"
DATABASE="portefeuille_db"
SQL_SCRIPT="init.sql"

# Exécuter le script SQL
sudo systemctl start mysql
mysql -u $USER -p < $SQL_SCRIPT