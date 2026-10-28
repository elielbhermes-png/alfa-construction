import os

os.makedirs('client/src/pages', exist_ok=True)

# HomePage - compact
homepage = """import { useRef } from 'react';
import { NavLink } from 'react-router-dom';
import { Button } from '@/components/ui/button';
import { ArrowRight, Building, Truck, Mining, Grid, TrendingUp, Shield, Loader } from 'lucide-react';
import { useI18n } from '@/contexts/I18nContext';

export function HomePage() {
  const { t } = useI18n();
  const heroRef = useRef<HTMLElement>(null);

  return (
    <div ref={heroRef} className="min-h-screen flex flex-col">
      {/* Hero */}
      <section id="accueil" className="relative min-h-screen flex items-center justify-center overflow-hidden bg-navy-900">
        <div className="absolute inset-0 bg-[url('data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIzMjBweCIgaGVpZ2h0PSIzMjBweCIgdmlld0JveD0iMCAwIDMyMCAzMjAiIGZpbGw9IiM4QzRDMzg0Ij48Y2lyY2xlIGN4PSIyMCIgY3k9IjIwIiByPSIxLjUiIGZpbGw9IiNlNjRmZjYwIi8+PC9zdmc+')] bg-center" />
        <div className="absolute inset-0 bg-gradient-to-b from-transparent via-navy-900/40 to-navy-900" />
        <div className="relative max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-20 sm:py-28 w-full">
          <div className="text-center">
            <p className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-white/5 border border-steel-600/50 text-steel-200 text-xs font-semibold mb-6">
              <svg className="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth={2}><rect x="4" y="4" width="16" height="16" rx="2"/><path d="M4 16l4-4 4 4 4-8 4 8"/></svg>
              République du Congo
            </p>
            <h1 className="text-4xl sm:text-5xl md:text-6xl lg:text-7xl font-extrabold leading-tight text-white">
              Construisons<br />
              <span className="text-accent">l'Avenir</span>
            </h1>
            <p className="mt-6 text-lg sm:text-xl text-steel-300 max-w-2xl mx-auto leading-relaxed">
              Bâtiment & Travaux Publics · Transport & Logistique · Exploitation de Carrières · Bureau d'Étude
            </p>
            <div className="mt-8 flex flex-col sm:flex-row gap-3 justify-center">
              <Button size="lg" className="text-base px-8" asChild>
                <NavLink to="/nos-realisations">{t('home.projectsCta')} <ArrowRight className="w-5 h-5" /></NavLink>
              </Button>
              <Button size="lg" variant="outline" className="text-base px-8 border-white/20 text-white hover:bg-white/10" asChild>
                <NavLink to="/contactez-nous">{t('home.contactCta')}</NavLink>
              </Button>
            </div>
          </div>
        </div>
      </section>

      {/* Sectors */}
      <section className="py-16 sm:py-24 bg-navy-900/50">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center mb-12 sm:mb-16">
            <h2 className="text-2xl sm:text-3xl md:text-4xl font-extrabold text-white">{t('home.sectorsTitle')}</h2>
            <p className="text-steel-300 mt-3 max-w-xl mx-auto">Des compétences complètes pour toutes les phases de vos projets</p>
          </div>
          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4 sm:gap-6">
            {[
              { icon: Building, title: t('home.sectorBuilding'), desc: 'Construction, travaux civils et foncées.' },
              { icon: Truck, title: t('home.sectorTransport'), desc: 'Transport et logistique de matériaux.' },
              { icon: Mining, title: t('home.sectorQuarry'), desc: 'Exploitation de carrières.' },
              { icon: Grid, title: t('home.sectorStudy'), desc: 'Bureau d\'Etude et études techniques.' },
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

      {/* Projects */}
      <section className="py-16 sm:py-24 bg-navy-900/50">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center mb-12">
            <h2 className="text-2xl sm:text-3xl md:text-4xl font-extrabold text-white">{t('home.projectsTitle')}</h2>
            <p className="text-steel-300 mt-3 max-w-xl mx-auto">Des réalisations qui marquent les esprits</p>
            <NavLink to="/nos-realisations">
              <Button variant="ghost" className="mt-4 text-accent border-accent/30 hover:bg-accent/5">Voir tous les projets <ArrowRight className="w-4 h-4" /></Button>
            </NavLink>
          </div>
          <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
            {[
              { title: 'Plateforme 600', loc: 'Congo', img: 'SVG' },
              { title: 'Wattaya', loc: 'Congo', img: 'SVG' },
              { title: 'Cité Verte', loc: 'Congo', img: 'SVG' },
            ].map((p, i) => (
              <div key={i} className="group cursor-pointer">
                <div className="h-48 rounded-xl bg-gradient-to-br from-steel-700/30 to-steel-800/50 border border-steel-600/20 overflow-hidden">
                  <div className="w-full h-full flex items-center justify-center text-steel-400">
                    <svg className="w-12 h-12" viewBox="0 0 64 64" fill="none" stroke="currentColor" strokeWidth={1.5}><path d="M16 40 L32 24 L48 40 L48 56 L16 56 Z" strokeLinecap="round" strokeLinejoin="round"/></svg>
                  </div>
                </div>
                <h3 className="mt-4 font-bold text-white">{p.title}</h3>
                <p className="text-xs text-steel-400">{p.loc}</p>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Strengths */}
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

      {/* Contact */}
      <section className="py-16 sm:py-24 bg-gradient-to-r from-navy-800/50 to-navy-900">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
          <h2 className="text-2xl sm:text-3xl md:text-4xl font-extrabold text-white">{t('home.contactTitle')}</h2>
          <p className="text-steel-300 mt-4 max-w-xl mx-auto">{t('home.contactText')}</p>
          <div className="mt-8 flex flex-col sm:flex-row gap-3 justify-center">
            <Button size="lg" asChild>
              <NavLink to="/contactez-nous">{t('home.contactCta')}</NavLink>
            </Button>
            <Button variant="outline" size="lg" className="border-white/30 text-white hover:bg-white/10" asChild>
              <a href="mailto:ali-safa@alfa-constructions.com">Email</a>
            </Button>
          </div>
        </div>
      </section>
    </div>
  );
}
"""

# AboutPage
aboutpage = """import { useI18n } from '@/contexts/I18nContext';
import { useSupabase } from '@/contexts/SupabaseProvider';
import { useEffect, useState } from 'react';
import { Building, Users, Shield, GraduationCap, ArrowRight, Globe } from 'lucide-react';
import { Link } from 'react-router-dom';

export function AboutPage() {
  const { t } = useI18n();
  const { supabase: supabaseClient, initialized } = useSupabase();
  const [aboutContent, setAboutContent] = useState<{ title: string; description: string } | null>(null);

  useEffect(() => {
    if (!initialized) return;
    supabaseClient?.from('site_settings').select('value').eq('key', 'about_content').single()
      .then(({ data }) => { if (data) setAboutContent(JSON.parse(data.value)); })
      .catch(() => {});
  }, [initialized, supabaseClient]);

  if (!aboutContent) {
    aboutContent = { title: t('about.title'), description: t('about.intro') };
  }

  return (
    <div className="py-16 sm:py-24 bg-navy-900/50 min-h-screen">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-10 items-center">
          <div>
            <p className="text-accent text-sm font-semibold mb-3">À propos</p>
            <h1 className="text-3xl sm:text-4xl md:text-5xl font-extrabold text-white leading-tight">{aboutContent.title}</h1>
            <p className="text-steel-300 mt-4 text-lg leading-relaxed">{aboutContent.description}</p>
            <div className="mt-8 flex flex-wrap gap-4">
              <Link to="/nos-realisations"><Button variant="ghost" className="text-white border-steel-600 hover:bg-white/5"><Building className="w-4 h-4 mr-2" />Projets</Button></Link>
              <Link to="/contactez-nous"><Button variant="outline" className="text-white border-steel-600 bg-white/5 hover:bg-white/10"><Users className="w-4 h-4 mr-2" />Notre équipe</Button></Link>
            </div>
          </div>
          <div className="grid grid-cols-2 gap-4">
            {[
              { icon: Building, title: 'Domaines', desc: '4 secteurs d\'activité' },
              { icon: Users, title: 'Collectif', desc: 'Alliance d\'expertises' },
              { icon: Shield, title: 'Sécurité', desc: 'Normes internationales' },
              { icon: GraduationCap, title: 'Innovation', desc: 'Pisteurs de solutions' },
            ].map((s, i) => (
              <div key={i} className="p-6 rounded-xl border border-steel-600/20 bg-navy-800/30">
                <s.icon className="w-6 h-6 text-accent mb-3" />
                <h3 className="font-bold text-white">{s.title}</h3>
                <p className="text-xs text-steel-300 mt-1">{s.desc}</p>
              </div>
            ))}
          </div>
        </div>
      </div>
    </div>
  );
}
"""

# ServicesPage
servicespage = """import { useState } from 'react';
import { useI18n } from '@/contexts/I18nContext';
import { useSupabase } from '@/contexts/SupabaseProvider';
import { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import { Button } from '@/components/ui/button';
import { ArrowRight, Wrench, Truck, Mining, Grid, GraduationCap, ChevronRight } from 'lucide-react';

export function ServicesPage() {
  const { t } = useI18n();
  const { supabase: supabaseClient, initialized } = useSupabase();
  const [services, setServices] = useState<Array<{ id: string; title: string; short_description: string; image_path: string | null; status: string }>>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    if (!initialized) return;
    supabaseClient?.from('services').select('*').eq('status', 'published').order('display_order')
      .then(({ data }) => { setServices(data ?? []); setLoading(false); })
      .catch(() => { setLoading(false); });
  }, [initialized, supabaseClient]);

  if (loading) return <div className="min-h-screen flex items-center justify-center"><p className="text-steel-300">Chargement...</p></div>;

  return (
    <div className="py-16 sm:py-24 bg-navy-900/50">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="text-center mb-12 sm:mb-16">
          <h1 className="text-3xl sm:text-4xl md:text-5xl font-extrabold text-white">{t('services.title')}</h1>
          <p className="text-steel-300 mt-4 max-w-xl mx-auto">{t('services.subtitle')}</p>
        </div>
        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
          {services.map((s) => (
            <div key={s.id} className="group p-6 rounded-xl border border-steel-600/20 bg-navy-800/20 hover:bg-navy-800/40 transition-all duration-300 hover:-translate-y-1 cursor-pointer">
              <div className="h-36 rounded-lg bg-gradient-to-br from-steel-700/30 to-steel-800/50 border border-steel-600/20 flex items-center justify-center overflow-hidden mb-4">
                <div className="text-steel-400">
                  {s.title.charAt(0)}
                </div>
              </div>
              <h3 className="text-lg font-bold text-white">{s.title}</h3>
              <p className="text-steel-300 text-sm mt-2 leading-relaxed">{s.short_description}</p>
              <Link to="/contactez-nous">
                <Button variant="ghost" className="mt-4 text-accent border-accent/30 hover:bg-accent/5 w-full justify-center"><ArrowRight className="w-4 h-4 mr-2" /> Demander ce service</Button>
              </Link>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}
"""

# ProjectsPage
projectspage = """import { useI18n } from '@/contexts/I18nContext';
import { useSupabase } from '@/contexts/SupabaseProvider';
import { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import { Button } from '@/components/ui/button';
import { ArrowRight, Filter, Loader, Plus } from 'lucide-react';

export function ProjectsPage() {
  const { t } = useI18n();
  const { supabase: supabaseClient, initialized } = useSupabase();
  const [projects, setProjects] = useState<Array<{ id: string; title: string; short_description: string; location: string | null; cover_image_path: string | null; status: string }>>([]);
  const [loading, setLoading] = useState(true);
  const [category, setCategory] = useState<string>('all');

  useEffect(() => {
    if (!initialized) return;
    supabaseClient?.from('projects').select('*').order('updated_at', { ascending: false })
      .then(({ data }) => { setProjects(data ?? []); setLoading(false); })
      .catch(() => { setLoading(false); });
  }, [initialized, supabaseClient]);

  const filtered = category === 'all' ? projects : projects.filter(p => p.category_id === category);
  const publishable: Array<{ id: string; label: string }> = [
    { id: 'batiments', label: 'Bâtiment' },
    { id: 'travaux-publics', label: 'Travaux Publics' },
    { id: 'transport', label: 'Transport' },
    { id: 'carrieres', label: 'Carrières' },
    { id: 'bureaude', label: 'Bureau d\'Etude' },
  ];

  if (loading) return <div className="min-h-screen flex items-center justify-center"><p className="text-steel-300">{t('shared.loading')}</p></div>;

  return (
    <div className="py-16 sm:py-24 bg-navy-900/50">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="text-center mb-10">
          <h1 className="text-3xl sm:text-4xl md:text-5xl font-extrabold text-white">{t('projects.title')}</h1>
          <p className="text-steel-300 mt-4">{t('projects.subtitle')}</p>
        </div>
        <div className="flex flex-wrap gap-2 mb-8 justify-center">
          <Button variant="outline" size="sm" className={category === 'all' ? 'bg-accent text-navy-900' : 'bg-transparent text-white border-steel-500 hover:bg-white/10'} onClick={() => setCategory('all')}>{t('projects.all')}</Button>
          {publishable.map(c => (
            <Button key={c.id} variant="outline" size="sm" className={category === c.id ? 'bg-accent text-navy-900' : 'bg-transparent text-white border-steel-500 hover:bg-white/10'} onClick={() => setCategory(c.id)}>{c.label}</Button>
          ))}
        </div>
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {filtered.map((p) => (
            <Link key={p.id} to={`/realisations/${p.slug || p.id}`} className="group block">
              <div className="h-48 rounded-xl bg-gradient-to-br from-steel-700/30 to-steel-800/50 border border-steel-600/20 overflow-hidden flex items-center justify-center">
                <div className="text-steel-400"><svg className="w-12 h-12" viewBox="0 0 64 64" fill="none" stroke="currentColor" strokeWidth={1.5}><path d="M16 40 L32 24 L48 40 L48 56 L16 56 Z" strokeLinecap="round" strokeLinejoin="round"/></svg></div>
              </div>
              <div className="mt-4">
                <h3 className="font-bold text-white">{p.title}</h3>
                <p className="text-xs text-steel-400 mt-1">{p.location || 'Lieu à confirmer'}</p>
                <p className="text-xs text-steel-300 mt-2 line-clamp-2">{p.short_description}</p>
              </div>
            </Link>
          ))}
          {filtered.length === 0 && <div className="col-span-3 text-center text-steel-400 py-12">{t('projects.none')}</div>}
        </div>
      </div>
    </div>
  );
}
"""

# ProjectDetailPage
projectdetail = """import { useParams, Link } from 'react-router-dom';
import { useI18n } from '@/contexts/I18nContext';
import { useSupabase } from '@/contexts/SupabaseProvider';
import { useEffect, useState } from 'react';
import { ArrowLeft, ArrowRight, Edit, MapPin, Calendar, FolderOpen, Image, FileText } from 'lucide-react';

export function ProjectDetailPage() {
  const { slug } = useParams();
  const { t } = useI18n();
  const { supabase: supabaseClient, initialized } = useSupabase();
  const [project, setProject] = useState<any>(null);
  const [images, setImages] = useState<Array<{ id: string; caption: string; alt_text: string; storage_path: string }>>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    if (!initialized) return;
    supabaseClient?.from('projects').select('*').eq('slug', slug).or('status.eq.published,status.eq.draft').single()
      .then(({ data }) => { setProject(data); })
      .catch(() => {});
    supabaseClient?.from('project_images').select('*').eq('project_id', slug).order('display_order')
      .then(({ data }) => { setImages(data ?? []); })
      .catch(() => {});
    setLoading(false);
  }, [initialized, supabaseClient, slug]);

  if (loading) return <div className="min-h-screen flex items-center justify-center"><p className="text-steel-300">{t('shared.loading')}</p></div>;
  if (!project) return <div className="min-h-screen flex items-center justify-center"><p className="text-steel-300">Aucun projet trouvé.</p></div>;

  return (
    <div className="py-16 sm:py-24 bg-navy-900/50">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <Link to="/nos-realisations"><ArrowLeft className="w-4 h-4 text-steel-300 hover:text-white mb-4 inline-block" /></Link>
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
          {/* Gallery */}
          <div>
            {images.length > 0 ? (
              <div className="space-y-3">
                {images.map((img, i) => (
                  <div key={img.id} className={`rounded-xl border border-steel-600/20 overflow-hidden ${i === 0 ? 'md:col-span-2' : ''}`}>
                    <img src={img.storage_path || ''} alt={img.alt_text || t('project.gallery')} className={`w-full object-cover ${i === 0 ? 'h-64' : 'h-24'}`} />
                    {img.caption && <p className="p-3 text-sm text-steel-300">{img.caption}</p>}
                  </div>
                ))}
              </div>
            ) : (
              <div className="h-64 rounded-xl bg-gradient-to-br from-steel-700/30 to-steel-800/50 border border-steel-600/20 flex items-center justify-center">
                <div className="text-steel-400"><FolderOpen className="w-12 h-12" /></div>
              </div>
            )}
          </div>
          {/* Details */}
          <div>
            <h1 className="text-3xl sm:text-4xl font-extrabold text-white">{project.title}</h1>
            <div className="flex flex-wrap gap-3 mt-4 text-sm text-steel-300">
              {project.location && <span className="flex items-center gap-1"><MapPin className="w-4 h-4" /> {project.location}</span>}
              {project.start_date && <span className="flex items-center gap-1"><Calendar className="w-4 h-4" /> {new Date(project.start_date).toLocaleDateString('fr-FR')}</span>}
              {project.completion_date && <span className="flex items-center gap-1"><Calendar className="w-4 h-4" /> {new Date(project.completion_date).toLocaleDateString('fr-FR')}</span>}
            </div>
            <p className="text-steel-300 mt-6 leading-relaxed">{project.description}</p>
            <div className="mt-8 flex gap-3">
              <Link to="/contactez-nous"><button className="flex items-center gap-2 px-6 py-3 rounded-lg bg-accent text-navy-900 font-semibold hover:bg-accent/90 transition-colors">Demander le devis</button></Link>
              <Link to="/nos-realisations"><button className="px-6 py-3 rounded-lg border border-steel-500 text-white hover:bg-white/5 transition-colors">Retour aux projets</button></Link>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
"""

with open('client/src/pages/HomePage.tsx', 'w') as f:
    f.write(homepage)
with open('client/src/pages/AboutPage.tsx', 'w') as f:
    f.write(aboutpage)
with open('client/src/pages/ServicesPage.tsx', 'w') as f:
    f.write(servicespage)
with open('client/src/pages/ProjectsPage.tsx', 'w') as f:
    f.write(projectspage)
with open('client/src/pages/ProjectDetailPage.tsx', 'w') as f:
    f.write(projectdetail)

print("Pages written")
