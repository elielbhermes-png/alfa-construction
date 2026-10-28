import os

os.makedirs('client/src/lib', exist_ok=True)

i18n = """export const frTranslations = {
  nav: { home: "Accueil", about: "A propos", services: "Services", projects: "Projets", contact: "Contact", admin: "Admin", language: "Langue" },
  home: { heroTitle: "Construisons l'Avenir", heroSubtitle: "ALFA Construction realise des travaux.", heroCta: "Decouvrir nos projets", heroQuotation: "Demander un devis", about: "A propos", aboutText: "Fondee par Ali Safa.", sectorsTitle: "Nos Sectors", sectorBuilding: "Bâtiment & Travaux Publics", sectorTransport: "Transport & Logistique", sectorQuarry: "Exploitation de Carrières", sectorStudy: "Bureau d'Etude", projectsTitle: "Projets", projectsCta: "Tous", strengthsTitle: "Notre Methode", strength1: "Exécution", strength2: "Sécurité", strength3: "Budget", strength4: "Transparence", contactTitle: "Contact", contactCta: "Demander un devis", contactText: "Pour vos projets." },
  about: { title: "A propos", intro: "ALFA Construction est un groupe de construction.", mission: "Mission", missionText: "Raliser des infrastructures.", vision: "Vision", visionText: "Devenir le groupe de reference.", valuesTitle: "Valeurs", value1: "Excellence", value2: "Integres", value3: "Securite", value4: "Responsabilite", value5: "Innovation", value6: "Service" },
  services: { title: "Nos Services", subtitle: "Des services d'ingénierie.", service1: { title: "Bâtiment & Travaux Publics", subtitle: "Travaux civils.", items: ["Construction", "Travaux civils", "Terre-oeuvre", "Beton", "Fondations"] }, service2: { title: "Transport & Logistique", subtitle: "Logistique.", items: ["Envois", "Logistique", "Matériaux", "Equipements", "Flotte"] }, service3: { title: "Exploitation de Carrières", subtitle: "Carrie.", items: ["Carrières", "Matériaux", "Production", "Qualité", "Environnement"] }, service4: { title: "Bureau d'Etude", subtitle: "Etudes techniques.", items: ["Etudes", "Planification", "Expertise", "Conception", "Faisabilite"] } },
  projects: { title: "Nos Realisations", subtitle: "Projets de construction.", filter: "Filtrer", all: "Tous", category1: "Bâtiment", category2: "Travaux Publics", category3: "Transport", category4: "Carrières", category5: "Bureau d'Etude", loadMore: "Charger plus", none: "Aucun projet." },
  project: { gallery: "Galerie", phases: "Phases", readMore: "En savoir plus" },
  contact: { title: "Contactez-Nous", subtitle: "Pour des projets.", name: "Nom", company: "Entreprise", email: "Email", phone: "Telephone", subject: "Sujet", message: "Message", privacy: "Je consens.", submit: "Envoyer", quotationTitle: "Demander un devis", service: "Service", location: "Lieu", description: "Description", budget: "Budget", startDate: "Debut", files: "Documents", error: "Erreur.", success: "Message recu." },
  quotation: { submit: "Demander le devis", processing: "Traitement..." },
  navbar: { menu: "Menu", close: "Fermer" },
  footer: { copyright: "ALFA Construction", legal: "Mentions Légales", privacy: "Confidentialité", faq: "FAQ", contact: "Contact", address: "Congo." },
  legal: { title: "Mentions Légales", description: "Mentions.", editor: "Ali Safa", address: "Congo.", email: "ali@alfa-constructions.com", rcs: "A attribuer." },
  faq: { title: "FAQ", subtitle: "Questions.", q1: "Regions?", a1: "Congo.", q2: "Devis?", a2: "Oui.", q3: "Domaines?", a3: "Construction, Transport, Carrières.", q4: "Contact?", a4: "Formulaire.", q5: "Livraison?", a5: "Oui." },
  admin: { login: "Connexion", email: "Email", password: "Mot de passe", signIn: "Se connecter", signOut: "Deconnexion", dashboard: "Tableau", overview: "Apercu", projects: "Projets", services: "Services", media: "Medias", messages: "Messages", quotes: "Devis", settings: "Parametres", draft: "Brouillon", published: "Publie", unpublished: "Non publie", status: "Statut", title: "Titre", slug: "Slug", description: "Description", actions: "Actions", edit: "Modifier", delete: "Supprimer", cancel: "Annuler", save: "Enregistrer", deleteConfirm: "Supprimer?", created: "Cre", updated: "Mis à jour", contactMessages: "Messages", quotationRequests: "Devis", newMessage: "Nouveau", pending: "En attente", read: "Lu", archived: "Archive", treat: "Traite", addNote: "Note", notePlaceholder: "Note", settingsTitle: "Parametres" },
  shared: { loading: "Chargement...", search: "Rechercher", noneFound: "Aucun.", back: "Retour" },
};

export const enTranslations = { ...frTranslations };
"""

types = """export interface Project { id: string; title: string; slug: string; short_description: string; description: string; location: string|null; category_id: string|null; cover_image_path: string|null; status: string; start_date: string|null; completion_date: string|null; created_at: string; updated_at: string; }
export interface ProjectImage { id: string; project_id: string; storage_path: string; caption: string; alt_text: string; display_order: number; created_at: string; }
export interface Service { id: string; title: string; slug: string; short_description: string; description: string; image_path: string|null; display_order: number; status: string; created_at: string; updated_at: string; }
export interface ContactMessage { id: string; name: string; company: string|null; email: string; phone: string|null; subject: string; message: string; status: string; created_at: string; updated_at: string; }
export interface QuotationRequest { id: string; name: string; company: string|null; email: string; phone: string|null; service_id: string|null; project_location: string; project_description: string; estimated_budget: string|null; desired_start_date: string|null; status: string; created_at: string; updated_at: string; }
"""

validation = """import { z } from 'zod';
export const ContactFormSchema = z.object({ name: z.string().min(2), company: z.string().max(120).optional(), email: z.string().email(), phone: z.string().max(30).optional(), subject: z.string().min(3), message: z.string().min(10).max(5000), privacy: z.boolean().refine((v) => v === true) });
export type ContactFormValues = z.infer<typeof ContactFormSchema>;
export const QuotationFormSchema = z.object({ name: z.string().min(2), company: z.string().max(120).optional(), email: z.string().email(), phone: z.string().min(8), service: z.string().min(1), projectLocation: z.string().min(2), projectDescription: z.string().min(10).max(5000), estimatedBudget: z.string().max(50).optional(), desiredStartDate: z.string().max(50).optional(), files: z.array(z.any()).max(5) });
export type QuotationFormValues = z.infer<typeof QuotationFormSchema>;
"""

with open('client/src/lib/i18n.ts', 'w') as f:
    f.write(i18n)
with open('client/src/lib/types.ts', 'w') as f:
    f.write(types)
with open('client/src/lib/validation.ts', 'w') as f:
    f.write(validation)

print("Lib files written successfully")
