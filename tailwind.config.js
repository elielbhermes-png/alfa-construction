/** @type {import('tailwindcss').Config} */
export default {
  content: ['./client/index.html', './client/src/**/*.{ts,tsx}'],
  theme: {
    extend: {
      colors: {
        navy: { 900: '#0B0F14', 800: '#11161F', 700: '#161D2B', 600: '#1C2536', 500: '#243044', 400: '#2E3F57', 300: '#3A4E68', 200: '#4B607B', 100: '#5C748F', 50: '#839ABC' },
        steel: { 900: '#0E1218', 800: '#141B27', 700: '#1A2433', 600: '#212E40', 500: '#293A4E', 400: '#34465E', 300: '#41546D', 200: '#50647C', 100: '#60758D', 50: '#8799B2' },
        accent: { 500: '#D4AF37', 400: '#C99A28', 300: '#B8861A', 200: '#A07418', 100: '#886214', 50: '#D8C49A' },
      },
      fontFamily: { sans: ['Inter', 'system-ui', '-apple-system', 'BlinkMacSystemFont', 'Segoe UI', 'Roboto', 'sans-serif'] },
      container: { center: true, screens: { '2xl': '1280px' } },
    },
  },
  plugins: [],
};
