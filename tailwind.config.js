/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [    
    './myapp/templates/**/*.html', // Caminho para os templates Django
    './myapp/static/js/**/*.js',   // Caminho para arquivos JS
],
  theme: {
    extend: {},
  },
  plugins: [],
}

