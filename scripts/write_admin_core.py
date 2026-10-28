import os

os.makedirs('client/src/pages/admin', exist_ok=True)

# AdminLayout
admin_layout = """import { useEffect, useState } from 'react';
import { Outlet, Link, useNavigate } from 'react-router-dom';
import { useSupabase } from '@/contexts/SupabaseProvider';
import { useI18n } from '@/contexts/I18nContext';
import { Button } from '@/components/ui/button';
import { Badge } from '@/components/ui/input';
import { LayoutDashboard, FileText, Wrench, Image, MessageSquare, BarChart3, Settings, LogOut, Menu, X } from 'lucide-react';

export function AdminLayout() {
  const { t } = useI18n();
  const { supabase: supabaseClient, initialized } = useSupabase();
  const navigate = useNavigate();
  const [loading, setLoading] = useState(true);
  const [sideOpen, setSideOpen] = useState(false);

  useEffect(() => {
    if (!initialized) { setLoading(true); return; }
    supabaseClient?.auth.getUser()
      .then(({ data }) => {
        if (!data.user) { navigate('/admin/login'); }
      })
      .catch(() => navigate('/admin/login'))
      .finally(() => setLoading(false));
  }, [initialized, supabaseClient, navigate]);

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
            <Link to="/" onClick={() => supabaseClient?.auth.signOut()}><LogOut className="w-4 h-4 mr-3" />{t('admin.signOut')}</Link>
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

# LoginPage
login = """import { useState } from 'react';
import { NavLink, useNavigate } from 'react-router-dom';
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
  email: z.string().email(), password: z.string().min(1),
});
type LoginForm = z.infer<typeof loginSchema>;

export function LoginPage() {
  const { t } = useI18n();
  const { supabaseClient, initialized } = useSupabase();
  const navigate = useNavigate();
  const [loading, setLoading] = useState(true);

  const { register, handleSubmit, formState: { errors } } = useForm<LoginForm>({
    resolver: zodResolver(loginSchema), defaultValues: { email: '', password: '' },
  });

  if (!initialized || !supabaseClient) return <div className="min-h-screen flex items-center justify-center">{t('shared.loading')}</div>;

  const onSubmit = async (data: LoginForm) => {
    try {
      setLoading(true);
      const { error } = await supabaseClient.auth.signInWithPassword({ email: data.email, password: data.password });
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
            {loading && <Loader2 className="w-4 h-4 animate-spin mr-2" />}
            {t('admin.signIn')}
          </Button>
        </form>
        <p className="mt-6 text-xs text-steel-400 text-center">Vitrine : <NavLink to="/" className="text-accent hover:underline">www.alfa-constructions.Netlify.com</NavLink></p>
      </div>
    </div>
  );
}
"""

# Dashboard
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
  const { supabase: supabaseClient, initialized } = useSupabase();
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
          supabaseClient!.from('projects').select('*', { count: 'exact' }).eq('status', 'published'),
          supabaseClient!.from('services').select('*', { count: 'exact' }),
          supabaseClient!.from('contact_messages').select('*', { count: 'exact' }).eq('status', 'new').limit(5),
          supabaseClient!.from('quotation_requests').select('*', { count: 'exact' }).or('status.eq.new,status.eq.pending').limit(5),
        ]);
        const draftCount = (projRes.data ?? []).filter((d: { status: string }) => d.status === 'draft').length;
        const { data: recent } = await supabaseClient!.from('projects').select('id, title, updated_at, status').eq('status', 'published').order('updated_at', { ascending: false }).limit(5);
        setStats({
          publishedProjects: projRes.count ?? 0, draftProjects: draftCount,
          totalServices: svcRes.count ?? 0, newMessages: msgRes.count ?? 0,
          pendingQuotes: quoteRes.count ?? 0, recentProjects: recent ?? [],
        });
      } catch {}
      setLoading(false);
    };
    fetchData();
  }, [initialized, supabaseClient]);

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

with open('client/src/pages/admin/AdminLayout.tsx', 'w') as f:
    f.write(admin_layout)
with open('client/src/pages/admin/LoginPage.tsx', 'w') as f:
    f.write(login)
with open('client/src/pages/admin/Dashboard.tsx', 'w') as f:
    f.write(dashboard)

print("Login, Dashboard, AdminLayout written")
