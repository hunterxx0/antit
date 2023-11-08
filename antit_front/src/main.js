import { createApp } from 'vue';
import App from './App.vue'; // Your main App component
import router from './router'; // Your router setup

createApp(App)
  .use(router)
  .mount('#app');