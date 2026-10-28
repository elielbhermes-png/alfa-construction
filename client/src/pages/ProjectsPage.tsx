import { useI18n } from '@/contexts/I18nContext';
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
      .then(({ data }) => { setProjects(data ?? []); setLoading(false); });
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
