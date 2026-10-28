import { cva, type VariantProps } from 'class-variance-authority';
import { forwardRef, type ButtonHTMLAttributes, type ReactNode, isValidElement, cloneElement } from 'react';
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

export interface ButtonProps extends ButtonHTMLAttributes<HTMLButtonElement>, VariantProps<typeof buttonVariants> { asChild?: boolean; }

export const Button = forwardRef<HTMLButtonElement, ButtonProps>(
  ({ className, variant, size, disabled, asChild = false, children, ...props }, ref) => {
    if (asChild && isValidElement<{ className?: string }>(children)) {
      return (
        <span className={cn(buttonVariants({ variant, size }))}>
          {cloneElement(children, { className: cn(children.props.className, className) })}
        </span>
      );
    }
    return (
      <button ref={ref} className={cn(buttonVariants({ variant, size, className }))} disabled={disabled} {...props}>
        {children}
      </button>
    );
  }
);
Button.displayName = 'Button';
