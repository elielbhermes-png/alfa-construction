import { useParams, Link } from 'react-router-dom';
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
