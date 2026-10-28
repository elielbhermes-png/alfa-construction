import { useI18n } from '@/contexts/I18nContext';
import { useSupabase } from '@/contexts/SupabaseProvider';
import { useEffect, useState } from 'react';
import { Card, CardHeader, CardTitle, CardContent } from '@/components/ui/card';
import { Badge } from '@/components/ui';
import { Button } from '@/components/ui/button';
import { Input } from '@/components/ui';
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
      .then(({ data }) => { setProjects(data ?? []); setLoading(false); })
      
  }, [initialized, supabase_client]);

  if (loading) return <div className="min-h-screen flex items-center justify-center"><p>{t('shared.loading')}</p></div>;

  const save = async () => {
    try {
      if (editing) {
        await supabase_client!.from('projects').update({ ...form, updated_at: new Date().toISOString() }).eq('id', editing);
      } else {
        await supabase_client!.from('projects').insert({ ...form, slug: form.slug || form.title?.toLowerCase().replace(/[\s\u0000-\u001F]+/g, '-'), created_at: new Date().toISOString(), updated_at: new Date().toISOString() });
      }
      setEditing(null);
      setForm({ title: '', slug: '', category_id: 'batiments', description: '', status: 'published', cover_path: '' });
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
