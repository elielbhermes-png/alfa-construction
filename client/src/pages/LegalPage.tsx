import { useI18n } from '@/contexts/I18nContext';
import { NavLink } from 'react-router-dom';

export function LegalPage() {
  const { t } = useI18n();
  return (
    <div className="py-16 sm:py-24 bg-navy-900/50">
      <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
        <h1 className="text-3xl sm:text-4xl font-extrabold text-white mb-8">{t('legal.title')}</h1>
        <div className="space-y-6 text-steel-300 leading-relaxed">
          <p><strong>Éditeur :</strong> ALFA Construction</p>
          <p><strong>Directeur de la publication :</strong> Ali Safa</p>
          <p><strong>Adresse :</strong> Avenue Docteur Cardorelle, Songolo, Congo</p>
          <p><strong>Email :</strong> ali-safa@alfa-constructions.com</p>
          <p>Ce site est un exercice de texte. Les informations publiées sont fournies à titre indicatif.</p>
        </div>
      </div>
    </div>
  );
}
