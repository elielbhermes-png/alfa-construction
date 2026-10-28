import { createContext, useContext, useState, type ReactNode } from 'react';
import { frTranslations, enTranslations } from '@/lib/i18n';

type I18nContextValue = {
  locale: 'fr' | 'en';
  setLocale: (l: 'fr' | 'en') => void;
  t: (k: string) => string;
};

const I18nContext = createContext<I18nContextValue | null>(null);

export function I18nProvider({ children }: { children: ReactNode }) {
  const [locale, setLocale] = useState<'fr' | 'en'>('fr');
  const t = (key: string): string => {
    const keys = key.split('.');
    let value: unknown = locale === 'fr' ? frTranslations : enTranslations;
    for (const k of keys) {
      if (typeof value !== 'object' || value === null) return key;
      value = (value as Record<string, unknown>)[k];
    }
    return typeof value === 'string' ? value : key;
  };
  return <I18nContext.Provider value={{ locale, setLocale, t }}>{children}</I18nContext.Provider>;
}

export function useI18n() {
  const ctx = useContext(I18nContext);
  if (!ctx) throw new Error('useI18n must be used within I18nProvider');
  return ctx;
}
