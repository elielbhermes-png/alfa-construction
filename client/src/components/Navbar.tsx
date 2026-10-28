import { useState, useEffect } from 'react';
import { NavLink, useLocation } from 'react-router-dom';
import { Button } from '@/components/ui/button';
import { Menu, X, Globe } from 'lucide-react';
import { useI18n } from '@/contexts/I18nContext';

const navItems = [
  { to: '/', label: 'Accueil' },
  { to: '/a-propos', label: 'A propos' },
  { to: '/nos-services', label: 'Services' },
  { to: '/nos-realisations', label: 'Projets' },
  { to: '/contactez-nous', label: 'Contact' },
];

export function Navbar() {
  const [scrolled, setScrolled] = useState(false);
  const [mobileOpen, setMobileOpen] = useState(false);
  const { t, locale, setLocale } = useI18n();
  const location = useLocation();

  useEffect(() => {
    const handleScroll = () => setScrolled(window.scrollY > 20);
    window.addEventListener('scroll', handleScroll);
    return () => window.removeEventListener('scroll', handleScroll);
  }, []);

  useEffect(() => {
    setMobileOpen(false);
  }, [location]);

  return (
    <header className={`fixed top-0 left-0 right-0 z-50 transition-all duration-300 ${scrolled ? 'bg-navy-900/95 backdrop-blur-md border-b border-steel-700/50' : 'bg-transparent'}`}>
      <nav className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-16 sm:h-20 flex items-center justify-between">
        <NavLink to="/" className="flex items-center gap-2 group">
          <svg className="w-8 h-8 text-accent" viewBox="0 0 32 32" fill="none" stroke="currentColor" strokeWidth={2}>
            <path d="M4 16 L10 8 L14 16 L22 16 L28 24 L26 16" strokeWidth={2.5} strokeLinecap="round" strokeLinejoin="round" />
            <path d="M8 24 L6 26" strokeWidth={2} strokeLinecap="round" />
            <path d="M24 8 L26 10" strokeWidth={2} strokeLinecap="round" />
          </svg>
          <span className="text-lg font-extrabold tracking-tight text-white hidden sm:block">ALFA<span className="text-accent"> CONSTRUCTION</span></span>
        </NavLink>

        <div className="hidden md:flex items-center gap-1">
          {navItems.map((item) => (
            <NavLink key={item.to} to={item.to} className={({ isActive }) => `px-3 py-2 rounded-md text-sm font-medium transition-colors ${isActive ? 'text-accent bg-white/5' : 'text-steel-300 hover:text-white hover:bg-steel-700/50'}`}>
              {item.label}
            </NavLink>
          ))}
        </div>

        <div className="flex items-center gap-2">
          <Button
            variant="ghost"
            size="sm"
            className="text-steel-200 hover:text-white hover:bg-steel-700/50"
            onClick={() => setLocale(locale === 'fr' ? 'en' : 'fr')}
          >
            <Globe className="w-4 h-4" />
            <span className="hidden sm:inline text-xs">{locale === 'fr' ? 'EN' : 'FR'}</span>
          </Button>
          <Button variant="outline" size="sm" className="hidden sm:inline-flex text-white border-steel-500 bg-white/5 hover:bg-white/10" asChild>
            <NavLink to="/contactez-nous">Demander un devis</NavLink>
          </Button>
          <button className="md:hidden p-2 rounded-lg text-steel-200 hover:bg-steel-700/50" onClick={() => setMobileOpen(!mobileOpen)}>
            {mobileOpen ? <X className="w-5 h-5" /> : <Menu className="w-5 h-5" />}
          </button>
        </div>
      </nav>

      {mobileOpen && (
        <div className="md:hidden bg-navy-900/98 border-t border-steel-700/50 shadow-xl">
          <div className="px-4 py-4 space-y-2">
            {navItems.map((item) => (
              <NavLink key={item.to} to={item.to} className={({ isActive }) => `block px-3 py-3 rounded-lg text-sm font-medium ${isActive ? 'text-accent bg-white/5' : 'text-steel-300 hover:bg-white/5'}`} onClick={() => setMobileOpen(false)}>
                {item.label}
              </NavLink>
            ))}
            <Button className="w-full justify-center" asChild>
              <NavLink to="/contactez-nous">Demander un devis</NavLink>
            </Button>
          </div>
        </div>
      )}
    </header>
  );
}
