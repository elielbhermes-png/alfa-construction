import { useRef } from 'react';
import { NavLink } from 'react-router-dom';
import { Button } from '@/components/ui/button';
import { ArrowRight, Building, Truck, Pickaxe, Grid, TrendingUp, Shield, Loader } from 'lucide-react';
import { useI18n } from '@/contexts/I18nContext';

export function HomePage() {
  const { t } = useI18n();
  const heroRef = useRef<HTMLDivElement>(null);

  return (
    <div ref={heroRef} className="min-h-screen flex flex-col">
      <section id="accueil" className="relative min-h-screen flex items-center justify-center overflow-hidden bg-navy-900">
        <div className="absolute inset-0 bg-gradient-to-b from-transparent via-navy-900/40 to-navy-900" />
        <div className="relative max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-20 sm:py-28 w-full">
          <div className="text-center">
            <p className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-white/5 border border-steel-600/50 text-steel-200 text-xs font-semibold mb-6">
              <svg className="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth={2}><rect x="4" y="4" width="16" height="16" rx="2"/><path d="M4 16l4-4 4 4 4-8 4 8"/></svg>
              Republique du Congo
            </p>
            <h1 className="text-4xl sm:text-5xl md:text-6xl lg:text-7xl font-extrabold leading-tight text-white">Construisons<br/><span className="text-accent">l'Avenir</span></h1>
            <p className="mt-6 text-lg sm:text-xl text-steel-300 max-w-2xl mx-auto leading-relaxed">Bâtiment & Travaux Publics · Transport & Logistique · Exploitation de Carrières · Bureau d'Étude</p>
            <div className="mt-8 flex flex-col sm:flex-row gap-3 justify-center">
              <Button size="lg" className="text-base px-8" asChild><NavLink to="/nos-realisations">Voir tous les projets <ArrowRight className="w-5 h-5" /></NavLink></Button>
              <Button size="lg" variant="outline" className="text-base px-8 border-white/20 text-white hover:bg-white/10" asChild><NavLink to="/contactez-nous">Demander un devis</NavLink></Button>
            </div>
          </div>
        </div>
      </section>

      <section className="py-16 sm:py-24 bg-navy-900/50">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center mb-12 sm:mb-16">
            <h2 className="text-2xl sm:text-3xl md:text-4xl font-extrabold text-white">Sectors d'Activite</h2>
            <p className="text-steel-300 mt-3 max-w-xl mx-auto">Des compétences complètes pour toutes les phases de vos projets</p>
          </div>
          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4 sm:gap-6">
            {[
              { icon: Building, title: "Bâtiment & Travaux Publics", desc: "Construction, travaux civils et foncées." },
              { icon: Truck, title: "Transport & Logistique", desc: "Transport et logistique de matériaux." },
              { icon: Pickaxe, title: "Exploitation de Carrières", desc: "Exploitation de carrières." },
              { icon: Grid, title: "Bureau d'Etude", desc: "Bureau d'Etude et études techniques." },
            ].map((s, i) => (
              <div key={i} className="group cursor-pointer">
                <div className="h-40 sm:h-48 rounded-xl bg-gradient-to-br from-navy-700/50 to-navy-800/50 border border-steel-600/20 flex items-center justify-center overflow-hidden">
                  <s.icon className="w-10 h-10 text-steel-300 group-hover:text-accent transition-colors duration-300" />
                </div>
                <h3 className="mt-4 text-sm font-bold text-white">{s.title}</h3>
                <p className="text-xs text-steel-400 mt-1">{s.desc}</p>
              </div>
            ))}
          </div>
        </div>
      </section>

      <section className="py-16 sm:py-24 bg-navy-900/50">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center mb-12">
            <h2 className="text-2xl sm:text-3xl md:text-4xl font-extrabold text-white">Projets Mélés</h2>
            <p className="text-steel-300 mt-3 max-w-xl mx-auto">Des réalisations qui marquent les esprits</p>
            <NavLink to="/nos-realisations">
              <Button variant="ghost" className="mt-4 text-accent border-accent/30 hover:bg-accent/5">Voir tous les projets <ArrowRight className="w-4 h-4" /></Button>
            </NavLink>
          </div>
          <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
            {[
              { title: 'Plateforme 600', loc: 'Congo' },
              { title: 'Wattaya', loc: 'Congo' },
              { title: 'Cité Verte', loc: 'Congo' },
            ].map((p, i) => (
              <div key={i} className="group cursor-pointer">
                <div className="h-48 rounded-xl bg-gradient-to-br from-steel-700/30 to-steel-800/50 border border-steel-600/20 overflow-hidden flex items-center justify-center">
                  <div className="text-steel-400"><svg className="w-12 h-12" viewBox="0 0 64 64" fill="none" stroke="currentColor" strokeWidth={1.5}><path d="M16 40 L32 24 L48 40 L48 56 L16 56 Z" strokeLinecap="round" strokeLinejoin="round"/></svg></div>
                </div>
                <h3 className="mt-4 font-bold text-white">{p.title}</h3>
                <p className="text-xs text-steel-400">{p.loc}</p>
              </div>
            ))}
          </div>
        </div>
      </section>

      <section className="py-16 sm:py-24">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="grid grid-cols-1 md:grid-cols-4 gap-6">
            {[
              { icon: TrendingUp, title: 'Qualité', desc: 'Des normes strictes.' },
              { icon: Shield, title: 'Sécurité', desc: 'Un environnement sûr.' },
              { icon: Loader, title: 'Fiabilité', desc: 'Des délais respectés.' },
              { icon: TrendingUp, title: 'Innovation', desc: 'Des solutions modernes.' },
            ].map((s, i) => (
              <div key={i} className="p-6 rounded-xl border border-steel-600/20 bg-navy-800/20 hover:bg-navy-800/40 transition-colors cursor-pointer">
                <s.icon className="w-8 h-8 text-accent mb-3" />
                <h3 className="font-bold text-white">{s.title}</h3>
                <p className="text-xs text-steel-400 mt-1">{s.desc}</p>
              </div>
            ))}
          </div>
        </div>
      </section>

      <section className="py-16 sm:py-24 bg-gradient-to-r from-navy-800/50 to-navy-900">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
          <h2 className="text-2xl sm:text-3xl md:text-4xl font-extrabold text-white">Construisons Ensemble</h2>
          <p className="text-steel-300 mt-4 max-w-xl mx-auto">Pour vos demandes de projet, devis ou partenariats.</p>
          <div className="mt-8 flex flex-col sm:flex-row gap-3 justify-center">
            <Button size="lg" asChild><NavLink to="/contactez-nous">Demander un devis</NavLink></Button>
            <Button variant="outline" size="lg" className="border-white/30 text-white hover:bg-white/10" asChild><a href="mailto:ali-safa@alfa-constructions.com">Email</a></Button>
          </div>
        </div>
      </section>
    </div>
  );
}
