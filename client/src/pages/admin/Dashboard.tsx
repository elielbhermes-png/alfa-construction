import { useI18n } from '@/contexts/I18nContext';
import { useSupabase } from '@/contexts/SupabaseProvider';
import { useEffect, useState } from 'react';
import { Card, CardHeader, CardTitle, CardContent } from '@/components/ui/card';
import { Badge } from '@/components/ui';
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
