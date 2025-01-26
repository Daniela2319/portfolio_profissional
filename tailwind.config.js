/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [    
    './myapp/templates/**/*.html', // Caminho para os templates Django
    // './static/**/*.css', // Caminho para os arquivos CSS
    "./static/**/*.js", // Caminho para os arquivos JS
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

