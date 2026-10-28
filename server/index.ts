import { serve } from "https://deno.land/std@0.168.0/http/server.ts";
import { type ServeHandlerInfo } from "https://deno.land/std@0.168.0/http/server.ts";

const corsHeaders = {
  "Access-Control-Allow-Origin": "*",
  "Access-Control-Allow-Headers": "authorization, x-client-info, apikey, content-type",
  "Access-Control-Allow-Methods": "POST, OPTIONS",
};

async function validateSupabase(env: Record<string, string | undefined>) {
  const url = env.VITE_SUPABASE_URL;
  const anonKey = env.VITE_SUPABASE_ANON_KEY;
  if (!url || !anonKey) return null;
  const { createClient } = await import("@supabase/supabase-js");
  return createClient(url, anonKey);
}

const handler: ServeHandlerInfo = (req) => {
  if (req.method === "OPTIONS") return new Response(null, { headers: corsHeaders });

  try {
    const supabase = await validateSupabase(Deno.env.toObject());
    if (!supabase) {
      return new Response(JSON.stringify({ error: "Unsupported" }), { status: 400, headers: { "Content-Type": "application/json" } });
    }

    const body = await req.json();
    const { name, company, email, phone, subject, message, privacy } = body;

    if (req.url.includes("/contact")) {
      if (!name || !email || !subject || !message || !privacy) {
        return new Response(JSON.stringify({ error: "Missing or invalid fields" }), { status: 400, headers: { "Content-Type": "application/json" } });
      }
      const { error } = await supabase.from("contact_messages").insert({
        name, company: company || null, email, phone: phone || null, subject, message, status: "new"
      });
      if (error) return new Response(JSON.stringify({ error: error.message }), { status: 500, headers: { "Content-Type": "application/json" } });
      return new Response(JSON.stringify({ success: true }), { headers: { "Content-Type": "application/json" } });
    }

    if (req.url.includes("/quotation")) {
      const { service, projectLocation, projectDescription, estimatedBudget, desiredStartDate } = body;
      if (!name || !email || !phone || !service || !projectLocation || !projectDescription) {
        return new Response(JSON.stringify({ error: "Missing or invalid fields" }), { status: 400, headers: { "Content-Type": "application/json" } });
      }
      const { error } = await supabase.from("quotation_requests").insert({
        name, company: company || null, email, phone, service_id: service, project_location: projectLocation,
        project_description: projectDescription, estimated_budget: estimatedBudget || null, desired_start_date: desiredStartDate || null, status: "new"
      });
      if (error) return new Response(JSON.stringify({ error: error.message }), { status: 500, headers: { "Content-Type": "application/json" } });
      return new Response(JSON.stringify({ success: true }), { headers: { "Content-Type": "application/json" } });
    }

    return new Response(JSON.stringify({ error: "Not found" }), { status: 404, headers: { "Content-Type": "application/json" } });
  } catch (e) {
    return new Response(JSON.stringify({ error: e.message }), { status: 500, headers: { "Content-Type": "application/json" } });
  }
};

serve(handler, { port: 4000, onListen: ({ port }) => console.log(`API on port ${port}`) });
