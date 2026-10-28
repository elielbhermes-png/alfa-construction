import { useI18n } from '@/contexts/I18nContext';
import { useSupabase } from '@/contexts/SupabaseProvider';
import { useEffect, useState } from 'react';
import { Card, CardHeader, CardTitle, CardContent } from '@/components/ui/card';
import { Badge } from '@/components/ui';
import { Button } from '@/components/ui/button';
import { Input } from '@/components/ui';
import { Send, Trash2 } from 'lucide-react';

export function MessagesAdmin() {
  const { t } = useI18n();
  const { supabase: supabase_client, initialized } = useSupabase();
  const [messages, setMessages] = useState<Array<any>>([]);
  const [loading, setLoading] = useState(true);
  const [form, setForm] = useState({ status: 'new' as const, note: '' });
  const [notes, setNotes] = useState<Record<string, string>>({});

  useEffect(() => {
    if (!initialized) return;
    supabase_client!.from('contact_messages').select('*').order('created_at', { ascending: false })
      .then(({ data }) => { setMessages(data ?? []); setLoading(false); })
      
  }, [initialized, supabase_client]);

  if (loading) return <div className="min-h-screen flex items-center justify-center"><p>{t('shared.loading')}</p></div>;

  const updateStatus = async (id: string, status: string) => {
    await supabase_client!.from('contact_messages').update({ status, updated_at: new Date().toISOString() }).eq('id', id);
    await fetchMessages();
  };

  const fetchMessages = async () => {
    const { data } = await supabase_client!.from('contact_messages').select('*').order('created_at', { ascending: false });
    setMessages(data ?? []);
  };

  const addNote = async (id: string) => {
    if (!form.note.trim()) return;
    const note = notes[id] ? notes[id] + '\n' + form.note : form.note;
    await supabase_client!.from('audit_logs').insert({ action: 'note_created', entity_type: 'contact_messages', entity_id: id, details: note });
    await supabase_client!.from('contact_messages').update({ notes: note, updated_at: new Date().toISOString() }).eq('id', id);
    setNotes({ ...notes, [id]: note });
    setForm({ status: 'new', note: '' });
    await fetchMessages();
  };

  return (
    <div className="space-y-6">
      <h2 className="text-xl font-bold text-white">{t('admin.contactMessages')}</h2>
      <div className="grid grid-cols-1 gap-4">
        {messages.map((m: any) => (
          <Card key={m.id}>
            <CardContent className="p-5">
              <div className="flex items-start justify-between gap-4">
                <div className="flex-1">
                  <div className="flex items-center gap-3 flex-wrap">
                    <h3 className="font-bold text-white">{m.name}</h3>
                    <Badge variant={m.status === 'new' ? 'default' : m.status === 'pending' ? 'warning' : m.status === 'read' ? 'success' : 'outline'}>{m.status === 'new' ? 'Nouveau' : m.status === 'pending' ? 'En attente' : m.status === 'read' ? 'Lu' : m.status === 'archived' ? 'Archivé' : 'Traité'}</Badge>
                  </div>
                  <p className="text-sm text-steel-300 mt-1">{m.email} {m.phone ? '<br>' + m.phone : ''}</p>
                  <p className="text-sm text-steel-300 mt-1"><span className="font-medium">Sujet:</span> {m.subject}</p>
                  <p className="text-sm text-steel-300 mt-1 line-clamp-3">{m.message}</p>
                  {m.notes && <div className="mt-3 p-3 rounded-lg bg-steel-700/40 text-xs text-steel-300 leading-relaxed">{m.notes}</div>}
                  <div className="flex gap-2 mt-3">
                    <select value={form.status} onChange={(e) => setForm({ ...form, status: e.target.value as any })} className="px-3 py-1.5 rounded-lg border border-steel-600 bg-navy-700 text-white text-sm">
                      <option value="new">Nouveau</option><option value="pending">En attente</option><option value="read">Lu</option><option value="archived">Archivé</option><option value="treate">Traité</option>
                    </select>
                    <Button size="sm" className="gap-1" onClick={() => addNote(m.id)}><Send className="w-3 h-3" /> Note</Button>
                  </div>
                </div>
              </div>
            </CardContent>
          </Card>
        ))}
        {messages.length === 0 && <p className="text-steel-400 col-span-full">{t('shared.noneFound')}</p>}
      </div>
    </div>
  );
}
