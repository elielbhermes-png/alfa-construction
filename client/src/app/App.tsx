import { Suspense } from 'react';
import { Routes, Route, useLocation } from 'react-router-dom';
import { Loader } from '@/components/Loader';
import { Navbar } from '@/components/Navbar';
import { Footer } from '@/components/Footer';
import { HomePage } from '@/pages/HomePage';
import { AboutPage } from '@/pages/AboutPage';
import { ServicesPage } from '@/pages/ServicesPage';
import { ProjectsPage } from '@/pages/ProjectsPage';
import { ProjectDetailPage } from '@/pages/ProjectDetailPage';
import { ContactPage } from '@/pages/ContactPage';
import { PrivacyPage } from '@/pages/PrivacyPage';
import { LegalPage } from '@/pages/LegalPage';
import { FaqPage } from '@/pages/FaqPage';
import { NotFoundPage } from '@/pages/NotFoundPage';
import { AdminLayout } from '@/pages/admin/AdminLayout';
import { Dashboard } from '@/pages/admin/Dashboard';
import { ProjectsAdmin } from '@/pages/admin/ProjectsAdmin';
import { ServicesAdmin } from '@/pages/admin/ServicesAdmin';
import { MediaAdmin } from '@/pages/admin/MediaAdmin';
import { MessagesAdmin } from '@/pages/admin/MessagesAdmin';
import { QuotesAdmin } from '@/pages/admin/QuotesAdmin';
import { SettingsPage } from '@/pages/admin/SettingsPage';
import { LoginPage } from '@/pages/admin/LoginPage';
import { I18nProvider } from '@/contexts/I18nContext';
import { SupabaseProvider } from '@/contexts/SupabaseProvider';

function AppShell() {
  const location = useLocation();
  const isAdminRoute = location.pathname.startsWith('/admin');
  return (
    <div className="min-h-screen flex flex-col bg-navy-900 text-white antialiased">
      {!isAdminRoute && <Navbar />}
      <main className="flex-1">
        <Routes>
          <Route path="/" element={<HomePage />} />
          <Route path="/a-propos" element={<AboutPage />} />
          <Route path="/nos-services" element={<ServicesPage />} />
          <Route path="/nos-realisations" element={<ProjectsPage />} />
          <Route path="/realisations/:slug" element={<ProjectDetailPage />} />
          <Route path="/contactez-nous" element={<ContactPage />} />
          <Route path="/politique-de-confidentialite" element={<PrivacyPage />} />
          <Route path="/mentions-legales" element={<LegalPage />} />
          <Route path="/faq" element={<FaqPage />} />
          <Route path="/admin/*" element={<AdminLayout />}>
            <Route path="dashboard" element={<Dashboard />} />
            <Route path="projects" element={<ProjectsAdmin />} />
            <Route path="services" element={<ServicesAdmin />} />
            <Route path="media" element={<MediaAdmin />} />
            <Route path="messages" element={<MessagesAdmin />} />
            <Route path="quotes" element={<QuotesAdmin />} />
            <Route path="settings" element={<SettingsPage />} />
          </Route>
          <Route path="/admin/login" element={<LoginPage />} />
          <Route path="*" element={<NotFoundPage />} />
        </Routes>
      </main>
      {!isAdminRoute && <Footer />}
    </div>
  );
}

export default function App() {
  return (
    <SupabaseProvider>
      <I18nProvider>
        <Suspense fallback={<Loader />}>
          <AppShell />
        </Suspense>
      </I18nProvider>
    </SupabaseProvider>
  );
}
