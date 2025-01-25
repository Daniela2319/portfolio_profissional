/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [    
    './myapp/templates/**/*.html', // Caminho para os templates Django
    './myapp/static/**/*.css', // Caminho para os arquivos CSS
    // "./myapp/static/**/*.js", // Caminho para os arquivos JS
],
  theme: {
    extend: { transitionDuration: {
      500: "500ms",
    },
    rotate: {
      180: "180deg",
    },
  },
  },
  plugins: [],
}

