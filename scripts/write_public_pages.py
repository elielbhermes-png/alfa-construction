import os

os.makedirs('client/src/pages', exist_ok=True)
os.makedirs('client/src/pages/admin', exist_ok=True)

# HomePage
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
              { icon: Mining, title: "Exploitation de Carrières", desc: "Exploitation de carrières." },
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
"""

# AboutPage
aboutpage = """import { useI18n } from '@/contexts/I18nContext';
import { useSupabase } from '@/contexts/SupabaseProvider';
import { useEffect, useState } from 'react';
import { Building, Users, Shield, GraduationCap, Link, ArrowRight } from 'lucide-react';

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
import { ArrowRight } from 'lucide-react';

export function ServicesPage() {
  const { t } = useI18n();
  const { supabase: supabaseClient, initialized } = useSupabase();
  const [services, setServices] = useState<Array<{ id: string; title: string; short_description: string; status: string }>>([]);
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
                <div className="text-steel-400">{s.title.charAt(0)}</div>
              </div>
              <h3 className="text-lg font-bold text-white">{s.title}</h3>
              <p className="text-steel-300 text-sm mt-2 leading-relaxed">{s.short_description}</p>
              <Link to="/contactez-nous">
                <Button variant="ghost" className="mt-4 text-accent border-accent/30 hover:bg-accent/5"><ArrowRight className="w-4 h-4 mr-2" /> Demander ce service</Button>
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
import { ArrowRight } from 'lucide-react';

export function ProjectsPage() {
  const { t } = useI18n();
  const { supabase: supabaseClient, initialized } = useSupabase();
  const [projects, setProjects] = useState<Array<any>>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    if (!initialized) return;
    supabaseClient?.from('projects').select('*').order('updated_at', { ascending: false })
      .then(({ data }) => { setProjects(data ?? []); setLoading(false); })
      .catch(() => { setLoading(false); });
  }, [initialized, supabaseClient]);

  if (loading) return <div className="min-h-screen flex items-center justify-center"><p className="text-steel-300">Chargement...</p></div>;

  return (
    <div className="py-16 sm:py-24 bg-navy-900/50">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="text-center mb-10">
          <h1 className="text-3xl sm:text-4xl md:text-5xl font-extrabold text-white">{t('projects.title')}</h1>
          <p className="text-steel-300 mt-4">{t('projects.subtitle')}</p>
        </div>
        <div className="flex flex-wrap gap-2 mb-8 justify-center">
          <Button variant="outline" size="sm" className="bg-transparent text-white border-steel-500 hover:bg-white/10">Tous</Button>
          <Button variant="outline" size="sm" className="bg-transparent text-white border-steel-500 hover:bg-white/10">Bâtiment</Button>
          <Button variant="outline" size="sm" className="bg-transparent text-white border-steel-500 hover:bg-white/10">Travaux Publics</Button>
          <Button variant="outline" size="sm" className="bg-transparent text-white border-steel-500 hover:bg-white/10">Transport</Button>
          <Button variant="outline" size="sm" className="bg-transparent text-white border-steel-500 hover:bg-white/10">Carrières</Button>
          <Button variant="outline" size="sm" className="bg-transparent text-white border-steel-500 hover:bg-white/10">Bureau d'Etude</Button>
        </div>
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {projects.map((p: any) => (
            <Link key={p.id} to={`/realisations/${p.slug || p.id}`} className="group block">
              <div className="h-48 rounded-xl bg-gradient-to-br from-steel-700/30 to-steel-800/50 border border-steel-600/20 overflow-hidden flex items-center justify-center">
                <div className="text-steel-400"><svg className="w-12 h-12" viewBox="0 0 64 64" fill="none" stroke="currentColor" strokeWidth={1.5}><path d="M16 40 L32 24 L48 40 L48 56 L16 56 Z" strokeLinecap="round" strokeLinejoin="round"/></svg></div>
              </div>
              <div className="mt-4">
                <h3 className="font-bold text-white">{p.title}</h3>
                <p className="text-xs text-steel-400">{p.location || ''}</p>
                <p className="text-xs text-steel-300 mt-2 line-clamp-2">{p.short_description}</p>
              </div>
            </Link>
          ))}
          {projects.length === 0 && <div className="col-span-3 text-center text-steel-400 py-12">{t('projects.none')}</div>}
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
import { ArrowLeft, MapPin, Calendar, FolderOpen, FileText } from 'lucide-react';

export function ProjectDetailPage() {
  const { slug } = useParams();
  const { t } = useI18n();
  const { supabase: supabaseClient, initialized } = useSupabase();
  const [project, setProject] = useState<any>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    if (!initialized) return;
    supabaseClient?.from('projects').select('*').eq('slug', slug).or('status.eq.published,status.eq.draft').single()
      .then(({ data }) => { setProject(data); })
      .catch(() => {});
    setLoading(false);
  }, [initialized, supabaseClient, slug]);

  if (loading) return <div className="min-h-screen flex items-center justify-center"><p className="text-steel-300">Chargement...</p></div>;
  if (!project) return <div className="min-h-screen flex items-center justify-center"><p className="text-steel-300">Aucun projet trouvé.</p></div>;

  return (
    <div className="py-16 sm:py-24 bg-navy-900/50">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <Link to="/nos-realisations"><ArrowLeft className="w-4 h-4 text-steel-300 hover:text-white mb-4 inline-block" /></Link>
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
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

# ContactPage
contactpage = """import { useState } from 'react';
import { useI18n } from '@/contexts/I18nContext';
import { useSupabase } from '@/contexts/SupabaseProvider';
import { Controller, useForm } from 'react-hook-form';
import { zodResolver } from '@hookform/resolvers/zod';
import { ContactFormSchema, type ContactFormValues, QuotationFormSchema, type QuotationFormValues } from '@/lib/validation';
import { Button } from '@/components/ui/button';
import { Input } from '@/components/ui/input';
import { Textarea } from '@/components/ui/input';
import { Mail, Phone, MapPin, FileText, Send, Loader, ArrowLeft } from 'lucide-react';
import { Link } from 'react-router-dom';

export function ContactPage() {
  const { t } = useI18n();
  const { supabase: supabaseClient, initialized } = useSupabase();
  const [formStatus, setFormStatus] = useState<'idle' | 'loading' | 'success' | 'error'>('idle');

  const contactForm = useForm<ContactFormValues>({
    resolver: zodResolver(ContactFormSchema),
    defaultValues: { name: '', company: '', email: '', phone: '', subject: '', message: '', privacy: false },
  });

  const quotationForm = useForm<QuotationFormValues>({
    resolver: zodResolver(QuotationFormSchema),
    defaultValues: { name: '', company: '', email: '', phone: '', service: '', projectLocation: '', projectDescription: '', estimatedBudget: '', desiredStartDate: '', files: [] },
  });

  const handleSubmit = async (data: any, form: typeof contactForm) => {
    if (!initialized || !supabaseClient) { setFormStatus('error'); return; }
    try {
      setFormStatus('loading');
      const { error } = await supabaseClient.from('contact_messages').insert({
        name: data.name, company: data.company, email: data.email, phone: data.phone,
        subject: data.subject, message: data.message, status: 'new',
      });
      if (error) throw error;
      setFormStatus('success');
      form.reset();
    } catch {
      setFormStatus('error');
    }
  };

  return (
    <div className="py-16 sm:py-24 bg-navy-900/50">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="text-center mb-12 sm:mb-16">
          <h1 className="text-3xl sm:text-4xl md:text-5xl font-extrabold text-white">{t('contact.title')}</h1>
          <p className="text-steel-300 mt-4 max-w-xl mx-auto">{t('contact.subtitle')}</p>
        </div>
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
          <div className="space-y-6">
            {[
              { icon: Mail, label: 'Email', value: 'ali-safa@alfa-constructions.com' },
              { icon: Phone, label: 'Téléphone', value: '+242 06 822 22 20' },
              { icon: MapPin, label: 'Adresse', value: 'Avenue Docteur Cardorelle, Songolo, Congo' },
            ].map((item) => (
              <div key={item.label} className="flex items-start gap-4 p-4 rounded-xl border border-steel-600/20 bg-navy-800/20">
                <item.icon className="w-5 h-5 text-accent flex-shrink-0 mt-1" />
                <div><p className="text-xs text-steel-400">{item.label}</p><p className="text-sm font-medium text-white">{item.value}</p></div>
              </div>
            ))}
          </div>
          <div className="space-y-6">
            <div className="p-6 rounded-xl border border-steel-600/20 bg-navy-800/20">
              <h3 className="text-lg font-bold text-white mb-4">{t('contact.submit')}</h3>
              {formStatus === 'success' && <p className="text-green-400 text-sm">{t('contact.success')}</p>}
              {formStatus === 'error' && <p className="text-red-400 text-sm">{t('contact.error')}</p>}
              <form id="contact-form" onSubmit={contactForm.handleSubmit((data) => handleSubmit(data, contactForm))} className="space-y-4">
                <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
                  <div className="col-span-full"><Input {...contactForm.register('name')} placeholder={t('contact.name')} /></div>
                  <div className="col-span-full"><Input {...contactForm.register('email')} type="email" placeholder={t('contact.email')} /></div>
                </div>
                <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
                  <div className="col-span-full"><Input {...contactForm.register('phone')} placeholder={t('contact.phone')} /></div>
                  <div className="col-span-full"><Input {...contactForm.register('subject')} placeholder={t('contact.subject')} /></div>
                </div>
                <div className="col-span-full"><Textarea {...contactForm.register('message')} rows={5} placeholder={t('contact.message')} /></div>
                <div className="flex items-center gap-2">
                  <input type="checkbox" {...contactForm.register('privacy')} className="w-4 h-4 rounded border-steel-500 bg-navy-700 accent-accent" />
                  <label className="text-sm text-steel-300">{t('contact.privacy')} {t('contact.required')}</label>
                </div>
                <Button type="submit" className="w-full sm:w-auto" disabled={formStatus === 'loading'}>
                  {formStatus === 'loading' && <Loader className="w-4 h-4 animate-spin mr-2" />}
                  {formStatus === 'loading' ? t('quotation.processing') : <><Send className="w-4 h-4 mr-2" />{t('contact.submit')}</>}
                </Button>
              </form>
            </div>
            <div className="p-6 rounded-xl border border-steel-600/20 bg-navy-800/20">
              <h3 className="text-lg font-bold text-white mb-4">{t('contact.quotationTitle')}</h3>
              <form className="space-y-4">
                <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
                  <div className="col-span-full"><Input {...quotationForm.register('name')} placeholder={t('contact.name')} /></div>
                  <div className="col-span-full"><Input {...quotationForm.register('email')} type="email" placeholder={t('contact.email')} /></div>
                </div>
                <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
                  <div className="col-span-full"><Input {...quotationForm.register('phone')} placeholder={t('contact.phone')} /></div>
                  <div className="col-span-full"><Input {...quotationForm.register('service')} placeholder={t('contact.service')} /></div>
                </div>
                <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
                  <div className="col-span-full"><Input {...quotationForm.register('projectLocation')} placeholder={t('contact.location')} /></div>
                  <div className="col-span-full"><Input {...quotationForm.register('estimatedBudget')} placeholder={t('contact.budget')} /></div>
                </div>
                <div className="col-span-full"><Textarea {...quotationForm.register('projectDescription')} rows={4} placeholder={t('contact.description')} /></div>
                <Button type="submit" className="w-full sm:w-auto bg-green-600 hover:bg-green-500">{t('contact.quotationTitle')}</Button>
              </form>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
"""

# PrivacyPage, LegalPage, FaqPage, NotFoundPage
privacy = """import { useI18n } from '@/contexts/I18nContext';

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
"""

legal = """import { useI18n } from '@/contexts/I18nContext';
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
"""

faq = """import { useI18n } from '@/contexts/I18nContext';

export function FaqPage() {
  const { t } = useI18n();
  const faqs = [
    { q: t('faq.q1'), a: t('faq.a1') },
    { q: t('faq.q2'), a: t('faq.a2') },
    { q: t('faq.q3'), a: t('faq.a3') },
    { q: t('faq.q4'), a: t('faq.a4') },
    { q: t('faq.q5'), a: t('faq.a5') },
  ];
  return (
    <div className="py-16 sm:py-24 bg-navy-900/50 min-h-screen">
      <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
        <h1 className="text-3xl sm:text-4xl font-extrabold text-white text-center mb-12">{t('faq.title')}</h1>
        <div className="space-y-4">
          {faqs.map((faq, i) => (
            <div key={i} className="p-6 rounded-xl border border-steel-600/20 bg-navy-800/20">
              <h3 className="font-bold text-white">{faq.q}</h3>
              <p className="text-steel-300 text-sm mt-2">{faq.a}</p>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}
"""

notfound = """import { Link } from 'react-router-dom';
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
with open('client/src/pages/ContactPage.tsx', 'w') as f:
    f.write(contactpage)
with open('client/src/pages/PrivacyPage.tsx', 'w') as f:
    f.write(privacy)
with open('client/src/pages/LegalPage.tsx', 'w') as f:
    f.write(legal)
with open('client/src/pages/FaqPage.tsx', 'w') as f:
    f.write(faq)
with open('client/src/pages/NotFoundPage.tsx', 'w') as f:
    f.write(notfound)

print("Public pages created")
