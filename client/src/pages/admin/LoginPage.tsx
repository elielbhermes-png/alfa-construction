import { useState } from 'react';
import { useNavigate, NavLink } from 'react-router-dom';
import { useForm } from 'react-hook-form';
import { zodResolver } from '@hookform/resolvers/zod';
import { z } from 'zod';
import { useSupabase } from '@/contexts/SupabaseProvider';
import { useI18n } from '@/contexts/I18nContext';
import { Button } from '@/components/ui/button';
import { Input } from '@/components/ui/input';
import { Loader } from '@/components/Loader';
import { Mail, Lock, ArrowRight } from 'lucide-react';

const loginSchema = z.object({
  email: z.string().email(),
  password: z.string().min(1),
});
type LoginForm = z.infer<typeof loginSchema>;

export function LoginPage() {
  const { t } = useI18n();
  const { supabase, initialized } = useSupabase();
  const navigate = useNavigate();
  const [loading, setLoading] = useState(true);

  const { register, handleSubmit, formState: { errors } } = useForm<LoginForm>({
    resolver: zodResolver(loginSchema),
    defaultValues: { email: '', password: '' },
  });

  if (!initialized || !supabase) {
    return <div className="min-h-screen flex items-center justify-center">{t('shared.loading')}</div>;
  }

  const onSubmit = async (data: LoginForm) => {
    try {
      setLoading(true);
      const { error } = await supabase.auth.signInWithPassword({ email: data.email, password: data.password });
      if (error) throw error;
      navigate('/admin/dashboard');
    } catch (e: any) {
      alert(e.message || 'Échec de la connexion');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen flex items-center justify-center bg-navy-900">
      <div className="w-full max-w-md p-8 rounded-2xl border border-steel-700/50 bg-navy-800/30">
        <h1 className="text-2xl font-extrabold text-white text-center mb-8">{t('admin.login')}</h1>
        <form onSubmit={handleSubmit(onSubmit)} className="space-y-4">
          <div className="mb-4">
            <Input {...register('email')} type="email" placeholder="Email" />
            {errors.email && <p className="text-red-400 text-sm mt-1">{errors.email.message}</p>}
          </div>
          <div className="mb-6">
            <Input {...register('password')} type="password" placeholder="Mot de passe" />
            {errors.password && <p className="text-red-400 text-sm mt-1">{errors.password.message}</p>}
          </div>
          <Button type="submit" className="w-full" disabled={loading}>
            {loading && <Loader />}
            {t('admin.signIn')}
          </Button>
        </form>
        <p className="mt-6 text-xs text-steel-400 text-center">Vitrine : <NavLink to="/" className="text-accent hover:underline">www.alfa-constructions.Netlify.com</NavLink></p>
      </div>
    </div>
  );
}
