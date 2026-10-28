import { useI18n } from '@/contexts/I18nContext';
import { useSupabase } from '@/contexts/SupabaseProvider';
import { useEffect, useState } from 'react';
import { Card, CardHeader, CardTitle, CardContent } from '@/components/ui/card';
import { Badge } from '@/components/ui';
import { Button } from '@/components/ui/button';
import { Input } from '@/components/ui';
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
      .then(({ data }) => { setServices(data ?? []); setLoading(false); })
      
  }, [initialized, supabase_client]);

  if (loading) return <div className="min-h-screen flex items-center justify-center"><p>{t('shared.loading')}</p></div>;

  const save = async () => {
    try {
      if (editing) {
        await supabase_client!.from('services').update({ ...form, updated_at: new Date().toISOString() }).eq('id', editing);
      } else {
        await supabase_client!.from('services').insert({ ...form, slug: form.slug || form.title?.toLowerCase().replace(/[\s\u0000-\u001F]+/g, '-'), created_at: new Date().toISOString(), updated_at: new Date().toISOString() });
      }
      setEditing(null);
      setForm({ title: '', slug: '', description: '', status: 'published', image_path: '' });
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
