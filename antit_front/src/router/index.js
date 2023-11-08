import { createRouter, createWebHistory } from 'vue-router';
import Login from '@/components/LoginView.vue';
import HelloUser from '@/components/HelloUser.vue';

const routes = [
  { path: '/login', component: Login },
  { path: '/hello-user', component: HelloUser },
  { path: '/', redirect: '/login' },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;