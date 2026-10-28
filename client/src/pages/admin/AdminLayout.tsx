import { useEffect, useState } from 'react';
import { useNavigate, Link, Outlet } from 'react-router-dom';
import { useI18n } from '@/contexts/I18nContext';
import { useSupabase } from '@/contexts/SupabaseProvider';
import { Button } from '@/components/ui/button';
import { Badge } from '@/components/ui';
import { LayoutDashboard, FileText, Wrench, Image, MessageSquare, BarChart3, Settings, LogOut, Menu, X } from 'lucide-react';

export function AdminLayout() {
  const { t } = useI18n();
  const { supabase, initialized } = useSupabase();
  const navigate = useNavigate();
  const [loading, setLoading] = useState(true);
  const [sideOpen, setSideOpen] = useState(false);

  useEffect(() => {
    if (!initialized) { setLoading(true); return; }
    if (!supabase) return;
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
