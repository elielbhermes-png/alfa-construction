import { useI18n } from '@/contexts/I18nContext';

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
