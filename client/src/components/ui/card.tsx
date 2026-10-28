import { type HTMLAttributes, forwardRef, type ReactNode } from 'react';
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
