import os

os.makedirs('client/src/components', exist_ok=True)
os.makedirs('client/src/components/ui', exist_ok=True)
os.makedirs('client/src/pages', exist_ok=True)

# UI components
button = """import { cva, type VariantProps } from 'class-variance-authority';
import { forwardRef, type ButtonHTMLAttributes } from 'react';
import { cn } from '@/lib/utils';

const buttonVariants = cva(
  'inline-flex items-center justify-center gap-2 rounded-lg text-sm font-semibold transition-all duration-200 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-accent focus-visible:ring-offset-2 disabled:opacity-50 disabled:cursor-not-allowed active:scale-[0.98]',
  {
    variants: {
      variant: {
        primary: 'bg-accent text-navy-900 hover:bg-accent-hover',
        secondary: 'bg-navy-700 text-white hover:bg-navy-600',
        ghost: 'bg-transparent text-steel-200 hover:bg-steel-700/50',
        outline: 'border border-steel-600 text-steel-200 hover:bg-steel-700/30',
        white: 'bg-white text-navy-900 hover:bg-white/90',
        success: 'bg-green-600 text-white hover:bg-green-500',
      },
      size: {
        sm: 'px-3 py-1.5 text-xs',
        md: 'px-4 py-2 text-sm',
        lg: 'px-6 py-3 text-base',
      },
    },
    defaultVariants: { variant: 'primary', size: 'md' },
  }
);

export interface ButtonProps extends ButtonHTMLAttributes<HTMLButtonElement>, VariantProps<typeof buttonVariants> { }

export const Button = forwardRef<HTMLButtonElement, ButtonProps>(
  ({ className, variant, size, disabled, ...props }, ref) => {
    return <button ref={ref} className={cn(buttonVariants({ variant, size, className }))} disabled={disabled} {...props} />;
  }
);
Button.displayName = 'Button';
"""

input = """import { forwardRef, type InputHTMLAttributes, type TextareaHTMLAttributes } from 'react';
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
"""

card = """import { type HTMLAttributes, forwardRef, type ReactNode } from 'react';
import { cn } from '@/lib/utils';

const Card = forwardRef<HTMLDivElement, HTMLAttributes<HTMLDivElement>>(({ className, ...props }, ref) => (
  <div ref={ref} className={cn('rounded-xl border border-steel-700 bg-navy-800/40 backdrop-blur-sm', className)} {...props} />
));
Card.displayName = 'Card';

const CardHeader = ({ className, children, ...props }: HTMLAttributes<HTMLDivElement>) => (
  <div className={cn('p-5 pb-3 flex flex-col sm:flex-row sm:items-center sm:justify-between gap-3', className)} {...props}>{children}</div>
);

const CardTitle = ({ className, children, ...props }: HTMLAttributes<HTMLHeadingElement>) => (
  <h3 className={cn('text-lg font-bold text-white', className)} {...props}>{children}</h3>
);

const CardDescription = ({ className, children, ...props }: HTMLAttributes<HTMLParagraphElement>) => (
  <p className={cn('text-sm text-steel-300', className)} {...props}>{children}</p>
);

const CardContent = ({ className, children, ...props }: HTMLAttributes<HTMLDivElement>) => (
  <div className={cn('p-5 pt-3', className)} {...props}>{children}</div>
);

const CardFooter = ({ className, children, ...props }: HTMLAttributes<HTMLDivElement>) => (
  <div className={cn('flex items-center justify-end gap-3 p-5 pt-0 border-t border-steel-600', className)} {...props}>{children}</div>
);

export { Card, CardHeader, CardTitle, CardDescription, CardContent, CardFooter };
"""

icon = """import { forwardRef, type SVGProps } from 'react';

export interface IconProps extends SVGProps<SVGSVGElement> { }

const Icon = forwardRef<SVGSVGElement, IconProps>(({ children, className, ...props }, ref) => (
  <svg ref={ref} className={className} viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth={1.5} strokeLinecap="round" strokeLinejoin="round" {...props}>
    {children}
  </svg>
));
Icon.displayName = 'Icon';
export default Icon;
"""

with open('client/src/components/ui/button.tsx', 'w') as f:
    f.write(button)
with open('client/src/components/ui/input.tsx', 'w') as f:
    f.write(input)
with open('client/src/components/ui/card.tsx', 'w') as f:
    f.write(card)
with open('client/src/components/ui/icon.tsx', 'w') as f:
    f.write(icon)

print("UI components written")
