import os

os.makedirs('client/src/pages/admin', exist_ok=True)

admin_layout = """import { useEffect, useState } from 'react';
import { useNavigate, Link, Outlet } from 'react-router-dom';
import { useI18n } from '@/contexts/I18nContext';
import { useSupabase } from '@/contexts/SupabaseProvider';
import { Button } from '@/components/ui/button';
import { Badge } from '@/components/ui/input';
import { LayoutDashboard, FileText, Wrench, Image, MessageSquare, BarChart3, Settings, LogOut, Menu, X } from 'lucide-react';

export function AdminLayout() {
  const { t } = useI18n();
  const { supabase, initialized } = useSupabase();
  const navigate = useNavigate();
  const [loading, setLoading] = useState(true);
  const [sideOpen, setSideOpen] = useState(false);

  useEffect(() => {
    if (!initialized) { setLoading(true); return; }
    supabase.auth.getUser()
      .then(({ data }) => {
        if (!data.user) { navigate('/admin/login'); }
      })
      .catch(() => navigate('/admin/login'))
      .finally(() => setLoading(false));
  }, [initialized, supabase, navigate]);

  if (loading) return <div className="min-h-screen flex items-center justify-center"><p>{t('shared.loading')}</p></div>;

  const navItems = [
    { icon: LayoutDashboard, label: t('admin.dashboard'), path: 'dashboard' },
    { icon: FileText, label: t('admin.projects'), path: 'projects' },
    { icon: Wrench, label: t('admin.services'), path: 'services' },
    { icon: Image, label: t('admin.media'), path: 'media' },
    { icon: MessageSquare, label: t('admin.messages'), path: 'messages' },
    { icon: BarChart3, label: t('admin.quotes'), path: 'quotes' },
    { icon: Settings, label: t('admin.settings'), path: 'settings' },
  ];

  return (
    <div className="min-h-screen bg-navy-900/30">
      <aside className={`fixed top-0 left-0 z-40 h-full w-64 bg-navy-800/95 border-r border-steel-700/50 transform transition-transform duration-300 ${sideOpen ? 'translate-x-0' : '-translate-x-full'} md:translate-x-0 md:relative`}>
        <div className="flex items-center justify-between p-4">
          <span className="text-lg font-bold text-white">ALFA Admin</span>
          <button className="md:hidden" onClick={() => setSideOpen(false)}><X className="w-5 h-5" /></button>
        </div>
        <nav className="mt-4 px-2 space-y-1">
          {navItems.map((item) => (
            <Link key={item.path} to={`/admin/${item.path}`} className="flex items-center gap-3 px-3 py-2 rounded-lg text-sm font-medium text-steel-300 hover:bg-steel-700/30 hover:text-white transition-colors">
              <item.icon className="w-4 h-4" />
              {item.label}
            </Link>
          ))}
        </nav>
        <div className="absolute bottom-0 w-full p-4">
          <Button variant="ghost" className="w-full justify-start text-steel-300 hover:text-white hover:bg-white/5" asChild>
            <Link to="/" onClick={() => supabase?.auth.signOut()}><LogOut className="w-4 h-4 mr-3" />{t('admin.signOut')}</Link>
          </Button>
        </div>
      </aside>
      <div className={`md:pl-64 transition-all duration-300 ${sideOpen ? 'md:ml-0' : ''}`}>
        <div className="h-16 bg-navy-900 border-b border-steel-700/50 px-4 flex items-center justify-between md:hidden">
          <button onClick={() => setSideOpen(true)}><Menu className="w-5 h-5 text-white" /></button>
          <span className="font-bold text-white">ALFA Admin</span>
        </div>
        <main className="p-6">
          <Outlet />
        </main>
      </div>
    </div>
  );
}
"""

login = """import { useState } from 'react';
import { useNavigate, NavLink } from 'react-router-dom';
import { useForm } from 'react-hook-form';
import { zodResolver } from '@hookform/resolvers/zod';
import { z } from 'zod';
import { useSupabase } from '@/contexts/SupabaseProvider';
import { useI18n } from '@/contexts/I18nContext';
import { Button } from '@/components/ui/button';
import { Input } from '@/components/ui/input';
import { Loader } from '@/components/Loader';
import { Mail, Lock, ArrowRight } from 'lucide-react';

const loginSchema = z.object({
  email: z.string().email(),
  password: z.string().min(1),
});
type LoginForm = z.infer<typeof loginSchema>;

export function LoginPage() {
  const { t } = useI18n();
  const { supabase, initialized } = useSupabase();
  const navigate = useNavigate();
  const [loading, setLoading] = useState(true);

  const { register, handleSubmit, formState: { errors } } = useForm<LoginForm>({
    resolver: zodResolver(loginSchema),
    defaultValues: { email: '', password: '' },
  });

  if (!initialized || !supabase) {
    return <div className="min-h-screen flex items-center justify-center">{t('shared.loading')}</div>;
  }

  const onSubmit = async (data: LoginForm) => {
    try {
      setLoading(true);
      const { error } = await supabase.auth.signInWithPassword({ email: data.email, password: data.password });
      if (error) throw error;
      navigate('/admin/dashboard');
    } catch (e: any) {
      alert(e.message || 'Échec de la connexion');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen flex items-center justify-center bg-navy-900">
      <div className="w-full max-w-md p-8 rounded-2xl border border-steel-700/50 bg-navy-800/30">
        <h1 className="text-2xl font-extrabold text-white text-center mb-8">{t('admin.login')}</h1>
        <form onSubmit={handleSubmit(onSubmit)} className="space-y-4">
          <div className="mb-4">
            <Input {...register('email')} type="email" placeholder="Email" />
            {errors.email && <p className="text-red-400 text-sm mt-1">{errors.email.message}</p>}
          </div>
          <div className="mb-6">
            <Input {...register('password')} type="password" placeholder="Mot de passe" />
            {errors.password && <p className="text-red-400 text-sm mt-1">{errors.password.message}</p>}
          </div>
          <Button type="submit" className="w-full" disabled={loading}>
            {loading && <Loader className="w-4 h-4 animate-spin mr-2" />}
            {t('admin.signIn')}
          </Button>
        </form>
        <p className="mt-6 text-xs text-steel-400 text-center">Vitrine : <NavLink to="/" className="text-accent hover:underline">www.alfa-constructions.Netlify.com</NavLink></p>
      </div>
    </div>
  );
}
"""

dashboard = """import { useI18n } from '@/contexts/I18nContext';
import { useSupabase } from '@/contexts/SupabaseProvider';
import { useEffect, useState } from 'react';
import { Card, CardHeader, CardTitle, CardContent } from '@/components/ui/card';
import { Badge } from '@/components/ui/input';
import { Button } from '@/components/ui/button';
import { Link } from 'react-router-dom';
import { FileText, Folder, Mail, MessageSquare, Users, Calendar } from 'lucide-react';

export function Dashboard() {
  const { t } = useI18n();
  const { supabase, initialized } = useSupabase();
  const [stats, setStats] = useState({
    publishedProjects: 0, draftProjects: 0, totalServices: 0, newMessages: 0, pendingQuotes: 0,
    recentProjects: [] as Array<{ id: string; title: string; updated_at: string; status: string }>,
  });
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    if (!initialized) return;
    const fetchData = async () => {
      try {
        const [projRes, svcRes, msgRes, quoteRes] = await Promise.all([
          supabase!.from('projects').select('*', { count: 'exact' }).eq('status', 'published'),
          supabase!.from('services').select('*', { count: 'exact' }),
          supabase!.from('contact_messages').select('*', { count: 'exact' }).eq('status', 'new').limit(5),
          supabase!.from('quotation_requests').select('*', { count: 'exact' }).or('status.eq.new,status.eq.pending').limit(5),
        ]);
        const draftCount = (projRes.data ?? []).filter((d: { status: string }) => d.status === 'draft').length;
        const { data: recent } = await supabase!.from('projects').select('id, title, updated_at, status').eq('status', 'published').order('updated_at', { ascending: false }).limit(5);
        setStats({
          publishedProjects: projRes.count ?? 0, draftProjects: draftCount,
          totalServices: svcRes.count ?? 0, newMessages: msgRes.count ?? 0,
          pendingQuotes: quoteRes.count ?? 0, recentProjects: recent ?? [],
        });
      } catch (e) {}
      setLoading(false);
    };
    fetchData();
  }, [initialized, supabase]);

  if (loading) return <div className="min-h-screen flex items-center justify-center"><p>{t('shared.loading')}</p></div>;

  return (
    <div className="max-w-6xl mx-auto">
      <div className="text-center mb-8">
        <h1 className="text-2xl sm:text-3xl font-extrabold text-white">{t('admin.dashboard')}</h1>
        <p className="text-sm text-steel-300 mt-1">{t('admin.overview')}</p>
      </div>
      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4 mb-8">
        <Card><CardContent className="p-5"><div className="flex items-center gap-4"><div className="flex-shrink-0 h-12 w-12 rounded-xl bg-steel-700/50 flex items-center justify-center"><Folder className="w-6 h-6 text-accent" /></div><div><p className="text-2xl font-extrabold text-white">{stats.publishedProjects}</p><p className="text-xs text-steel-300">Projets publiés</p></div></div></CardContent></Card>
        <Card><CardContent className="p-5"><div className="flex items-center gap-4"><div className="flex-shrink-0 h-12 w-12 rounded-xl bg-steel-700/50 flex items-center justify-center"><FileText className="w-6 h-6 text-amber-300" /></div><div><p className="text-2xl font-extrabold text-white">{stats.draftProjects}</p><p className="text-xs text-steel-300">Brouillons</p></div></div></CardContent></Card>
        <Card><CardContent className="p-5"><div className="flex items-center gap-4"><div className="flex-shrink-0 h-12 w-12 rounded-xl bg-steel-700/50 flex items-center justify-center"><MessageSquare className="w-6 h-6 text-blue-300" /></div><div><p className="text-2xl font-extrabold text-white">{stats.newMessages}</p><p className="text-xs text-steel-300">Messages</p></div></div></CardContent></Card>
        <Card><CardContent className="p-5"><div className="flex items-center gap-4"><div className="flex-shrink-0 h-12 w-12 rounded-xl bg-steel-700/50 flex items-center justify-center"><Users className="w-6 h-6 text-purple-300" /></div><div><p className="text-2xl font-extrabold text-white">{stats.totalServices}</p><p className="text-xs text-steel-300">Services</p></div></div></CardContent></Card>
        <Card><CardContent className="p-5"><div className="flex items-center gap-4"><div className="flex-shrink-0 h-12 w-12 rounded-xl bg-steel-700/50 flex items-center justify-center"><Calendar className="w-6 h-6 text-green-300" /></div><div><p className="text-2xl font-extrabold text-white">{stats.pendingQuotes}</p><p className="text-xs text-steel-300">Devis en attente</p></div></div></CardContent></Card>
        <Card><CardContent className="p-5"><div className="flex items-center gap-4"><div className="flex-shrink-0 h-12 w-12 rounded-xl bg-steel-700/50 flex items-center justify-center"><Mail className="w-6 h-6 text-steel-400" /></div><div><Link to="/admin/messages"><p className="text-2xl font-extrabold text-white">Nouveaux</p><p className="text-xs text-steel-300">Messages</p></Link></div></div></CardContent></Card>
      </div>
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
        <Card><CardHeader><CardTitle>Projets récents</CardTitle></CardHeader><CardContent className="space-y-3">{stats.recentProjects.map((p) => <div key={p.id} className="flex items-center justify-between p-3 rounded-lg bg-navy-800/40"><p className="font-semibold text-white text-sm">{p.title}</p><Badge variant="success">{p.status}</Badge></div>)}</CardContent></Card>
        <Card><CardHeader><CardTitle>Actions rapides</CardTitle></CardHeader><CardContent className="space-y-2"><Button variant="ghost" className="w-full justify-start" asChild><Link to="/admin/projects">Gérer les projets</Link></Button><Button variant="ghost" className="w-full justify-start" asChild><Link to="/admin/services">Gérer les services</Link></Button><Button variant="ghost" className="w-full justify-start" asChild><Link to="/admin/media">Médias</Link></Button><Button variant="ghost" className="w-full justify-start" asChild><Link to="/admin/messages">Messages</Link></Button><Button variant="ghost" className="w-full justify-start" asChild><Link to="/admin/quotes">Devis</Link></Button><Button variant="ghost" className="w-full justify-start" asChild><Link to="/admin/settings">Paramètres</Link></Button></CardContent></Card>
      </div>
    </div>
  );
}
"""

projects_admin = """import { useI18n } from '@/contexts/I18nContext';
import { useSupabase } from '@/contexts/SupabaseProvider';
import { useEffect, useState } from 'react';
import { Card, CardHeader, CardTitle, CardContent } from '@/components/ui/card';
import { Badge } from '@/components/ui/input';
import { Button } from '@/components/ui/button';
import { Input } from '@/components/ui/input';
import { Plus, Edit, Trash2, Save, X } from 'lucide-react';
import { useNavigate } from 'react-router-dom';

export function ProjectsAdmin() {
  const { t } = useI18n();
  const { supabase: supabase_client, initialized } = useSupabase();
  const navigate = useNavigate();
  const [projects, setProjects] = useState<Array<any>>([]);
  const [loading, setLoading] = useState(true);
  const [editing, setEditing] = useState<string | null>(null);
  const [form, setForm] = useState({ title: '', slug: '', category_id: 'batiments', description: '', status: 'published' as const, cover_path: '' });

  useEffect(() => {
    if (!initialized) return;
    supabase_client!.from('projects').select('*').order('updated_at', { ascending: false })
      .then(({ data }) => setProjects(data ?? []))
      .catch(() => {})
      .finally(() => setLoading(false));
  }, [initialized, supabase_client]);

  if (loading) return <div className="min-h-screen flex items-center justify-center"><p>{t('shared.loading')}</p></div>;

  const save = async () => {
    try {
      if (editing) {
        await supabase_client!.from('projects').update({ ...form, updated_at: new Date().toISOString() }).eq('id', editing);
      } else {
        await supabase_client!.from('projects').insert({ ...form, slug: form.slug || form.title?.toLowerCase().replace(/[\\s\\u0000-\\u001F]+/g, '-'), created_at: new Date().toISOString(), updated_at: new Date().toISOString() });
      }
      setEditing(null);
      setForm({ title: '', slug: '', category_id: 'batiments', description: '', status: 'published' });
      await fetchProjects();
    } catch (e: any) { alert(e.message); }
  };

  const fetchProjects = async () => {
    const { data } = await supabase_client!.from('projects').select('*').order('updated_at', { ascending: false });
    setProjects(data ?? []);
  };

  const deleteProject = async (id: string) => {
    if (!confirm('Supprimer ce projet ?')) return;
    await supabase_client!.from('projects').delete().eq('id', id);
    await fetchProjects();
  };

  return (
    <div className="space-y-6">
      <div className="flex items-center justify-between">
        <h2 className="text-xl font-bold text-white">{t('admin.projects')}</h2>
        <Button onClick={() => setEditing('new')} className="gap-2"><Plus className="w-4 h-4" /> {t('shared.new')}</Button>
      </div>
      <div className="grid grid-cols-1 gap-4">
        {projects.map((p: any) => (
          <Card key={p.id}>
            <CardContent className="p-4">
              <div className="flex items-start justify-between gap-4">
                <div className="flex-1">
                  {editing === p.id ? (
                    <div className="space-y-3">
                      <Input value={form.title} onChange={(e) => setForm({ ...form, title: e.target.value })} className="font-normal" placeholder={t('admin.title')} />
                      <Input value={form.slug} onChange={(e) => setForm({ ...form, slug: e.target.value })} className="font-normal" placeholder={t('admin.slug')} />
                      <select value={form.category_id} onChange={(e) => setForm({ ...form, category_id: e.target.value })} className="w-full px-3 py-2 rounded-lg border border-steel-600 bg-navy-700 text-white">
                        <option value="batiments">Bâtiment</option><option value="travaux-publics">Travaux Publics</option><option value="transport">Transport</option><option value="carrieres">Carrières</option><option value="bureaude">Bureau d'Etude</option>
                      </select>
                      <textarea value={form.description} onChange={(e) => setForm({ ...form, description: e.target.value })} rows={4} className="w-full px-3 py-2 rounded-lg border border-steel-600 bg-navy-700 text-white" placeholder={t('admin.description')} />
                      <select value={form.status} onChange={(e) => setForm({ ...form, status: e.target.value as any })} className="w-full px-3 py-2 rounded-lg border border-steel-600 bg-navy-700 text-white">
                        <option value="draft">{t('admin.draft')}</option><option value="published">{t('admin.published')}</option>
                      </select>
                      <div className="flex gap-2"><Button onClick={() => { save(); setEditing(null); }}><Save className="w-4 h-4" /></Button><Button variant="ghost" onClick={() => setEditing(null)}><X className="w-4 h-4" /></Button></div>
                    </div>
                  ) : (
                    <div className="flex items-center justify-between">
                      <div><h3 className="font-bold text-white text-lg">{p.title}</h3><p className="text-sm text-steel-400">{p.location || ''}</p></div>
                      <div className="flex gap-2">
                        <Button variant="ghost" size="sm" onClick={() => { setEditing(p.id); setForm({ title: p.title, slug: p.slug || '', category_id: p.category_id || 'batiments', description: p.description || '', status: p.status, cover_path: '' }); }}><Edit className="w-4 h-4" /></Button>
                        <Button variant="ghost" size="sm" className="text-red-400" onClick={() => deleteProject(p.id)}><Trash2 className="w-4 h-4" /></Button>
                      </div>
                    </div>
                  )}
                </div>
              </div>
            </CardContent>
          </Card>
        ))}
        {projects.length === 0 && <p className="text-steel-400 col-span-full">{t('shared.noneFound')}</p>}
      </div>
    </div>
  );
}
"""

services_admin = """import { useI18n } from '@/contexts/I18nContext';
import { useSupabase } from '@/contexts/SupabaseProvider';
import { useEffect, useState } from 'react';
import { Card, CardHeader, CardTitle, CardContent } from '@/components/ui/card';
import { Badge } from '@/components/ui/input';
import { Button } from '@/components/ui/button';
import { Input } from '@/components/ui/input';
import { Plus, Edit, Trash2, Save, X } from 'lucide-react';
import { useNavigate } from 'react-router-dom';

export function ServicesAdmin() {
  const { t } = useI18n();
  const { supabase: supabase_client, initialized } = useSupabase();
  const [services, setServices] = useState<Array<any>>([]);
  const [loading, setLoading] = useState(true);
  const [editing, setEditing] = useState<string | null>(null);
  const [form, setForm] = useState({ title: '', slug: '', description: '', status: 'published' as const, image_path: '' });

  useEffect(() => {
    if (!initialized) return;
    supabase_client!.from('services').select('*').order('display_order')
      .then(({ data }) => setServices(data ?? []))
      .catch(() => {})
      .finally(() => setLoading(false));
  }, [initialized, supabase_client]);

  if (loading) return <div className="min-h-screen flex items-center justify-center"><p>{t('shared.loading')}</p></div>;

  const save = async () => {
    try {
      if (editing) {
        await supabase_client!.from('services').update({ ...form, updated_at: new Date().toISOString() }).eq('id', editing);
      } else {
        await supabase_client!.from('services').insert({ ...form, slug: form.slug || form.title?.toLowerCase().replace(/[\\s\\u0000-\\u001F]+/g, '-'), created_at: new Date().toISOString(), updated_at: new Date().toISOString() });
      }
      setEditing(null);
      setForm({ title: '', slug: '', description: '', status: 'published' });
      await fetchServices();
    } catch (e: any) { alert(e.message); }
  };

  const fetchServices = async () => {
    const { data } = await supabase_client!.from('services').select('*').order('display_order');
    setServices(data ?? []);
  };

  const deleteService = async (id: string) => {
    if (!confirm('Supprimer ce service ?')) return;
    await supabase_client!.from('services').delete().eq('id', id);
    await fetchServices();
  };

  return (
    <div className="space-y-6">
      <div className="flex items-center justify-between">
        <h2 className="text-xl font-bold text-white">{t('admin.services')}</h2>
        <Button onClick={() => setEditing('new')} className="gap-2"><Plus className="w-4 h-4" /> {t('shared.new')}</Button>
      </div>
      <div className="grid grid-cols-1 gap-4">
        {services.map((s: any) => (
          <Card key={s.id}>
            <CardContent className="p-4">
              <div className="flex items-start justify-between gap-4">
                <div className="flex-1">
                  {editing === s.id ? (
                    <div className="space-y-3">
                      <Input value={form.title} onChange={(e) => setForm({ ...form, title: e.target.value })} placeholder={t('admin.title')} />
                      <Input value={form.slug} onChange={(e) => setForm({ ...form, slug: e.target.value })} className="font-normal" placeholder={t('admin.slug')} />
                      <textarea value={form.description} onChange={(e) => setForm({ ...form, description: e.target.value })} rows={4} className="w-full px-3 py-2 rounded-lg border border-steel-600 bg-navy-700 text-white" placeholder={t('admin.description')} />
                      <select value={form.status} onChange={(e) => setForm({ ...form, status: e.target.value as any })} className="w-full px-3 py-2 rounded-lg border border-steel-600 bg-navy-700 text-white">
                        <option value="draft">{t('admin.draft')}</option><option value="published">{t('admin.published')}</option>
                      </select>
                      <div className="flex gap-2"><Button onClick={() => { save(); setEditing(null); }}><Save className="w-4 h-4" /></Button><Button variant="ghost" onClick={() => setEditing(null)}><X className="w-4 h-4" /></Button></div>
                    </div>
                  ) : (
                    <div className="flex items-center justify-between">
                      <div><h3 className="font-bold text-white text-lg">{s.title}</h3><p className="text-sm text-steel-400">{s.description}</p></div>
                      <div className="flex gap-2">
                        <Button variant="ghost" size="sm" onClick={() => { setEditing(s.id); setForm({ title: s.title, slug: s.slug || '', description: s.description || '', status: s.status, image_path: '' }); }}><Edit className="w-4 h-4" /></Button>
                        <Button variant="ghost" size="sm" className="text-red-400" onClick={() => deleteService(s.id)}><Trash2 className="w-4 h-4" /></Button>
                      </div>
                    </div>
                  )}
                </div>
              </div>
            </CardContent>
          </Card>
        ))}
        {services.length === 0 && <p className="text-steel-400 col-span-full">{t('shared.noneFound')}</p>}
      </div>
    </div>
  );
}
"""

media = """import { useI18n } from '@/contexts/I18nContext';
import { useSupabase } from '@/contexts/SupabaseProvider';
import { useEffect, useState } from 'react';
import { Card, CardHeader, CardTitle, CardContent } from '@/components/ui/card';
import { Button } from '@/components/ui/button';
import { Input } from '@/components/ui/input';
import { Label } from '@/components/ui/input';
import { Image as FileImage, Trash2, Upload, Edit, Save, X } from 'lucide-react';

export function MediaAdmin() {
  const { t } = useI18n();
  const { supabase: supabase_client, initialized } = useSupabase();
  const [media, setMedia] = useState<Array<any>>([]);
  const [loading, setLoading] = useState(true);
  const [editing, setEditing] = useState<string | null>(null);
  const [form, setForm] = useState({ caption: '', alt_text: '', storage_path: '', project_id: '', is_public: true });

  useEffect(() => {
    if (!initialized) return;
    supabase_client!.from('media').select('*').order('created_at', { ascending: false })
      .then(({ data }) => setMedia(data ?? []))
      .catch(() => {})
      .finally(() => setLoading(false));
  }, [initialized, supabase_client]);

  if (loading) return <div className="min-h-screen flex items-center justify-center"><p>{t('shared.loading')}</p></div>;

  const saveMedia = async () => {
    try {
      if (editing) {
        await supabase_client!.from('media').update({ ...form, updated_at: new Date().toISOString() }).eq('id', editing);
      } else {
        await supabase_client!.from('media').insert({ ...form, created_at: new Date().toISOString(), updated_at: new Date().toISOString() });
      }
      setEditing(null);
      setForm({ caption: '', alt_text: '', storage_path: '', project_id: '', is_public: true });
      await fetchMedia();
    } catch (e: any) { alert(e.message); }
  };

  const fetchMedia = async () => {
    const { data } = await supabase_client!.from('media').select('*').order('created_at', { ascending: false });
    setMedia(data ?? []);
  };

  const deleteMedia = async (id: string) => {
    if (confirm('Supprimer ?')) {
      await supabase_client!.from('media').delete().eq('id', id);
      await fetchMedia();
    }
  };

  return (
    <div className="space-y-6">
      <div className="flex items-center justify-between">
        <h2 className="text-xl font-bold text-white">{t('admin.media')}</h2>
        <Button onClick={() => setEditing('new')} className="gap-2"><Upload className="w-4 h-4" /> {t('shared.new')}</Button>
      </div>
      <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
        {media.map((m: any) => (
          <Card key={m.id}>
            <CardContent className="p-4">
              <div className="flex items-start gap-4">
                <div className="flex-shrink-0 h-20 w-20 rounded-lg bg-steel-700/30 flex items-center justify-center">
                  {m.storage_path ? <img src={m.storage_path} alt={m.alt_text || ''} className="w-full h-full object-cover" /> : <FileImage className="w-6 h-6 text-steel-400" />}
                </div>
                <div className="flex-1 min-w-0">
                  {editing === m.id ? (
                    <div className="space-y-3">
                      <Input value={form.caption} onChange={(e) => setForm({ ...form, caption: e.target.value })} placeholder="Caption" />
                      <Input value={form.alt_text} onChange={(e) => setForm({ ...form, alt_text: e.target.value })} placeholder="Alt text" />
                      <Input value={form.storage_path} onChange={(e) => setForm({ ...form, storage_path: e.target.value })} placeholder="Path" />
                      <Input value={form.project_id} onChange={(e) => setForm({ ...form, project_id: e.target.value })} placeholder="Project" />
                      <div className="flex gap-2">
                        <Button onClick={() => { saveMedia(); setEditing(null); }}><Save className="w-4 h-4" /></Button>
                        <Button variant="ghost" onClick={() => setEditing(null)}><X className="w-4 h-4" /></Button>
                      </div>
                    </div>
                  ) : (
                    <div className="flex items-center justify-between">
                      <h3 className="font-semibold text-white truncate">{m.caption || m.storage_path?.split('/').pop()}</h3>
                      <div className="flex gap-2">
                        <Button variant="ghost" size="sm" onClick={() => { setEditing(m.id); setForm({ caption: m.caption || '', alt_text: m.alt_text || '', storage_path: m.storage_path || '', project_id: m.project_id || '', is_public: m.is_public }); }}><Edit className="w-4 h-4" /></Button>
                        <Button variant="ghost" size="sm" className="text-red-400" onClick={() => deleteMedia(m.id)}><Trash2 className="w-4 h-4" /></Button>
                      </div>
                    </div>
                  )}
                </div>
              </div>
            </CardContent>
          </Card>
        ))}
        {media.length === 0 && <p className="text-steel-400 col-span-2">{t('shared.noneFound')}</p>}
      </div>
    </div>
  );
}
"""

messages = """import { useI18n } from '@/contexts/I18nContext';
import { useSupabase } from '@/contexts/SupabaseProvider';
import { useEffect, useState } from 'react';
import { Card, CardHeader, CardTitle, CardContent } from '@/components/ui/card';
import { Badge } from '@/components/ui/input';
import { Button } from '@/components/ui/button';
import { Input } from '@/components/ui/input';
import { Send, Trash2 } from 'lucide-react';

export function MessagesAdmin() {
  const { t } = useI18n();
  const { supabase: supabase_client, initialized } = useSupabase();
  const [messages, setMessages] = useState<Array<any>>([]);
  const [loading, setLoading] = useState(true);
  const [form, setForm] = useState({ status: 'new' as const, note: '' });
  const [notes, setNotes] = useState<Record<string, string>>({});

  useEffect(() => {
    if (!initialized) return;
    supabase_client!.from('contact_messages').select('*').order('created_at', { ascending: false })
      .then(({ data }) => setMessages(data ?? []))
      .catch(() => {})
      .finally(() => setLoading(false));
  }, [initialized, supabase_client]);

  if (loading) return <div className="min-h-screen flex items-center justify-center"><p>{t('shared.loading')}</p></div>;

  const updateStatus = async (id: string, status: string) => {
    await supabase_client!.from('contact_messages').update({ status, updated_at: new Date().toISOString() }).eq('id', id);
    await fetchMessages();
  };

  const fetchMessages = async () => {
    const { data } = await supabase_client!.from('contact_messages').select('*').order('created_at', { ascending: false });
    setMessages(data ?? []);
  };

  const addNote = async (id: string) => {
    if (!form.note.trim()) return;
    const note = notes[id] ? notes[id] + '\n' + form.note : form.note;
    await supabase_client!.from('audit_logs').insert({ action: 'note_created', entity_type: 'contact_messages', entity_id: id, details: note });
    await supabase_client!.from('contact_messages').update({ notes: note, updated_at: new Date().toISOString() }).eq('id', id);
    setNotes({ ...notes, [id]: note });
    setForm({ status: 'new', note: '' });
    await fetchMessages();
  };

  return (
    <div className="space-y-6">
      <h2 className="text-xl font-bold text-white">{t('admin.contactMessages')}</h2>
      <div className="grid grid-cols-1 gap-4">
        {messages.map((m: any) => (
          <Card key={m.id}>
            <CardContent className="p-5">
              <div className="flex items-start justify-between gap-4">
                <div className="flex-1">
                  <div className="flex items-center gap-3 flex-wrap">
                    <h3 className="font-bold text-white">{m.name}</h3>
                    <Badge variant={m.status === 'new' ? 'default' : m.status === 'pending' ? 'warning' : m.status === 'read' ? 'success' : 'outline'}>{m.status === 'new' ? 'Nouveau' : m.status === 'pending' ? 'En attente' : m.status === 'read' ? 'Lu' : m.status === 'archived' ? 'Archivé' : 'Traité'}</Badge>
                  </div>
                  <p className="text-sm text-steel-300 mt-1">{m.email} {m.phone ? `<br>${m.phone}` : ''}</p>
                  <p className="text-sm text-steel-300 mt-1"><span className="font-medium">Sujet:</span> {m.subject}</p>
                  <p className="text-sm text-steel-300 mt-1 line-clamp-3">{m.message}</p>
                  {m.notes && <div className="mt-3 p-3 rounded-lg bg-steel-700/40 text-xs text-steel-300 leading-relaxed">{m.notes}</div>}
                  <div className="flex gap-2 mt-3">
                    <select value={form.status} onChange={(e) => setForm({ ...form, status: e.target.value as any })} className="px-3 py-1.5 rounded-lg border border-steel-600 bg-navy-700 text-white text-sm">
                      <option value="new">Nouveau</option><option value="pending">En attente</option><option value="read">Lu</option><option value="archived">Archivé</option><option value="treate">Traité</option>
                    </select>
                    <Button size="sm" className="gap-1" onClick={() => addNote(m.id)}><Send className="w-3 h-3" /> Note</Button>
                  </div>
                </div>
              </div>
            </CardContent>
          </Card>
        ))}
        {messages.length === 0 && <p className="text-steel-400 col-span-full">{t('shared.noneFound')}</p>}
      </div>
    </div>
  );
}
"""

quotes = """import { useI18n } from '@/contexts/I18nContext';
import { useSupabase } from '@/contexts/SupabaseProvider';
import { useEffect, useState } from 'react';
import { Card, CardHeader, CardTitle, CardContent } from '@/components/ui/card';
import { Badge } from '@/components/ui/input';
import { Button } from '@/components/ui/button';
import { Trash2, Send, User, Building, Phone, MapPin, Calendar, FileText } from 'lucide-react';

export function QuotesAdmin() {
  const { t } = useI18n();
  const { supabase: supabase_client, initialized } = useSupabase();
  const [quotes, setQuotes] = useState<Array<any>>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    if (!initialized) return;
    supabase_client!.from('quotation_requests').select('*').order('created_at', { ascending: false })
      .then(({ data }) => setQuotes(data ?? []))
      .catch(() => {})
      .finally(() => setLoading(false));
  }, [initialized, supabase_client]);

  if (loading) return <div className="min-h-screen flex items-center justify-center"><p>{t('shared.loading')}</p></div>;

  const updateStatus = async (id: string, status: string) => {
    await supabase_client!.from('quotation_requests').update({ status, updated_at: new Date().toISOString() }).eq('id', id);
    await fetchQuotes();
  };

  const fetchQuotes = async () => {
    const { data } = await supabase_client!.from('quotation_requests').select('*').order('created_at', { ascending: false });
    setQuotes(data ?? []);
  };

  return (
    <div className="space-y-6">
      <h2 className="text-xl font-bold text-white">{t('admin.quotationRequests')}</h2>
      <div className="grid grid-cols-1 gap-4">
        {quotes.map((q: any) => (
          <Card key={q.id}>
            <CardContent className="p-5">
              <div className="flex items-start justify-between gap-4">
                <div className="flex-1">
                  <div className="flex items-center gap-3 flex-wrap">
                    <h3 className="font-bold text-white">{q.name}</h3>
                    <Badge variant="default">{q.status}</Badge>
                  </div>
                  <p className="text-sm text-steel-300 mt-1">{q.email} {q.phone ? `<br>${q.phone}` : ''}</p>
                  <p className="text-sm text-steel-300 mt-1"><span className="font-medium">Lieu:</span> {q.project_location}</p>
                  <p className="text-sm text-steel-300 mt-1 line-clamp-2">{q.project_description}</p>
                  <div className="flex gap-2 mt-3 flex-wrap">
                    <select value={q.status} onChange={(e) => updateStatus(q.id, e.target.value as any)} className="px-3 py-1.5 rounded-lg border border-steel-600 bg-navy-700 text-white text-sm">
                      <option value="new">Nouveau</option><option value="pending">En attente</option><option value="read">Lu</option><option value="treate">Traité</option><option value="archived">Archivé</option>
                    </select>
                  </div>
                </div>
              </div>
            </CardContent>
          </Card>
        ))}
        {quotes.length === 0 && <p className="text-steel-400 col-span-full">{t('shared.noneFound')}</p>}
      </div>
    </div>
  );
}
"""

settings = """import { useI18n } from '@/contexts/I18nContext';
import { useSupabase } from '@/contexts/SupabaseProvider';
import { useEffect, useState } from 'react';
import { Card, CardHeader, CardTitle, CardContent } from '@/components/ui/card';
import { Button } from '@/components/ui/button';
import { Input } from '@/components/ui/input';
import { Label } from '@/components/ui/input';
import { Save, X } from 'lucide-react';

export function SettingsPage() {
  const { t } = useI18n();
  const { supabase: supabase_client, initialized } = useSupabase();
  const [form, setForm] = useState({
    site_name: 'ALFA CONSTRUCTION', about: '', logo: '', contact_email: 'ali-safa@alfa-constructions.com',
    phone: '+242 06 822 22 20', address: 'Avenue Docteur Cardorelle, Songolo, Congo', website: 'www.alfa-constructions.Netlify.com',
    footer: '', hours: 'Lun - Ven : 08h00 - 18h00',
  });
  const [saving, setSaving] = useState(false);

  useEffect(() => {
    if (!initialized) return;
    supabase_client!.from('site_settings').select('*').eq('key', 'site_settings')
      .then(({ data }) => { if (data && data.length) setForm({ ...form, ...JSON.parse(data[0].value) }); })
      .catch(() => {});
  }, [initialized, supabase_client]);

  const saveSettings = async () => {
    try {
      setSaving(true);
      const { data } = await supabase_client!.from('site_settings').select('*').eq('key', 'site_settings').single();
      if (data) {
        await supabase_client!.from('site_settings').update({ value: JSON.stringify(form), updated_at: new Date().toISOString() }).eq('id', data.id);
      } else {
        await supabase_client!.from('site_settings').insert({ key: 'site_settings', value: JSON.stringify(form), created_at: new Date().toISOString(), updated_at: new Date().toISOString() });
      }
      alert('Sauvegardé!');
    } catch (e: any) { alert(e.message); }
    setSaving(false);
  };

  return (
    <div className="max-w-3xl space-y-6">
      <h2 className="text-xl font-bold text-white">{t('admin.settingsTitle')}</h2>
      <div className="grid grid-cols-1 gap-6">
        <Card>
          <CardHeader><CardTitle>Informations de base</CardTitle></CardHeader>
          <CardContent className="space-y-4">
            <Input value={form.site_name} onChange={(e) => setForm({ ...form, site_name: e.target.value })} placeholder="Nom du site" />
            <Input value={form.contact_email} onChange={(e) => setForm({ ...form, contact_email: e.target.value })} placeholder="Email contact" />
            <Input value={form.phone} onChange={(e) => setForm({ ...form, phone: e.target.value })} placeholder="Téléphone" />
            <Input value={form.address} onChange={(e) => setForm({ ...form, address: e.target.value })} placeholder="Adresse" />
            <Input value={form.website} onChange={(e) => setForm({ ...form, website: e.target.value })} placeholder="Site Web" />
            <div className="flex gap-2">
              <Button onClick={saveSettings} disabled={saving}><Save className="w-4 h-4" /> {t('admin.save')}</Button>
              <Button variant="ghost" onClick={() => setForm({ ...form })}><X className="w-4 h-4" /></Button>
            </div>
          </CardContent>
        </Card>
        <Card>
          <CardHeader><CardTitle>Homepage</CardTitle></CardHeader>
          <CardContent>
            <textarea value={form.about} onChange={(e) => setForm({ ...form, about: e.target.value })} rows={6} className="w-full px-3 py-2 rounded-lg border border-steel-600 bg-navy-700 text-white" placeholder="Contenu d'accueil" />
          </CardContent>
        </Card>
        <Card>
          <CardHeader><CardTitle>Footer</CardTitle></CardHeader>
          <CardContent>
            <textarea value={form.footer} onChange={(e) => setForm({ ...form, footer: e.target.value })} rows={4} className="w-full px-3 py-2 rounded-lg border border-steel-600 bg-navy-700 text-white" placeholder="Pied de page" />
          </CardContent>
        </Card>
      </div>
    </div>
  );
}
"""

with open('client/src/pages/admin/AdminLayout.tsx', 'w') as f:
    f.write(admin_layout)
with open('client/src/pages/admin/LoginPage.tsx', 'w') as f:
    f.write(login)
with open('client/src/pages/admin/Dashboard.tsx', 'w') as f:
    f.write(dashboard)
with open('client/src/pages/admin/ProjectsAdmin.tsx', 'w') as f:
    f.write(projects_admin)
with open('client/src/pages/admin/ServicesAdmin.tsx', 'w') as f:
    f.write(services_admin)
with open('client/src/pages/admin/MediaAdmin.tsx', 'w') as f:
    f.write(media)
with open('client/src/pages/admin/MessagesAdmin.tsx', 'w') as f:
    f.write(messages)
with open('client/src/pages/admin/QuotesAdmin.tsx', 'w') as f:
    f.write(quotes)
with open('client/src/pages/admin/SettingsPage.tsx', 'w') as f:
    f.write(settings)

print("Admin pages created")
