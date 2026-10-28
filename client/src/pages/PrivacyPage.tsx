import { useI18n } from '@/contexts/I18nContext';

export function PrivacyPage() {
  const { t } = useI18n();
  return (
    <div className="py-16 sm:py-24 bg-navy-900/50">
      <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
        <h1 className="text-3xl sm:text-4xl font-extrabold text-white mb-8">{t('legal.title')}</h1>
        <div className="space-y-6 text-steel-300 leading-relaxed">
          <p>ALFA Construction est un groupe de construction basé en République du Congo.</p>
          <p>Pour toute question relative à cette politique de confidentialité, contactez-nous à ali-safa@alfa-constructions.com.</p>
          <p><strong>Données collectées :</strong> Nom, email, téléphone, message, informations de devis.</p>
          <p><strong>Finalité :</strong> Traitement des demandes de devis et de contact.</p>
          <p><strong>Partage :</strong> Les données ne sont pas partagées avec des tiers sans autorisation.</p>
        </div>
      </div>
    </div>
  );
}
