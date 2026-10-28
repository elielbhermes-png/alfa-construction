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
      .then(({ data }) => { setServices(data ?? []); setLoading(false); });
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
