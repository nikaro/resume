#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = "Nicolas Karolak"
SITENAME = "Nicolas Karolak"
SITEURL = ""
SITEDESCRIPTION = ""

PATH = "content"

TIMEZONE = "Europe/Paris"

DEFAULT_LANG = "fr"

FEED_ALL_ATOM = None

RELATIVE_URLS = True

THEME = "resume"
CSS_FILE = "main-6.css"

# Profile information
NAME = "Nicolas Karolak"
TAGLINE = "Ingénieur Systèmes Linux"
PIC = "../../images/photo.jpg"

# sidebar links
EMAIL = "nicolas@karolak.fr"
PHONE = "+33651422138"
WEBSITE = "blog.karolak.fr"
LINKEDIN = "nicolas-karolak"
GITHUB = "nikaro"
SOURCEHUT = "nka"
TWITTER = None

DOWNLOAD_PDF = "images/cv-nicolas-karolak.pdf"

CAREER_SUMMARY = "Passionné d'informatique. Orienté Linux et automatisation. Amateur de logiciels libres et open source. Contributeur occasionnel. Télétravailleur. J'ai besoin que mon travail ait du sens et une utilité sociale."

SKILLS = [
    {
        "title": "Linux : Debian, CentOS, ArchLinux",
        "level": "90",
    },
    {
        "title": "Scripting : Bash, Python, PHP, Go",
        "level": "80",
    },
    {
        "title": "IaC : Ansible, Git, Gitlab CI, Terraform",
        "level": "80",
    },
    {
        "title": "Web : NGINX, HAProxy, Apache2",
        "level": "70",
    },
    {
        "title": "Virtualisation : Docker, KVM, LXC, LXD",
        "level": "60",
    },
    {
        "title": "Cloud : Scaleway, OVH, AWS",
        "level": "50",
    },
    {
        "title": "Base de données : PostgreSQL, MySQL, MariaDB, Galera Cluster, Redis",
        "level": "50",
    },
    {
        "title": "Réseaux : Pare-feu, Routage, VLAN, OpenVPN, WireGuard",
        "level": "50",
    },
]

PROJECTS = [
    {
        "title": "Contributions",
        "tagline": "Plusieurs soumissions dans quelques projets Open Source, tels que Ansible, Pyinfra, Rss2email, Rss-Bridge, et de nombreux rapports de bogues.",
    },
    {
        "title": "Devc",
        "link": "https://sr.ht/~nka/devc",
        "tagline": "Outil de gestion de devcontainer en CLI, écrit en Go. Un devcontainer permet d'isoler les outils de l'environnement de développement dans un conteneur Docker en lien avec l'éditeur de code.",
    },
    {
        "title": "Resume-PyCLI",
        "link": "https://sr.ht/~nka/resume-pycli",
        "tagline": "Générateur de CV au formats HTML et PDF, écrit en Python, avec le moteur de template Jinja. Utilise le format JSONResume, et est inspiré de l'outil resume-cli.",
    },
    {
        "title": "Infra",
        "link": "https://git.sr.ht/~nka/infra",
        "tagline": "Dépôt contenant les scripts de déploiement et d'orchestration de mon infrastructure personnelle (serveur de messagerie, web, Nextcloud, etc.), en Ansible et Terraform.",
    },
]

LANGUAGES = [
    {
        "name": "Français",
        "description": "Langue maternelle",
    },
    {
        "name": "Anglais écrit",
        "description": "Autonome (C1)",
    },
    {
        "name": "Anglais oral",
        "description": "Intermédiaire (B1)",
    },
]

INTERESTS = [
    "Informatique",
    "Judo",
    "Lecture",
    "Cuisine",
    "Cinéma",
    "Restaurant",
    "Randonnée",
    "Cueillette de champignons",
    "Moto",
]

EXPERIENCES = [
    {
        "job_title": "Administrateur Systèmes Linux",
        "time": "Octobre 2020 - Aujourd'hui",
        "company": "BoondManager, Télétravail",
        "details": [
            "Mise en place cluster GlusterFS",
            "Écriture de tests de charge avec Locust",
            "Scripting Bash et Ansible",
        ],
    },
    {
        "job_title": "Enseignant vacataire en Licence Pro",
        "time": "Oct. 2012 - Aujourd'hui",
        "company": "IUT de Sénart, Lieusaint",
        "details": [
            "Scripting (Python, Perl)",
            "Chiffrement et certificats",
            "VPN",
        ],
    },
    {
        "job_title": "Ingénieur Systèmes Linux",
        "time": "Mai 2020 - Octobre 2020",
        "company": "Université Gustave Eiffel, Champs-sur-Marne",
        "details": [
            "Déploiement de services (WireGuard, pfSense, etc.)",
            "Écriture d'un démon de logging pour WireGuard",
        ],
    },
    {
        "job_title": "Ingénieur Systèmes Linux",
        "time": "Sep. 2017 - Avril 2020",
        "company": "UbiCast, Ivry-sur-Seine, Télétravail",
        "details": [
            "Déploiement d'infrastructure avec Terraform, Packer et Ansible",
            "Portage des scripts de déploiement (Python/Bash) vers Ansible",
            "Mise en haute-disponibilité du produit (cluster PostgreSQL, HAProxy, etc.)",
        ],
    },
    {
        "job_title": "Responsable informatique",
        "time": "Sep. 2016 - Août 2017",
        "company": "Lycée Technique Privé Saint-Nicolas, Paris",
        "details": [
            "Développement d'un gestionnaire de comptes utilisateurs (Django)",
            "Migration serveur de messagerie interne (Postfix, Dovecot)",
            "Mise en place Nextcloud pour les professeurs et étudiants",
        ],
    },
    {
        "job_title": "Administrateur Systèmes et Réseaux",
        "time": "Sep. 2015 - Sep. 2016",
        "company": "IUT de Sénart, Lieusaint",
        "details": [
            "Administration système (Debian/Ubuntu)",
            "Développement (PHP/Bash/Python)",
            "Exploitation de parc (Ubuntu/Windows)",
        ],
    },
    {
        "job_title": "Administrateur Systèmes et Réseaux",
        "time": "Août 2011 - Déc. 2014",
        "company": "Lycée Technique Privé Saint-Nicolas, Paris",
        "details": [
            "Administration serveurs GNU/Linux et Windows",
            "Conception nouvelle infrastructure : Virtualisation, VPN, Active Directory, etc.",
        ],
    },
    {
        "job_title": "Informaticien HelpDesk",
        "time": "Août 2009 - Août 2011",
        "company": "Châteaud'eau, La Courneuve",
        "details": [
            "Gestion, maintenance, installation (Serveurs & PC)",
            "Participation à l'implémentation de projets d'infrastructure",
            "Pilotage de la migration de l'ancien logiciel client ERP vers le nouveau",
        ],
    },
]

EDUCATIONS = [
    {
        "degree": "Licence Pro Administration Systèmes et Réseaux",
        "meta": "IUT de Sénart, Lieusaint",
        "time": "Oct. 2011 - Juin 2012",
    },
    {
        "degree": "BTS Informatique de Gestion",
        "meta": "Institut Medicis Alternance, Paris",
        "time": "Sep. 2009 - Mai 2011",
    },
    {
        "degree": "Bac Pro Micro-informatique et Réseaux",
        "meta": "Lycée Jacques Prevert, Combs-la-Ville",
        "time": "Sep. 2007 - Juin 2009",
    },
]
