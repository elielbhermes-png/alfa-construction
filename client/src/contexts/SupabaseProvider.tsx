import { createClient, SupabaseClient } from '@supabase/supabase-js';
import { createContext, useContext, type ReactNode, useState } from 'react';

export type SupabaseContextValue = {
  supabase: SupabaseClient | null;
  initialized: boolean;
  loading: boolean;
};

const supabaseUrl = import.meta.env.VITE_SUPABASE_URL;
const supabaseAnonKey = import.meta.env.VITE_SUPABASE_ANON_KEY;

export const SupabaseContext = createContext<SupabaseContextValue>({ supabase: null, initialized: false, loading: true });

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
  return createClient(supabaseUrl, supabaseAnonKey, { auth: { autoRefreshToken: true, persistSession: true, detectSessionInUrl: true } });
}
