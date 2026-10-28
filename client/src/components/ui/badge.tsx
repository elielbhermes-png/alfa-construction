import { type VariantProps, cva } from 'class-variance-authority';
import { type HTMLAttributes } from 'react';
import { cn } from '@/lib/utils';

const badgeVariants = cva(
  'inline-flex items-center gap-1.5 px-2.5 py-0.5 rounded-full text-xs font-semibold transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-accent focus-visible:ring-offset-2',
  {
    variants: {
      variant: {
        default: 'bg-steel-700/50 text-steel-300',
        success: 'bg-green-600/50 text-green-300',
        warning: 'bg-amber-600/50 text-amber-300',
        danger: 'bg-red-600/50 text-red-300',
        outline: 'bg-transparent text-steel-300 border border-steel-600',
      },
    },
    defaultVariants: { variant: 'default' },
  }
);

export interface BadgeProps extends HTMLAttributes<HTMLSpanElement>, VariantProps<typeof badgeVariants> {}

export function Badge({ className, variant, ...props }: BadgeProps) {
  return <span className={cn(badgeVariants({ variant }), className)} {...props} />;
}
