import { z } from 'zod';
export const ContactFormSchema = z.object({
  name: z.string().min(2), company: z.string().max(120).optional(), email: z.string().email(),
  phone: z.string().max(30).optional(), subject: z.string().min(3), message: z.string().min(10).max(5000),
  privacy: z.boolean().refine((v) => v === true),
});
export type ContactFormValues = z.infer<typeof ContactFormSchema>;
export const QuotationFormSchema = z.object({
  name: z.string().min(2), company: z.string().max(120).optional(), email: z.string().email(),
  phone: z.string().min(8), service: z.string().min(1), projectLocation: z.string().min(2),
  projectDescription: z.string().min(10).max(5000), estimatedBudget: z.string().max(50).optional(),
  desiredStartDate: z.string().max(50).optional(), files: z.array(z.any()).max(5),
});
export type QuotationFormValues = z.infer<typeof QuotationFormSchema>;
