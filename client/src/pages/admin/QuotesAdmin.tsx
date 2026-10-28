import { useI18n } from '@/contexts/I18nContext';
import { useSupabase } from '@/contexts/SupabaseProvider';
import { useEffect, useState } from 'react';
import { Card, CardHeader, CardTitle, CardContent } from '@/components/ui/card';
import { Badge } from '@/components/ui';
import { Button } from '@/components/ui/button';
import { Trash2, Send, User, Building, Phone, MapPin, Calendar, FileText } from 'lucide-react';

export function QuotesAdmin() {
  const { t } = useI18n();
  const { supabase: supabase_client, initialized } = useSupabase();
  const [quotes, setQuotes] = useState<Array<any>>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    if (!initialized) return;
    supabase_client!.from('quotation_requests').select('*').order('created_at', { ascending: false })
      .then(({ data }) => { setQuotes(data ?? []); setLoading(false); })
      
  }, [initialized, supabase_client]);

  if (loading) return <div className="min-h-screen flex items-center justify-center"><p>{t('shared.loading')}</p></div>;

  const updateStatus = async (id: string, status: string) => {
    await supabase_client!.from('quotation_requests').update({ status, updated_at: new Date().toISOString() }).eq('id', id);
    await fetchQuotes();
  };

  const fetchQuotes = async () => {
    const { data } = await supabase_client!.from('quotation_requests').select('*').order('created_at', { ascending: false });
    setQuotes(data ?? []);
  };

  return (
    <div className="space-y-6">
      <h2 className="text-xl font-bold text-white">{t('admin.quotationRequests')}</h2>
      <div className="grid grid-cols-1 gap-4">
        {quotes.map((q: any) => (
          <Card key={q.id}>
            <CardContent className="p-5">
              <div className="flex items-start justify-between gap-4">
                <div className="flex-1">
                  <div className="flex items-center gap-3 flex-wrap">
                    <h3 className="font-bold text-white">{q.name}</h3>
                    <Badge variant="default">{q.status}</Badge>
                  </div>
                  <p className="text-sm text-steel-300 mt-1">{q.email} {q.phone ? `<br>${q.phone}` : ''}</p>
                  <p className="text-sm text-steel-300 mt-1"><span className="font-medium">Lieu:</span> {q.project_location}</p>
                  <p className="text-sm text-steel-300 mt-1 line-clamp-2">{q.project_description}</p>
                  <div className="flex gap-2 mt-3 flex-wrap">
                    <select value={q.status} onChange={(e) => updateStatus(q.id, e.target.value as any)} className="px-3 py-1.5 rounded-lg border border-steel-600 bg-navy-700 text-white text-sm">
                      <option value="new">Nouveau</option><option value="pending">En attente</option><option value="read">Lu</option><option value="treate">Traité</option><option value="archived">Archivé</option>
                    </select>
                  </div>
                </div>
              </div>
            </CardContent>
          </Card>
        ))}
        {quotes.length === 0 && <p className="text-steel-400 col-span-full">{t('shared.noneFound')}</p>}
      </div>
    </div>
  );
}
