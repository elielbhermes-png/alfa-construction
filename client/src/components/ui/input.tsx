import { forwardRef, type InputHTMLAttributes, type TextareaHTMLAttributes } from 'react';
import { cn } from '@/lib/utils';

export interface InputProps extends InputHTMLAttributes<HTMLInputElement> { }
export interface TextareaProps extends TextareaHTMLAttributes<HTMLTextAreaElement> { }

export const Input = forwardRef<HTMLInputElement, InputProps>(({ className, type, ...props }, ref) => (
  <input ref={ref} type={type} className={cn('w-full px-4 py-2.5 rounded-lg border border-steel-600 bg-navy-800/50 text-white placeholder-steel-400 focus:outline-none focus:border-accent focus:ring-1 focus:ring-accent transition-colors', className)} {...props} />
));
Input.displayName = 'Input';

export const Textarea = forwardRef<HTMLTextAreaElement, TextareaProps>(({ className, ...props }, ref) => (
  <textarea ref={ref} className={cn('w-full px-4 py-2.5 rounded-lg border border-steel-600 bg-navy-800/50 text-white placeholder-steel-400 focus:outline-none focus:border-accent focus:ring-1 focus:ring-accent transition-colors resize-none', className)} {...props} />
));
Textarea.displayName = 'Textarea';
