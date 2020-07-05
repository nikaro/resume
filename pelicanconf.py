#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Nicolas Karolak'
SITENAME = 'Nicolas Karolak'
SITEURL = ''
SITEDESCRIPTION = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'fr'

FEED_ALL_ATOM = None

RELATIVE_URLS = True

THEME = 'resume'
CSS_FILE = 'main-6.css'

# Profile information
NAME = 'Nicolas Karolak'
TAGLINE = 'Ingénieur Systèmes Linux'
PIC = '../../images/photo.jpg'

# sidebar links
EMAIL = 'nicolas@karolak.fr'
PHONE = '+33651422138'
WEBSITE = 'blog.karolak.fr'
LINKEDIN = 'nicolas-karolak'
GITHUB = 'nikaro'
SOURCEHUT = 'nka'
TWITTER = None

CAREER_SUMMARY = "Passionné d'informatique. Orienté Linux et automatisation. Amateur de logiciels libres et open source. Contributeur occasionnel. Télétravailleur. J'ai besoin que mon travail ait du sens et une utilité sociale."

SKILLS = [
    {
        'title': 'Linux : Debian, CentOS',
        'level': '80',
    },
    {
        'title': 'IaC : Ansible, Terraform, Packer',
        'level': '90',
    },
    {
        'title': 'Web : NGINX, HAProxy, Apache2',
        'level': '80',
    },
    {
        'title': 'Virtualisation : LXD/LXC, KVM, Docker',
        'level': '70',
    },
    {
        'title': 'Cloud : AWS, GCP, Scaleway, OpenStack',
        'level': '50',
    },
    {
        'title': 'Scripting : Bash, Python, Golang',
        'level': '80',
    },
    {
        'title': 'Réseaux : Pare-feu, Routage, VLAN',
        'level': '60',
    },
]

PROJECTS = [
    {
        'title': 'Contributions',
        'tagline': 'Plusieurs soumissions dans quelques projets Open Source, tels que Ansible, Pyinfra, Rss2email, Rss-Bridge, et de nombreux rapports de bogues.',
    },
    {
        'title': 'Devc',
        'link': 'https://git.sr.ht/~nka/devc',
        'tagline': "Outil de gestion de devcontainer en ligne de commande, écrit en Go. Un devcontainer, concept issus de VSCode, permet d'isoler les outils de l'environnement de développement dans un conteneur Docker en lien avec l'éditeur de code.",
    },
    {
        'title': 'Infra',
        'link': 'https://git.sr.ht/~nka/infra',
        'tagline': "Dépôt contenant les scripts de déploiement et d'orchestration de mon infrastructure personnelle (serveur de messagerie, web, Nextcloud, etc.), en Ansible et Terraform.",
    },
]

LANGUAGES = [
    {
        'name': 'Français',
        'description': 'Maternel',
    },
    {
        'name': 'Anglais',
        'description': 'Professionnel',
    },
]

INTERESTS = [
    'Judo',
    'Cinéma',
    'Restaurant',
]

EXPERIENCES = [
    {
        'job_title': 'Ingénieur Systèmes Linux',
        'time': "Mai 2020 - Aujourd'hui",
        'company': 'Université Gustave Eiffel, Champs-sur-Marne',
        'details': '',
    },
    {
        'job_title': 'Enseignant vacataire en Licence Pro',
        'time': "Oct. 2012 - Aujourd'hui",
        'company': 'IUT de Sénart, Lieusaint',
        'details': 'Intervention sur les modules : Scripting (Python, Perl), Chiffrement et certificats, VPN.',
    },
    {
        'job_title': 'Ingénieur Systèmes Linux',
        'time': 'Sep. 2017 - Avril 2020',
        'company': 'UbiCast, Ivry-sur-Seine',
        'details': "Déploiement d'infrastructure Cloud/On-premise avec Terraform, Packer et Ansible. Portage des scripts de déploiement (Python/Bash) vers Ansible. Mise en haute-disponibilité du produit (cluster PostgreSQL, HAProxy, etc.).",
    },
    {
        'job_title': 'Responsable informatique',
        'time': 'Sep. 2016 - Août 2017',
        'company': 'Lycée Technique Privé Saint-Nicolas, Paris',
        'details': "Développement d'une solution gestion des mots de passe (Python, Django). Migration serveur de messagerie interne (Postfix, Dovecot). Mise en place Nextcloud pour les professeurs et étudiants.",
    },
    {
        'job_title': 'Administrateur Systèmes et Réseaux',
        'time': 'Sep. 2015 - Sep. 2016',
        'company': 'IUT de Sénart, Lieusaint',
        'details': 'Administration système (Debian/Ubuntu). Développement (PHP/Bash/Python). Exploitation de parc (Ubuntu/Windows).',
    },
    {
        'job_title': 'Développeur Web',
        'time': 'Déc. 2014 - Sep. 2015',
        'company': 'Indépendant',
        'details': 'Développement de sites internet en PHP et Python/Django.',
    },
    {
        'job_title': 'Administrateur Systèmes et Réseaux',
        'time': 'Août 2011 - Déc. 2014',
        'company': 'Lycée Technique Privé Saint-Nicolas, Paris',
        'details': 'Administration serveurs GNU/Linux et Windows. Conception & mise en œuvre nouvelle infrastructure multi-site : Virtualisation, VPN, Active Directory, etc. Monitoring : Nagios. Outil de gestion de configuration : Rudder. Scripting : Batch, VBS, Bash, Perl.',
    },
    {
        'job_title': 'Informaticien HelpDesk',
        'time': 'Août 2009 - Août 2011',
        'company': "Châteaud'eau, La Courneuve",
        'details': "Gestion, maintenance, installation (Serveurs & PC). Participation à l'implémentation de projets d'infrastructure. Pilotage de la migration de l'ancien logiciel client ERP vers le nouveau.",
    },
]

EDUCATIONS = [
    {
        'degree': 'Licence Pro Administration Systèmes et Réseaux',
        'meta': 'IUT de Sénart, Lieusaint',
        'time': 'Oct. 2011 - Juin 2012',
    },
    {
        'degree': 'BTS Informatique de Gestion',
        'meta': 'Institut Medicis Alternance, Paris',
        'time': 'Sep. 2009 - Mai 2011',
    },
    {
        'degree': 'Bac Pro Micro-informatique et Réseaux',
        'meta': 'Lycée Jacques Prevert, Combs-la-Ville',
        'time': 'Sep. 2007 - Juin 2009',
    },
]
