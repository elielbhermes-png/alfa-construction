import { forwardRef, type SVGProps } from 'react';

export interface IconProps extends SVGProps<SVGSVGElement> { }

export const Icon = forwardRef<SVGSVGElement, IconProps>(({ children, className, ...props }, ref) => (
  <svg ref={ref} className={className} viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth={1.5} strokeLinecap="round" strokeLinejoin="round" {...props}>
    {children}
  </svg>
));
Icon.displayName = 'Icon';
export default Icon;
