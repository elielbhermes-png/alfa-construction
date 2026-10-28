import { useEffect, useState } from 'react';
import { Loader2 } from 'lucide-react';

export function Loader() {
  const [show, setShow] = useState(true);
  useEffect(() => {
    const t = setTimeout(() => setShow(false), 600);
    return () => clearTimeout(t);
  }, []);
  if (!show) return null;
  return (
    <div className="fixed inset-0 z-[9999] flex items-center justify-center bg-navy-900/95">
      <Loader2 className="w-8 h-8 text-accent animate-spin" />
    </div>
  );
}
