import { useI18n } from '@/contexts/I18nContext';
import { useSupabase } from '@/contexts/SupabaseProvider';
import { useEffect, useState } from 'react';
import { Card, CardHeader, CardTitle, CardContent } from '@/components/ui/card';
import { Button } from '@/components/ui/button';
import { Input } from '@/components/ui';
import { Save, X } from 'lucide-react';

export function SettingsPage() {
  const { t } = useI18n();
  const { supabase: supabase_client, initialized } = useSupabase();
  const [form, setForm] = useState({
    site_name: 'ALFA CONSTRUCTION', about: '', logo: '', contact_email: 'ali-safa@alfa-constructions.com',
    phone: '+242 06 822 22 20', address: 'Avenue Docteur Cardorelle, Songolo, Congo', website: 'www.alfa-constructions.Netlify.com',
    footer: '', hours: 'Lun - Ven : 08h00 - 18h00',
  });
  const [saving, setSaving] = useState(false);

  useEffect(() => {
    if (!initialized) return;
    supabase_client!.from('site_settings').select('*').eq('key', 'site_settings')
      .then(({ data }) => { if (data && data.length) setForm({ ...form, ...JSON.parse(data[0].value) }); })
      
  }, [initialized, supabase_client]);

  const saveSettings = async () => {
    try {
      setSaving(true);
      const { data } = await supabase_client!.from('site_settings').select('*').eq('key', 'site_settings').single();
      if (data) {
        await supabase_client!.from('site_settings').update({ value: JSON.stringify(form), updated_at: new Date().toISOString() }).eq('id', data.id);
      } else {
        await supabase_client!.from('site_settings').insert({ key: 'site_settings', value: JSON.stringify(form), created_at: new Date().toISOString(), updated_at: new Date().toISOString() });
      }
      alert('Sauvegardé!');
    } catch (e: any) { alert(e.message); }
    setSaving(false);
  };

  return (
    <div className="max-w-3xl space-y-6">
      <h2 className="text-xl font-bold text-white">{t('admin.settingsTitle')}</h2>
      <div className="grid grid-cols-1 gap-6">
        <Card>
          <CardHeader><CardTitle>Informations de base</CardTitle></CardHeader>
          <CardContent className="space-y-4">
            <Input value={form.site_name} onChange={(e) => setForm({ ...form, site_name: e.target.value })} placeholder="Nom du site" />
            <Input value={form.contact_email} onChange={(e) => setForm({ ...form, contact_email: e.target.value })} placeholder="Email contact" />
            <Input value={form.phone} onChange={(e) => setForm({ ...form, phone: e.target.value })} placeholder="Téléphone" />
            <Input value={form.address} onChange={(e) => setForm({ ...form, address: e.target.value })} placeholder="Adresse" />
            <Input value={form.website} onChange={(e) => setForm({ ...form, website: e.target.value })} placeholder="Site Web" />
            <div className="flex gap-2">
              <Button onClick={saveSettings} disabled={saving}><Save className="w-4 h-4" /> {t('admin.save')}</Button>
              <Button variant="ghost" onClick={() => setForm({ ...form })}><X className="w-4 h-4" /></Button>
            </div>
          </CardContent>
        </Card>
        <Card>
          <CardHeader><CardTitle>Homepage</CardTitle></CardHeader>
          <CardContent>
            <textarea value={form.about} onChange={(e) => setForm({ ...form, about: e.target.value })} rows={6} className="w-full px-3 py-2 rounded-lg border border-steel-600 bg-navy-700 text-white" placeholder="Contenu d'accueil" />
          </CardContent>
        </Card>
        <Card>
          <CardHeader><CardTitle>Footer</CardTitle></CardHeader>
          <CardContent>
            <textarea value={form.footer} onChange={(e) => setForm({ ...form, footer: e.target.value })} rows={4} className="w-full px-3 py-2 rounded-lg border border-steel-600 bg-navy-700 text-white" placeholder="Pied de page" />
          </CardContent>
        </Card>
      </div>
    </div>
  );
}
