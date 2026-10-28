import os

os.makedirs('client/src/pages', exist_ok=True)

# ContactPage
contact = """import { useState } from 'react';
import { useI18n } from '@/contexts/I18nContext';
import { useSupabase } from '@/contexts/SupabaseProvider';
import { Controller, useForm } from 'react-hook-form';
import { zodResolver } from '@hookform/resolvers/zod';
import { ContactFormSchema, type ContactFormValues, QuotationFormSchema, type QuotationFormValues } from '@/lib/validation';
import { Button } from '@/components/ui/button';
import { Input } from '@/components/ui/input';
import { Textarea } from '@/components/ui/input';
import { Label } from '@/components/ui/input';
import { ArrowLeft, Mail, Phone, MapPin, FileText, User, Building, MessageSquare, Calendar, Send, Loader } from 'lucide-react';

export function ContactPage() {
  const { t } = useI18n();
  const { supabase: supabaseClient, initialized } = useSupabase();
  const [formStatus, setFormStatus] = useState<'idle' | 'loading' | 'success' | 'error'>('idle');

  const contactForm = useForm<ContactFormValues>({
    resolver: zodResolver(ContactFormSchema),
    defaultValues: { name: '', company: '', email: '', phone: '', subject: '', message: '', privacy: false },
  });

  const quotationForm = useForm<QuotationFormValues>({
    resolver: zodResolver(QuotationFormSchema),
    defaultValues: { name: '', company: '', email: '', phone: '', service: '', projectLocation: '', projectDescription: '', estimatedBudget: '', desiredStartDate: '', files: [] },
  });

  const handleSubmit = async (data: any, form: typeof contactForm) => {
    if (!initialized || !supabaseClient) { setFormStatus('error'); return; }
    try {
      setFormStatus('loading');
      const { error } = await supabaseClient.from('contact_messages').insert({
        name: data.name, company: data.company, email: data.email, phone: data.phone,
        subject: data.subject, message: data.message, status: 'new',
      });
      if (error) throw error;
      setFormStatus('success');
      form.reset();
    } catch {
      setFormStatus('error');
    }
  };

  return (
    <div className="py-16 sm:py-24 bg-navy-900/50">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="text-center mb-12 sm:mb-16">
          <h1 className="text-3xl sm:text-4xl md:text-5xl font-extrabold text-white">{t('contact.title')}</h1>
          <p className="text-steel-300 mt-4 max-w-xl mx-auto">{t('contact.subtitle')}</p>
        </div>
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
          {/* Contact Info */}
          <div className="space-y-6">
            {[
              { icon: Mail, label: 'Email', value: 'ali-safa@alfa-constructions.com' },
              { icon: Phone, label: 'Téléphone', value: '+242 06 822 22 20' },
              { icon: MapPin, label: 'Adresse', value: 'Avenue Docteur Cardorelle, Songolo, Congo' },
            ].map((item) => (
              <div key={item.label} className="flex items-start gap-4 p-4 rounded-xl border border-steel-600/20 bg-navy-800/20">
                <item.icon className="w-5 h-5 text-accent flex-shrink-0 mt-1" />
                <div><p className="text-xs text-steel-400">{item.label}</p><p className="text-sm font-medium text-white">{item.value}</p></div>
              </div>
            ))}
            <div className="p-6 rounded-xl border border-steel-600/20 bg-navy-800/20">
              <h3 className="font-bold text-white mb-2">Horaires d'ouverture</h3>
              <p className="text-sm text-steel-300">Lun - Ven : 08h00 - 18h00</p>
            </div>
          </div>
          {/* Forms */}
          <div className="space-y-6">
            <div className="p-6 rounded-xl border border-steel-600/20 bg-navy-800/20">
              <h3 className="text-lg font-bold text-white mb-4">{t('contact.submit')}</h3>
              {formStatus === 'success' && <p className="text-green-400 text-sm">{t('contact.success')}</p>}
              {formStatus === 'error' && <p className="text-red-400 text-sm">{t('contact.error')}</p>}
              <form id="contact-form" onSubmit={contactForm.handleSubmit((data) => handleSubmit(data, contactForm))} className="space-y-4">
                <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
                  <div className="col-span-full"><Input {...contactForm.register('name')} placeholder={t('contact.name')} /></div>
                  <div className="col-span-full"><Input {...contactForm.register('email')} type="email" placeholder={t('contact.email')} /></div>
                </div>
                <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
                  <div className="col-span-full"><Input {...contactForm.register('phone')} placeholder={t('contact.phone')} /></div>
                  <div className="col-span-full"><Input {...contactForm.register('subject')} placeholder={t('contact.subject')} /></div>
                </div>
                <div className="col-span-full"><Textarea {...contactForm.register('message')} rows={5} placeholder={t('contact.message')} /></div>
                <div className="flex items-center gap-2">
                  <input type="checkbox" {...contactForm.register('privacy')} className="w-4 h-4 rounded border-steel-500 bg-navy-700 accent-accent" />
                  <label className="text-sm text-steel-300">{t('contact.privacy')} {t('contact.required')}</label>
                </div>
                <Button type="submit" className="w-full sm:w-auto" disabled={formStatus === 'loading'}>
                  {formStatus === 'loading' ? <><Loader className="w-4 h-4 animate-spin mr-2" />{t('quotation.processing')}</> : <><Send className="w-4 h-4 mr-2" />{t('contact.submit')}</>}
                </Button>
              </form>
            </div>
            <div className="p-6 rounded-xl border border-steel-600/20 bg-navy-800/20">
              <h3 className="text-lg font-bold text-white mb-4">{t('contact.quotationTitle')}</h3>
              <form id="quotation-form" className="space-y-4">
                <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
                  <div className="col-span-full"><Input {...quotationForm.register('name')} placeholder={t('contact.name')} /></div>
                  <div className="col-span-full"><Input {...quotationForm.register('email')} type="email" placeholder={t('contact.email')} /></div>
                </div>
                <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
                  <div className="col-span-full"><Input {...quotationForm.register('phone')} placeholder={t('contact.phone')} /></div>
                  <div className="col-span-full"><Input {...quotationForm.register('service')} placeholder={t('contact.service')} /></div>
                </div>
                <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
                  <div className="col-span-full"><Input {...quotationForm.register('projectLocation')} placeholder={t('contact.location')} /></div>
                  <div className="col-span-full"><Input {...quotationForm.register('estimatedBudget')} placeholder={t('contact.budget')} /></div>
                </div>
                <div className="col-span-full"><Textarea {...quotationForm.register('projectDescription')} rows={4} placeholder={t('contact.description')} /></div>
                <Button type="submit" className="w-full sm:w-auto bg-green-600 hover:bg-green-500">{t('contact.quotationTitle')}</Button>
              </form>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
"""

# Privacy, Legal, Faq, NotFound
privacy = """import { useI18n } from '@/contexts/I18nContext';

export function PrivacyPage() {
  const { t } = useI18n();
  return (
    <div className="py-16 sm:py-24 bg-navy-900/50">
      <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
        <h1 className="text-3xl sm:text-4xl font-extrabold text-white mb-8">{t('legal.title')}</h1>
        <div className="space-y-6 text-steel-300 leading-relaxed">
          <p>ALFA Construction est un groupe de construction basé en République du Congo.</p>
          <p>Pour toute question relative à cette politique de confidentialité, contactez-nous à ali-safa@alfa-constructions.com.</p>
          <p><strong>Données collectées :</strong> Nom, email, téléphone, message, informations de devis.</p>
          <p><strong>Finalité :</strong> Traitement des demandes de devis et de contact.</p>
          <p><strong>Partage :</strong> Les données ne sont pas partagées avec des tiers sans autorisation.</p>
          <p><strong>Droit à l\'image :</strong> Les photographies des projets sont utilisées dans le cadre de la communication de l\'entreprise.</p>
        </div>
      </div>
    </div>
  );
}
"""

legal = """import { useI18n } from '@/contexts/I18nContext';
import { NavLink } from 'react-router-dom';

export function LegalPage() {
  const { t } = useI18n();
  return (
    <div className="py-16 sm:py-24 bg-navy-900/50">
      <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
        <h1 className="text-3xl sm:text-4xl font-extrabold text-white mb-8">{t('legal.title')}</h1>
        <div className="space-y-6 text-steel-300 leading-relaxed">
          <p><strong>Éditeur :</strong> ALFA Construction</p>
          <p><strong>Directeur de la publication :</strong> Ali Safa</p>
          <p><strong>Adresse :</strong> Avenue Docteur Cardorelle, Songolo, Congo</p>
          <p><strong>Email :</strong> ali-safa@alfa-constructions.com</p>
          <p><strong>Hébergement :</strong> Netlify, 10 America Plaza, Suite 600, San Francisco, CA 94103</p>
          <p>Ce site est un exercice de texte. Les informations publiées sont fournies à titre indicatif.</p>
          <p className="text-sm text-steel-400">Pour toute question, contactez-nous à <a href="mailto:ali-safa@alfa-constructions.com" className="text-accent hover:underline">ali-safa@alfa-constructions.com</a>.</p>
        </div>
      </div>
    </div>
  );
}
"""

faq = """import { useI18n } from '@/contexts/I18nContext';

export function FaqPage() {
  const { t } = useI18n();
  const faqs = [
    { q: t('faq.q1'), a: t('faq.a1') },
    { q: t('faq.q2'), a: t('faq.a2') },
    { q: t('faq.q3'), a: t('faq.a3') },
    { q: t('faq.q4'), a: t('faq.a4') },
    { q: t('faq.q5'), a: t('faq.a5') },
  ];
  return (
    <div className="py-16 sm:py-24 bg-navy-900/50 min-h-screen">
      <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
        <h1 className="text-3xl sm:text-4xl font-extrabold text-white text-center mb-12">{t('faq.title')}</h1>
        <div className="space-y-4">
          {faqs.map((faq, i) => (
            <div key={i} className="p-6 rounded-xl border border-steel-600/20 bg-navy-800/20">
              <h3 className="font-bold text-white">{faq.q}</h3>
              <p className="text-steel-300 text-sm mt-2">{faq.a}</p>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}
"""

notfound = """import { Link } from 'react-router-dom';
import { useI18n } from '@/contexts/I18nContext';
import { Home } from 'lucide-react';

export function NotFoundPage() {
  const { t } = useI18n();
  return (
    <div className="min-h-screen flex items-center justify-center bg-navy-900">
      <div className="text-center">
        <h1 className="text-6xl font-extrabold text-white">404</h1>
        <p className="text-steel-300 mt-4 text-xl">{t('shared.noneFound')}</p>
        <Link to="/"><button className="mt-6 px-6 py-3 rounded-lg bg-accent text-navy-900 font-semibold hover:bg-accent/90 transition-colors">Retour à l'accueil</button></Link>
      </div>
    </div>
  );
}
"""

with open('client/src/pages/ContactPage.tsx', 'w') as f:
    f.write(contact)
with open('client/src/pages/PrivacyPage.tsx', 'w') as f:
    f.write(privacy)
with open('client/src/pages/LegalPage.tsx', 'w') as f:
    f.write(legal)
with open('client/src/pages/FaqPage.tsx', 'w') as f:
    f.write(faq)
with open('client/src/pages/NotFoundPage.tsx', 'w') as f:
    f.write(notfound)

print("Additional pages written")
