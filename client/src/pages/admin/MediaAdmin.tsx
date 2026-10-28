import { useI18n } from '@/contexts/I18nContext';
import { useSupabase } from '@/contexts/SupabaseProvider';
import { useEffect, useState } from 'react';
import { Card, CardHeader, CardTitle, CardContent } from '@/components/ui/card';
import { Button } from '@/components/ui/button';
import { Input } from '@/components/ui';
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
      .then(({ data }) => { setMedia(data ?? []); setLoading(false); })
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
