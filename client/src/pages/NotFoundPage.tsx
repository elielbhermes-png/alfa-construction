import { Link } from 'react-router-dom';
import { useI18n } from '@/contexts/I18nContext';

export function NotFoundPage() {
  const { t } = useI18n();
  return (
    <div className="min-h-screen flex items-center justify-center bg-navy-900">
      <div className="text-center">
        <h1 className="text-6xl font-extrabold text-white">404</h1>
        <p className="text-steel-300 mt-4 text-xl">{t('shared.noneFound')}</p>
        <Link to="/"><button className="mt-6 px-6 py-3 rounded-lg bg-accent text-navy-900 font-semibold hover:bg-accent/90 transition-colors">Retour à l'accueil</button></Link>
      </div>
    </div>
  );
}
