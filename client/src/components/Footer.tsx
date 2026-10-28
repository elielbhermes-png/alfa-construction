import { NavLink } from 'react-router-dom';
import { useI18n } from '@/contexts/I18nContext';

export function Footer() {
  const { t } = useI18n();
  return (
    <footer className="bg-navy-900 border-t border-steel-700/50 mt-auto">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-10">
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-8">
          <div>
            <h4 className="text-sm font-bold text-white mb-3">Navigation</h4>
            <ul className="space-y-2 text-sm text-steel-300">
              <li><NavLink to="/" className="hover:text-accent transition-colors">Accueil</NavLink></li>
              <li><NavLink to="/a-propos" className="hover:text-accent transition-colors">A propos</NavLink></li>
              <li><NavLink to="/nos-services" className="hover:text-accent transition-colors">Services</NavLink></li>
              <li><NavLink to="/nos-realisations" className="hover:text-accent transition-colors">Projets</NavLink></li>
            </ul>
          </div>
          <div>
            <h4 className="text-sm font-bold text-white mb-3">Contact</h4>
            <ul className="space-y-2 text-sm text-steel-300">
              <li>ali-safa@alfa-constructions.com</li>
              <li>+242 06 822 22 20</li>
              <li>Avenue Docteur Cardorelle, Songolo, Congo</li>
            </ul>
          </div>
          <div>
            <h4 className="text-sm font-bold text-white mb-3">Liens</h4>
            <ul className="space-y-2 text-sm text-steel-300">
              <li><NavLink to="/politique-de-confidentialite" className="hover:text-accent transition-colors">Confidentialité</NavLink></li>
              <li><NavLink to="/mentions-legales" className="hover:text-accent transition-colors">Mentions Légales</NavLink></li>
              <li><NavLink to="/faq" className="hover:text-accent transition-colors">FAQ</NavLink></li>
            </ul>
          </div>
          <div>
            <h4 className="text-sm font-bold text-white mb-3">Suivez-nous</h4>
            <p className="text-sm text-steel-300">ALFA Construction<br/>République du Congo</p>
          </div>
        </div>
        <div className="mt-8 pt-6 border-t border-steel-700/50 text-center text-xs text-steel-500">
          ALFA Construction - Republique du Congo | <NavLink to="/mentions-legales" className="hover:text-accent">Mentions Légales</NavLink>
        </div>
      </div>
    </footer>
  );
}
