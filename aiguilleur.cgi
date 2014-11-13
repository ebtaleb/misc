#!/bin/bash

REP_BASE="/users/Etu1/3264851/li219-2013fev/Serveur"
REP_DONNEES="$REP_BASE/Donnees"
REP_PUBLIC="$REP_DONNEES/Public"
REP_SCRIPTS="$REP_BASE/Scripts"
REP_HTML="$REP_BASE/PagesHTML"

FORM_ACTION='<form action="http://localhost/~3264851/cgi-bin/aiguilleur.cgi" method="get">'

export REP_DONNEES
export REP_SCRIPTS
export REP_HTML
export FORM_ACTION

DONNEES_CGI=`echo $QUERY_STRING | tr "&" " "`

echo 'Content-type: text/html'
echo ''

for couple in $DONNEES_CGI
do
    variable=`echo $couple | cut -d '=' -f 1`
    valeur="`echo $couple | cut -d '=' -f 2 | tr "+" " "`"
    export $variable="$valeur"
done

case $CHOICE in
    "Inscription") $REP_SCRIPTS/inscription.sh 2>&1 ;;
    "Connexion") $REP_SCRIPTS/connexion.sh 2>&1 ;;
    "Desinscription") $REP_SCRIPTS/desinscription.sh 2>&1 ;;
    "Desinscrire") $REP_SCRIPTS/desinscrire.sh 2>&1 ;;
    "RetourAccueil") cat $REP_HTML/accueil.html;;

    "AfficherListeMemos") $REP_SCRIPTS/afficheListeMemo.sh 2>&1;;
    "SaisirNouveauMemo") $REP_SCRIPTS/nouveauMemo.sh 2>&1;;

    "EnregistrerMemo") $REP_SCRIPTS/ajoutMemo.sh 2>&1;;
    "AfficherMemo") $REP_SCRIPTS/afficheMemo.sh 2>&1;;
    "GererMemos") $REP_SCRIPTS/gestionMemos.sh 2>&1;;

    "SupprimerMemo") $REP_SCRIPTS/supprimerMemo.sh 2>&1;;
    "ModifierMemo") $REP_SCRIPTS/modification.sh 2>&1;;

    "Valider") $REP_SCRIPTS/ajoutMemo.sh 2>&1;;
    "Modifier") $REP_SCRIPTS/modification.sh 2>&1;;
esac
