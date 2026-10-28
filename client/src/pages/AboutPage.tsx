import { useI18n } from '@/contexts/I18nContext';
import { useSupabase } from '@/contexts/SupabaseProvider';
import { useEffect, useState } from 'react';
import { Building, Users, Shield, GraduationCap, Link, ArrowRight } from 'lucide-react';
import { Button } from '@/components/ui/button';

export function AboutPage() {
  const { t } = useI18n();
  const { supabase: supabaseClient, initialized } = useSupabase();
  const [aboutContent, setAboutContent] = useState<{ title: string; description: string } | null>(null);

  useEffect(() => {
    if (!initialized) return;
    supabaseClient?.from('site_settings').select('value').eq('key', 'about_content').single()
      .then(({ data }) => {
        if (data) {
          setAboutContent(JSON.parse(data.value));
        } else {
          setAboutContent({ title: t('about.title'), description: t('about.intro') });
        }
      });
  }, [initialized, supabaseClient]);

  return (
    <div className="py-16 sm:py-24 bg-navy-900/50 min-h-screen">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-10 items-center">
          <div>
            <p className="text-accent text-sm font-semibold mb-3">À propos</p>
            <h1 className="text-3xl sm:text-4xl md:text-5xl font-extrabold text-white leading-tight">{aboutContent?.title || t('about.title')}</h1>
                    <p className="text-steel-300 mt-4 text-lg leading-relaxed">{aboutContent?.description || t('about.intro')}</p>
            <div className="mt-8 flex flex-wrap gap-4">
              <Link to="/nos-realisations"><Button variant="ghost" className="text-white border-steel-600 hover:bg-white/5"><Building className="w-4 h-4 mr-2" />Projets</Button></Link>
              <Link to="/contactez-nous"><Button variant="outline" className="text-white border-steel-600 bg-white/5 hover:bg-white/10"><Users className="w-4 h-4 mr-2" />Notre équipe</Button></Link>
            </div>
          </div>
          <div className="grid grid-cols-2 gap-4">
            {[
              { icon: Building, title: 'Domaines', desc: "4 secteurs d'activité" },
              { icon: Users, title: 'Collectif', desc: "Alliance d'expertises" },
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
