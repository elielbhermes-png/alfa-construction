import os

os.makedirs('client/src/contexts', exist_ok=True)
os.makedirs('client/src/pages/admin', exist_ok=True)

i18n_ctx = """import { createContext, useContext, useState, type ReactNode } from 'react';
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
"""

supabase_ctx = """import { createClient, SupabaseClient } from '@supabase/supabase-js';
import { createContext, useContext, type ReactNode, useState } from 'react';

export type SupabaseContextValue = {
  supabase: SupabaseClient | null;
  initialized: boolean;
  loading: boolean;
};

const supabaseUrl = import.meta.env.VITE_SUPABASE_URL;
const supabaseAnonKey = import.meta.env.VITE_SUPABASE_ANON_KEY;

export const SupabaseContext = createContext<SupabaseContextValue>({
  supabase: null, initialized: false, loading: true,
});

export function SupabaseProvider({ children }: { children: ReactNode }) {
  const [supabase, setSupabase] = useState<SupabaseClient | null>(null);
  const [initialized, setInitialized] = useState(false);
  const [loading, setLoading] = useState(true);

  if (!supabaseUrl || !supabaseAnonKey) {
    setLoading(false);
    return <SupabaseContext.Provider value={{ supabase, initialized, loading }}>{children}</SupabaseContext.Provider>;
  }

  const supabaseClient = createClient(supabaseUrl, supabaseAnonKey, {
    auth: { autoRefreshToken: true, persistSession: true, detectSessionInUrl: true },
  });
  setSupabase(supabaseClient);
  setInitialized(true);
  setLoading(false);

  return <SupabaseContext.Provider value={{ supabase, initialized, loading }}>{children}</SupabaseContext.Provider>;
}

export function useSupabase(): SupabaseContextValue {
  const ctx = useContext(SupabaseContext);
  if (!ctx) throw new Error('useSupabase must be used within SupabaseProvider');
  return ctx;
}

export async function getSupabaseClient(): Promise<SupabaseClient | null> {
  if (!supabaseUrl || !supabaseAnonKey) return null;
  return createClient(supabaseUrl, supabaseAnonKey, {
    auth: { autoRefreshToken: true, persistSession: true, detectSessionInUrl: true },
  });
}
"""

with open('client/src/contexts/I18nContext.tsx', 'w') as f:
    f.write(i18n_ctx)
with open('client/src/contexts/SupabaseProvider.tsx', 'w') as f:
    f.write(supabase_ctx)

print("Contexts written")
