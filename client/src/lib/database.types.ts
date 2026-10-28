export interface Project {
  id: string; title: string; slug: string; short_description: string; description: string;
  location: string | null; category_id: string | null; cover_image_path: string | null;
  status: string; start_date: string | null; completion_date: string | null;
  created_at: string; updated_at: string;
}
export interface ProjectImage { id: string; project_id: string; storage_path: string; caption: string; alt_text: string; display_order: number; created_at: string; }
export interface Service {
  id: string; title: string; slug: string; short_description: string; description: string;
  image_path: string | null; display_order: number; status: string; created_at: string; updated_at: string;
}
export interface ContactMessage {
  id: string; name: string; company: string | null; email: string; phone: string | null;
  subject: string; message: string; status: string; created_at: string; updated_at: string;
}
export interface QuotationRequest {
  id: string; name: string; company: string | null; email: string; phone: string | null;
  service_id: string | null; project_location: string; project_description: string;
  estimated_budget: string | null; desired_start_date: string | null;
  status: string; created_at: string; updated_at: string;
}
export interface Media { id: string; storage_path: string; caption: string; alt_text: string; project_id: string | null; is_public: boolean; created_at: string; updated_at: string; }
export interface SiteSettings { key: string; value: string; created_at: string; updated_at: string; }
