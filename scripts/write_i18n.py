import os

os.makedirs('client/src/lib', exist_ok=True)
os.makedirs('supabase/migrations', exist_ok=True)

# i18n
i18n = """export const frTranslations = {
  nav: { home: "Accueil", about: "A propos", services: "Services", projects: "Projets", contact: "Contact", admin: "Admin", language: "Langue" },
  home: {
    heroTitle: "Construisons l'Avenir",
    heroSubtitle: "ALFA Construction realise des travaux de Bâtiment & Travaux Publics, Transport & Logistique, Exploitation de Carrières et Bureau d'Etude en Republique du Congo.",
    heroCta: "Decouvrir nos projets",
    heroQuotation: "Demander un devis",
    about: "A propos",
    aboutText: "Fondee par Ali Safa, ALFA Construction opere a l'intersection de l'ingenierie et de l'execution.",
    sectorsTitle: "Nos Sectors d'Activite",
    sectorBuilding: "Bâtiment & Travaux Publics",
    sectorTransport: "Transport & Logistique",
    sectorQuarry: "Exploitation de Carrières",
    sectorStudy: "Bureau d'Etude",
    projectsTitle: "Projets Meles",
    projectsCta: "Tous les projets",
    strengthsTitle: "Notre Methode de Travail",
    strength1: "Exécution d'ingénierie",
    strength2: "Normes de sécurité rigoureux",
    strength3: "Livraison sur time et budget",
    strength4: "Communication transparente",
    contactTitle: "Construisons Ensemble",
    contactCta: "Demander un devis",
    contactText: "Pour vos demandes de projet, devis ou partenariats."
  },
  about: {
    title: "A propos de ALFA Construction",
    intro: "ALFA Construction est un groupe de construction de reference en Republique du Congo.",
    mission: "Mission",
    missionText: "Realiser des infrastructures de la plus haute qualite par l'excellence technique.",
    vision: "Vision",
    visionText: "Devenir le groupe de construction de reference de la Republique du Congo.",
    valuesTitle: "Valeurs Fondamentales",
    value1: "Excellence", value2: "Integres", value3: "Securite", value4: "Responsabilite", value5: "Innovation", value6: "Service"
  },
  services: {
    title: "Nos Services",
    subtitle: "Des services d'ingenierie et de construction completes.",
    service1: { title: "Bâtiment & Travaux Publics", subtitle: "Travaux civils et batiment.", items: ["Construction", "Travaux civils", "Terre-oeuvre", "Beton", "Fondations"] },
    service2: { title: "Transport & Logistique", subtitle: "Logistique de materiaux.", items: ["Envois", "Logistique", "Materiaux", "Equipements", "Flotte"] },
    service3: { title: "Exploitation de Carrières", subtitle: "Carrie et approvisionnement.", items: ["Carrieres", "Materiaux", "Production", "Qualité", "Environnement"] },
    service4: { title: "Bureau d'Etude", subtitle: "Etudes techniques.", items: ["Etudes", "Planification", "Expertise", "Conception", "Faisabilite"] }
  },
  projects: {
    title: "Nos Realisations",
    subtitle: "Projets de construction et d'infrastructure.",
    filter: "Filtrer par categorie", all: "Tous", category1: "Bâtiment", category2: "Travaux Publics", category3: "Transport", category4: "Carrieres", category5: "Bureau d'Etude", loadMore: "Charger plus", none: "Aucun projet."
  },
  project: { gallery: "Galerie", phases: "Phases", readMore: "En savoir plus", viewGallery: "Voir la galerie" },
  contact: {
    title: "Contactez-Nous", subtitle: "Contactez-nous pour des projets, devis ou partenariats.",
    name: "Nom complet", company: "Entreprise", email: "Email", phone: "Téléphone", subject: "Sujet", message: "Message",
    privacy: "Je consens.", submit: "Envoyer", quotationTitle: "Demander un devis", service: "Service", location: "Lieu", description: "Description", budget: "Budget", startDate: "Debut souhaité", files: "Documents",
    error: "Erreur.", success: "Message recu.", required: "Obligatoire.", invalidEmail: "Email invalide.", minLength: "Chars min."
  },
  quotation: { submit: "Demander le devis", processing: "Traitement..." },
  navbar: { menu: "Menu", close: "Fermer" },
  footer: { copyright: "ALFA Construction - Republique du Congo", legal: "Mentions Légales", privacy: "Confidentialité", faq: "FAQ", contact: "Contact", address: "Avenue Docteur Cardorelle, Songolo, Congo." },
  legal: { title: "Mentions Légales", description: "Mentions légales.", editor: "Ali Safa, Président Directeur Général", address: "Avenue Docteur Cardorelle, Songolo, Congo.", email: "ali-safa@alfa-constructions.com", rcs: "A attribuer." },
  faq: {
    title: "FAQ", subtitle: "Questions fréquentes.",
    q1: "Quelles régions servent-vous?", a1: "Principalement en Republique du Congo.",
    q2: "Proposez-vous des devis?", a2: "Oui. Contactez notre équipe.",
    q3: "Quels sont vos domaines?", a3: "Bâtiment, Transport, Carrières, Bureau d'Etude.",
    q4: "Comment contacter l'entreprise?", a4: "Formulaire de contact ou email.",
    q5: "Gérez-vous la livraison?", a5: "Oui, de la conception à la construction."
  },
  admin: {
    login: "Connexion", email: "Email", password: "Mot de passe", signIn: "Se connecter", signOut: "Deconnexion",
    dashboard: "Tableau de bord", overview: "Aperçu", projects: "Projets", services: "Services", media: "Média", messages: "Messages", quotes: "Devis", settings: "Parametres",
    draft: "Brouillon", published: "Publie", unpublished: "Non publie", status: "Statut", title: "Titre", slug: "Slug", description: "Description", actions: "Actions",
    edit: "Modifier", delete: "Supprimer", cancel: "Annuler", save: "Enregistrer", deleteConfirm: "Supprimer?",
    created: "Cre", updated: "Mis à jour",
    contactMessages: "Messages", quotationRequests: "Demandes", newMessage: "Nouveau", pending: "En attente", read: "Lu", archived: "Archivé", treat: "Traité",
    addNote: "Note interne", notePlaceholder: "Note...",
    settingsTitle: "Parametres", companyName: "Nom", logo: "Logo", contactPerson: "Contact", jobTitle: "Poste", emails: "Emails", phone: "Téléphone", address: "Adresse", website: "Site", homepage: "Accueil", footer: "Pied de page"
  },
  shared: { loading: "Chargement...", search: "Rechercher", noneFound: "Aucun résultat.", back: "Retour" }
};

export const enTranslations = { ...frTranslations };
"""

with open('client/src/lib/i18n.ts', 'w') as f:
    f.write(i18n)
print("i18n written")
