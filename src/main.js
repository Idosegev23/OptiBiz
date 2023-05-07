// main.js
import { createApp } from 'vue';
import App from './App.vue';
import router from './router';
import { createVuetify } from 'vuetify';
import 'vuetify/dist/vuetify.min.css'; // Import Vuetify CSS

const vuetify = createVuetify({
  theme: { dark: false },
});

const app = createApp(App);
app.use(router);
app.use(vuetify);
app.mount('#app');
